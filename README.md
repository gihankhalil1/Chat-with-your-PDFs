# Chat with Your PDFs 📚

Welcome to the **Chat with Your PDFs** application! This project allows you to upload PDF files, extract their content, and have an interactive chat experience with the information in those PDFs. Leveraging Google’s Generative AI and FAISS for efficient document retrieval, this app provides a user-friendly way to interact with your documents.

---

## Features

- **Upload Multiple PDFs**: Upload one or more PDF files for processing.
- **Text Extraction**: Extracts text from the uploaded PDFs for further analysis.
- **Embeddings with Google Generative AI**: Uses Google Generative AI to create embeddings for document retrieval.
- **Conversational AI**: Allows you to ask questions and have a conversation with the content of your PDFs.
- **Multilingual Support**: Automatically detects and responds in the language and tone of your input (formal, informal, or neutral).
- **Memory Integration**: Maintains context with a conversation buffer memory.
- **Custom Prompts**: Handles ambiguous or casual queries with clarity and politeness.

---

## Tech Stack

- **Python**: Core programming language.
- **Streamlit**: Web framework for building the application.
- **PyPDF2**: For extracting text from PDF files.
- **FAISS**: For efficient similarity search and clustering of embeddings.
- **LangChain**: For building conversational retrieval chains.
- **Google Generative AI**: Used for embedding creation and conversational LLMs.
- **dotenv**: For managing environment variables.

---

## Setup and Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- pip (Python package installer)

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/chat-with-pdfs.git
   cd chat-with-pdfs
   ```

2. **Set Up Virtual Environment** (optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   Install the required packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Key**

   - Create a `.env` file in the root directory.
   - Add your Google API key to the `.env` file:

     ```env
     GOOGLE_API_KEY=your_google_api_key
     ```

5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

6. **Access the App**

   Open your browser and navigate to `http://localhost:8501`.

---

## How It Works

1. **Upload PDFs**
   - Use the sidebar to upload one or more PDF documents.
   
2. **Processing**
   - The app extracts text from the uploaded PDFs and splits it into manageable chunks.
   - Embeddings are generated using Google Generative AI.
   - A FAISS vector store is created for efficient retrieval.

3. **Ask Questions**
   - Enter your questions or commands in the input box.
   - The app uses a conversational retrieval chain to provide relevant and contextual responses based on the content of your PDFs.

4. **Multilingual Responses**
   - The app detects the language and tone of your input and mirrors it in the response.

---

## File Structure

```plaintext
chat-with-pdfs/
|-- app.py              # Main application file
|-- htmlTemplates.py    # HTML templates for Streamlit UI
|-- requirements.txt    # Python dependencies
|-- .env                # Environment variables (not included in repo)
|-- README.md           # Documentation
```

---

## Dependencies

Key libraries and frameworks used in this project:

- `streamlit`
- `PyPDF2`
- `langchain`
- `faiss-cpu`
- `google-generativeai`
- `python-dotenv`

Refer to the `requirements.txt` for the full list of dependencies.

---

## Usage Examples

- **Upload PDFs**: Drag and drop PDF files into the sidebar uploader.
- **Ask a Question**: Type questions like:
  - "Summarize the document."
  - "What does page 3 talk about?"
- **Language Support**:
  - Input: "Expliquez ce document." (French)
  - Response: App will reply in French.



---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests on [GitHub](https://github.com/gihankhalil1/chat-with-pdfs).

---

## Acknowledgments

- [Google Generative AI](https://ai.google/) for their powerful tools.
- [LangChain](https://www.langchain.com/) for simplifying conversational AI workflows.
- [Streamlit](https://streamlit.io/) for making data apps easier to build.
