from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Initialize OpenAI
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
  # <<-- Replace this with your real OpenAI key

@app.route("/", methods=["POST"])
def generate_resume():
    # Step 1: Normally get data from POST (but override for testing)
    # request_data = request.get_json()

    # 🔥 TEMPORARY Dummy Data for Testing
    request_data = {
        "full_name": "John Doe",
        "current_job_title": "Software Engineer",
        "address": "123 Main Street, Riyadh",
        "phone_number": "+966501234567",
        "email": "john.doe@example.com",
        "summary": "Experienced software engineer focused on automation.",
        "current_company_name": "Tech Corp",
        "current_job_start_date": "2021-05-01",
        "current_job_description": "Developed AI solutions.",
        "previous_company_name": "InnoTech",
        "previous_job_title": "Developer",
        "previous_job_start_date": "2019-02-01",
        "previous_job_end_date": "2021-04-30",
        "previous_job_description": "Built scalable backend systems.",
        "old_company_name": "StartApp",
        "old_job_title": "Junior Developer",
        "old_job_start_date": "2017-01-01",
        "old_job_end_date": "2018-12-31",
        "old_job_description": "Helped in mobile app development.",
        "1st_university_major": "Computer Science",
        "1st_univeristy_name": "King Saud University",
        "1st_university_location": "Riyadh",
        "2nd_university_major": "Software Engineering",
        "2nd_univeristy_name": "Prince Sultan University",
        "2nd_university_location": "Riyadh",
        "skills": "Python, Flask, React, SQL, AI",
        "achievements": "Employee of the Year 2022",
        "languages": "English, Arabic"
    }
    # 🔥 End Dummy Data

    # Step 2: Extract all fields
    full_name = request_data.get('full_name', '')
    current_job_title = request_data.get('current_job_title', '')
    address = request_data.get('address', '')
    phone_number = request_data.get('phone_number', '')
    email = request_data.get('email', '')
    summary = request_data.get('summary', '')
    current_company_name = request_data.get('current_company_name', '')
    current_job_start_date = request_data.get('current_job_start_date', '')
    current_job_description = request_data.get('current_job_description', '')
    previous_company_name = request_data.get('previous_company_name', '')
    previous_job_title = request_data.get('previous_job_title', '')
    previous_job_start_date = request_data.get('previous_job_start_date', '')
    previous_job_end_date = request_data.get('previous_job_end_date', '')
    previous_job_description = request_data.get('previous_job_description', '')
    old_company_name = request_data.get('old_company_name', '')
    old_job_title = request_data.get('old_job_title', '')
    old_job_start_date = request_data.get('old_job_start_date', '')
    old_job_end_date = request_data.get('old_job_end_date', '')
    old_job_description = request_data.get('old_job_description', '')
    first_university_major = request_data.get('1st_university_major', '')
    first_university_name = request_data.get('1st_univeristy_name', '')
    first_university_location = request_data.get('1st_university_location', '')
    second_university_major = request_data.get('2nd_university_major', '')
    second_university_name = request_data.get('2nd_univeristy_name', '')
    second_university_location = request_data.get('2nd_university_location', '')
    skills = request_data.get('skills', '')
    achievements = request_data.get('achievements', '')
    languages = request_data.get('languages', '')

    # Step 3: Build the professional OpenAI prompt
    user_data = f"""
Please create a professional and powerful resume using the following details:

Personal Information:
- Full Name: {full_name}
- Professional Title: {current_job_title}
- Address: {address}
- Phone Number: {phone_number}
- Email: {email}

Professional Summary:
{summary}

Experience:
- Current Company: {current_company_name}
  - Job Title: {current_job_title}
  - Start Date: {current_job_start_date}
  - Description: {current_job_description}

- Previous Company: {previous_company_name}
  - Job Title: {previous_job_title}
  - Start Date: {previous_job_start_date}
  - End Date: {previous_job_end_date}
  - Description: {previous_job_description}

- Older Company: {old_company_name}
  - Job Title: {old_job_title}
  - Start Date: {old_job_start_date}
  - End Date: {old_job_end_date}
  - Description: {old_job_description}

Education:
- {first_university_major}, {first_university_name}, {first_university_location}
- {second_university_major}, {second_university_name}, {second_university_location}

Skills:
{skills}

Achievements:
{achievements}

Languages:
{languages}

Instructions:
- Expand the Professional Summary into 3–4 strong sentences highlighting strengths, years of experience, and specialization.
- For each company, generate 3 impactful bullet points describing key achievements and contributions.
- Organize Skills into clear neat bullet points (grouped if possible into technical and soft skills).
- Strengthen the Achievements section to sound result-driven and impressive.
- Format Languages section neatly.
- Format the full resume cleanly with proper section breaks.
- Do NOT mention these instructions in the final resume.
- Write in English language.
"""

    # Step 4: Call OpenAI to generate the resume
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional resume writer."},
            {"role": "user", "content": user_data}
        ],
        temperature=0.7,
        max_tokens=2000
    )

    generated_resume = response['choices'][0]['message']['content']

    # Step 5: Return the generated resume
    return jsonify({"resume": generated_resume})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

