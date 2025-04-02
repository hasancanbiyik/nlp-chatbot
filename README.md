# NLP Chatbot with Transformer Models

This project implements a multi-turn conversational chatbot using the pre-trained [DialoGPT-small](https://huggingface.co/microsoft/DialoGPT-small) model from Hugging Face. The chatbot is built using Flask for the web interface and PyTorch for running the model. It maintains conversation context across multiple turns using Flask sessions.

## Features

- **Multi-Turn Conversations:** Maintains conversation history to support context-aware dialogues.
- **Simple Web Interface:** A lightweight HTML/CSS/JavaScript interface for chatting.
- **Transformer-based NLP:** Leverages the state-of-the-art DialoGPT-small model for generating responses.
- **Easy Deployment:** Ready for local development and can be extended for cloud deployment.


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/nlp-chatbot.git
   cd nlp-chatbot

2. **Create and activate a virtual environment (optional but recommended):**
python3 -m venv venv
source venv/bin/activate

3. **Install the required dependencies:**
pip install -r requirements.txt

## Usage
1. Run the Flask application:
python app.py

2. Open your web browser and navigate to http://127.0.0.1:5000.

3. Start chatting!
Enter your message and press Enter or click the Send button. The chatbot will respond and maintain context over multiple turns.

## Future Improvements
- Enhanced Conversation Memory: Extend the context window or use a more advanced model for longer conversations.
- Improved UI/UX: Enhance the front-end with a modern framework or custom styling.
- Deployment: Deploy the application on platforms like Heroku, AWS, or Google Cloud.
- Logging and Analytics: Implement logging for conversation analysis and performance monitoring.
- Testing: Add unit and integration tests to ensure robustness.

## Contributing
Contributions are welcome! If you have ideas for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
