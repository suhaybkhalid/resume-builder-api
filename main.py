from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET'])
def home():
    return 'Qadeer Resume Builder AI Engine is Live 🚀'

@app.route('/generate-resume', methods=['POST'])
def generate_resume():
    data = request.get_json()

    # Receive all fields from the form
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

    # Generate enhanced resume parts using GPT-4
    def ask_openai(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional resume writer. Make text professional, brief, and bullet point formatted where appropriate."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']

    # Prompts for AI
    enhanced_summary = ask_openai(f"Rewrite this into a professional resume summary paragraph: {summary}")

    enhanced_current_job = ask_openai(
        f"Create 3 professional bullet points describing the job role based on this input for a resume: {current_job_description}"
    )

    enhanced_previous_job = ask_openai(
        f"Create 3 professional bullet points describing the previous job role based on this input for a resume: {previous_job_description}"
    )

    enhanced_old_job = ask_openai(
        f"Create 3 professional bullet points describing the older job role based on this input for a resume: {old_job_description}"
    )

    enhanced_skills = ask_openai(
        f"Organize these skills into a clean professional bullet list for a resume: {skills}"
    )

    enhanced_achievements = ask_openai(
        f"Rewrite and structure these achievements into a clean professional bullet list for a resume: {achievements}"
    )

    enhanced_languages = ask_openai(
        f"Organize these languages into a clean professional list for a resume: {languages}"
    )

    # Build the structured resume output
    resume_data = {
        "full_name": full_name,
        "current_job_title": current_job_title,
        "address": address,
        "phone_number": phone_number,
        "email": email,
        "summary": enhanced_summary,
        "current_company_name": current_company_name,
        "current_job_start_date": current_job_start_date,
        "current_job_description": enhanced_current_job,
        "previous_company_name": previous_company_name,
        "previous_job_title": previous_job_title,
        "previous_job_start_date": previous_job_start_date,
        "previous_job_end_date": previous_job_end_date,
        "previous_job_description": enhanced_previous_job,
        "old_company_name": old_company_name,
        "old_job_title": old_job_title,
        "old_job_start_date": old_job_start_date,
        "old_job_end_date": old_job_end_date,
        "old_job_description": enhanced_old_job,
        "skills": enhanced_skills,
        "achievements": enhanced_achievements,
        "1st_university_major": first_university_major,
        "1st_university_name": first_university_name,
        "1st_university_location": first_university_location,
        "2nd_university_major": second_university_major,
        "2nd_university_name": second_university_name,
        "2nd_university_location": second_university_location,
        "languages": enhanced_languages
    }

    return jsonify(resume_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
