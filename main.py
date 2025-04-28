from flask import Flask, request, jsonify
import openai
from docx import Document
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get OpenAI API Key from environment
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

@app.route('/', methods=['GET'])
def home():
    return 'Qadeer Resume Builder API is Live 🚀'

@app.route('/generate-resume', methods=['POST'])
def generate_resume():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')

    prompt = f"Create a professional English resume for {name}, email {email}."

    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {"role": "system", "content": "You are a professional resume formatter."},
            {"role": "user", "content": prompt}
        ]
    )

    resume_content = response['choices'][0]['message']['content']

    return jsonify({"resume": resume_content})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

