css = '''
<style>
.chat-container {
    max-width: 800px;
    margin: 0 auto;
}

.chat-message {
    padding: 1.5rem;
    border-radius: 0.8rem;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.chat-message.user {
    background-color: #2b313e;
}

.chat-message.bot {
    background-color: #475063;
}

.chat-message .avatar {
    width: 15%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.chat-message .avatar img {
    max-width: 64px;
    max-height: 64px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #fff;
}

.chat-message .message {
    width: 80%;
    padding: 0 1rem;
    color: #fff;
    font-size: 1rem;
    line-height: 1.5;
    word-wrap: break-word;
}

.chat-message:hover {
    transform: translateY(-2px);
    transition: all 0.3s ease-in-out;
}

body {
    background-color: #1e1e2f;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #fff;
    padding: 1rem;
}

h1 {
    text-align: center;
    color: #fff;
    margin-bottom: 2rem;
}

button {
    background-color: #4caf50;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #45a049;
}

input {
    padding: 0.7rem;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 100%;
    box-sizing: border-box;
    margin-bottom: 1rem;
    font-size: 1rem;
}

input:focus {
    border-color: #4caf50;
    outline: none;
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
}
</style>
'''










bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/Dt2PmKF/chatbot.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''


user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/wy5zNyy/two-rounded-rectangle-chatbox.png" alt="User Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''




