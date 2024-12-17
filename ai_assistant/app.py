from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from gpt4all import GPT4All
import os

# Initialize Flask App
app = Flask(__name__, static_folder="frontend", static_url_path="/")
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend

# Load GPT4All Model
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", model_path="./models")

@app.route("/")
def serve_index():
    """Serve the main HTML file."""
    return send_from_directory(app.static_folder, "index.html")

@app.route("/ask", methods=["POST"])
def ask_ai():
    """
    Handle AI queries from the frontend.
    """
    try:
        # Get the user's question from the request
        data = request.get_json()
        question = data.get("question", "")

        # Validate input
        if not question:
            return jsonify({"error": "Question is required!"}), 400

        # Generate AI response
        with model.chat_session():
            response = model.generate(question, max_tokens=100)

        # Return the response
        return jsonify({"answer": response})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong on the server!"}), 500

# Run the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
