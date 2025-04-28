from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

import openai

app = Flask(__name__)

# Get OpenAI API key from environment
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET'])
def home():
    return 'Qadeer Resume Builder API is Live 🚀'

@app.route('/generate-resume', methods=['POST'])
def generate_resume():
    data = request.get_json()

    # Safely extract all required fields
    full_name = data.get('full_name', '')
    current_job_title = data.get('current_job_title', '')
    address = data.get('address', '')
    phone_number = data.get('phone_number', '')
    email = data.get('email', '')
    summary = data.get('summary', '')
    current_company_name = data.get('current_company_name', '')
    current_job_start_date = data.get('current_job_start_date', '')
    current_job_description = data.get('current_job_description', '')
    previous_company_name = data.get('previous_company_name', '')
    previous_job_title = data.get('previous_job_title', '')
    previous_job_start_date = data.get('previous_job_start_date', '')
    previous_job_end_date = data.get('previous_job_end_date', '')
    previous_job_description = data.get('previous_job_description', '')
    old_company_name = data.get('old_company_name', '')
    old_job_title = data.get('old_job_title', '')
    old_job_start_date = data.get('old_job_start_date', '')
    old_job_end_date = data.get('old_job_end_date', '')
    old_job_description = data.get('old_job_description', '')
    first_university_major = data.get('1st_university_major', '')
    first_university_name = data.get('1st_university_name', '')
    first_university_location = data.get('1st_university_location', '')
    second_university_major = data.get('2nd_university_major', '')
    second_university_name = data.get('2nd_university_name', '')
    second_university_location = data.get('2nd_university_location', '')
    skills = data.get('skills', '')
    achievements = data.get('achievements', '')
    languages = data.get('languages', '')

    # Build the structured JSON response
    resume_data = {
        "full_name": full_name,
        "current_job_title": current_job_title,
        "address": address,
        "phone_number": phone_number,
        "email": email,
        "summary": summary,
        "current_company_name": current_company_name,
        "current_job_start_date": current_job_start_date,
        "current_job_description": current_job_description,
        "previous_company_name": previous_company_name,
        "previous_job_title": previous_job_title,
        "previous_job_start_date": previous_job_start_date,
        "previous_job_end_date": previous_job_end_date,
        "previous_job_description": previous_job_description,
        "old_company_name": old_company_name,
        "old_job_title": old_job_title,
        "old_job_start_date": old_job_start_date,
        "old_job_end_date": old_job_end_date,
        "old_job_description": old_job_description,
        "1st_university_major": first_university_major,
        "1st_university_name": first_university_name,
        "1st_university_location": first_university_location,
        "2nd_university_major": second_university_major,
        "2nd_university_name": second_university_name,
        "2nd_university_location": second_university_location,
        "skills": skills,
        "achievements": achievements,
        "languages": languages
    }

    return jsonify(resume_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


