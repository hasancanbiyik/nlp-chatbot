from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load the pre-trained DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.route("/")
def index():
    # Render the chat interface
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Get the user message from the request
    user_input = request.json.get("message")
    
    # Encode the user input and add the end-of-string token
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    
    # Generate a response from the model (this is a single-turn conversation)
    bot_output_ids = model.generate(new_user_input_ids,
                                    max_length=1000,
                                    pad_token_id=tokenizer.eos_token_id)
    
    # Decode the generated tokens to string
    bot_output = tokenizer.decode(bot_output_ids[:, new_user_input_ids.shape[-1]:][0],
                                  skip_special_tokens=True)
    
    # Return the response as JSON
    return jsonify({"response": bot_output})

if __name__ == "__main__":
    app.run(debug=True)