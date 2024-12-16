import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template
import google.generativeai as genai
from langchain.schema import HumanMessage, AIMessage  # <-- Import these classes

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a multilingual prompt template
def create_multilingual_tone_prompt(user_question, chat_history=None):
    base_prompt = """
    You are a highly intelligent and conversational assistant with the following abilities:
    - Automatically detect the language and tone (formal, informal, or neutral) of the user's input.
    - Respond in the user's detected language and mirror their tone (formal, informal, or neutral) in a natural and conversational manner.
    - If the user's input is ambiguous or unclear, ask for clarification in a polite and friendly way while maintaining the detected language and tone.
    - Handle informal or casual language appropriately without rejecting it. For example, if the user asks "What's up?" or "How's it going?", respond conversationally.
    - If explicitly requested, translate your response to the user's preferred language (e.g., "Translate to English").
    - Maintain politeness, empathy, and helpfulness in all your responses.

    Example scenarios:
    1. User (informal): "Yo, how's it going?"
       Assistant: "Hey there! I'm doing great, thanks for asking. How can I help you today?"

    2. User (formal): "Could you please provide an overview of AI?"
       Assistant: "Of course! AI, or artificial intelligence, refers to systems designed to simulate human intelligence..."

    3. User (neutral): "Tell me about machine learning."
       Assistant: "Sure! Machine learning is a branch of AI that allows systems to learn patterns from data without being explicitly programmed."

    4. User (unclear): "Explain this!"
       Assistant: "I'd love to help! Could you clarify what you'd like me to explain?"

    Chat history (if any):
    {history}

    User's question:
    {question}
    """
    history_text = "\n".join(
        [f"User: {msg.content}" if isinstance(msg, HumanMessage) else f"Assistant: {msg.content}" for msg in chat_history]
    ) if chat_history else "None"
    return base_prompt.format(history=history_text, question=user_question)

# Extract text from PDFs
def get_pdf_text(pdf_docs):
    """Extract text from a list of uploaded PDF documents."""
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Split text into manageable chunks
def get_text_chunks(text):
    """Split large text into smaller chunks for efficient processing."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return text_splitter.split_text(text)

# Generate and store embeddings in a vector store
def get_vectorstore(text_chunks):
    """Create a FAISS vector store from text chunks using embeddings."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_texts(text_chunks, embedding=embeddings)
    vectorstore.save_local("faiss_index")
    return vectorstore

# Initialize a conversational chain
def get_conversational_chain(vectorstore):
    """Create a conversational retrieval chain with memory."""
    try:
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        return ConversationalRetrievalChain.from_llm(
            llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3),
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
    except Exception as e:
        st.error(f"Error initializing conversational chain: {e}")
        raise

# Handle user input
def handle_user_input(user_question):
    """Process user input and update chat history."""
    if "user_facts" not in st.session_state:
        st.session_state.user_facts = {}

    if user_question.lower().startswith("remember this:"):
        fact = user_question[len("remember this:"):].strip()
        st.session_state.user_facts[f"Fact {len(st.session_state.user_facts) + 1}"] = fact
        st.write(bot_template.replace("{{MSG}}", "Got it! I'll remember that."), unsafe_allow_html=True)
    elif user_question.lower().startswith("what do you remember?"):
        if st.session_state.user_facts:
            remembered_facts = "\n".join([f"{key}: {value}" for key, value in st.session_state.user_facts.items()])
            st.write(bot_template.replace("{{MSG}}", f"Here’s what I remember:\n{remembered_facts}"), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", "I don't have anything to remember yet!"), unsafe_allow_html=True)
    else:
        prompt = create_multilingual_tone_prompt(user_question, chat_history=st.session_state.chat_history)
        response = st.session_state.conversation({"question": user_question})
        st.session_state.chat_history = response["chat_history"]

        for i, message in enumerate(st.session_state.chat_history):
            template = user_template if i % 2 == 0 else bot_template
            st.write(template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

# Main function
def main():
    """Main Streamlit application function."""

    st.set_page_config(page_title="Chat with your PDFs", page_icon="📚")
    st.write(css, unsafe_allow_html=True)

    # Initialize session state variables
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []  

    st.title("Chat with your PDFs 📚")
    user_question = st.text_input("Share Your Thoughts or Ask Anything You Want!!")
    if user_question:
        handle_user_input(user_question)

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here", type=["pdf"], accept_multiple_files=True)

        if st.button("Process"):
            with st.spinner("Processing your uploaded files..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.success("Done!")
                st.session_state.conversation = get_conversational_chain(vectorstore)

if __name__ == '__main__':
    main()
