from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
client = OpenAI(api_key="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")

# Optionally, set the fine-tuned model ID
FINE_TUNED_MODEL = "ftjob-aHLySRVYtPvGvaHXupAwC9La" 


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if not data or 'message' not in data:
        return jsonify({"error": "Invalid request. 'message' field is required."}), 400

    user_message = data['message']

    # Define system prompt
    system_prompt = (
        "You are a helpful assistant that assists with everything Python (coding) and "
        "only Python. You were designed to help the Computer Science Students of Morgan "
        "State University help debug, create code, and become better coders."
    )

    try:
        # Create a chat completion
        response = openai.ChatCompletion.create(
            model=FINE_TUNED_MODEL,  # Use the fine-tuned model if available
            # model="gpt-4",  # Uncomment to use standard GPT-4
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,  # Adjust as needed
            max_tokens=150,    # Adjust based on response length requirements
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        assistant_message = response['choices'][0]['message']['content'].strip()

        return jsonify({"message": assistant_message}), 200

    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        # Handle general errors
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
