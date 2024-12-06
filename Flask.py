from flask import Flask, request, jsonify, render_template, session, redirect, url_for
import openai
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'

openai.api_key = os.getenv("OPENAI_API_KEY")

FINE_TUNED_MODEL = 'ft:gpt-4o-mini-2024-07-18:personal::ADXHfnAj'

def test_new_model(prompt):
    try:
        
        prompt_lower = prompt.lower()

        
        if 'gpa calculator' in prompt_lower:
            session['asked_schedule'] = False
            return ('The GPA Calculator feature is built into this bot! Please use the **GPA Calculator** option in the sidebar menu '
                    'to calculate your GPA with ease.')

        if 'scholarships' in prompt_lower:
            session['asked_schedule'] = True
            return ('Scholarship information is available in the sidebar menu. Please select the **Scholarships** option to explore opportunities.')

        if 'academic calendar' in prompt_lower:
            session['asked_schedule'] = False
            return 'You can view the <strong>Academic Calendar</strong> <a href="https://www.morgan.edu/academic-calendar" target="_blank" style="color: #007bff;">here</a>.'

        if 'morgan home page' in prompt_lower or 'morgan university' in prompt_lower:
            session['asked_schedule'] = False
            return ('Looking for the Morgan State University homepage? Please use the **Morgan State Home Page** option in the sidebar menu, '
                    'or visit it directly <a href="https://www.morgan.edu" target="_blank" style="color: #007bff;">here</a>.')
        
        
        response = openai.ChatCompletion.create(
            model=FINE_TUNED_MODEL,
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant that assists with making sure Morgan State students are successful with coursework and coding.'},
                {'role': 'user', 'content': prompt}
            ],
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['message']['content']
    
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"message": "No message provided"})
    
    user_message = data['message']
    bot_response = test_new_model(user_message)

    return jsonify({
        'message': bot_response,
        'imageUrl': 'https://example.com/logo.png' if 'logo' in user_message.lower() else None
    })

@app.route('/gpa-calculator')
def gpa_calculator():
    return render_template('gpa_calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
