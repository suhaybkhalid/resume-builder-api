# 🚨 INSTRUCTION: Do not change working logic unless explicitly told.
# ✅ Fix only text formatting for Google Docs placeholders.
# ❌ Do not modify prompt, structure, or OpenAI logic unless asked.

from flask import Flask, request, jsonify
import openai
import os
import json

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

def format_bullets(items, symbol=''):
    if isinstance(items, list):
        return '\n'.join([f"{symbol} {item}" for item in items])
    return items  # fallback if OpenAI returns plain text

@app.route("/", methods=["POST"])
def generate_resume():
    try:
        request_data = request.get_json()

        # Extract user inputs (do not change)
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
        first_university_name = request_data.get('1st_university_name', '')
        first_university_location = request_data.get('1st_university_location', '')
        second_university_major = request_data.get('2nd_university_major', '')
        second_university_name = request_data.get('2nd_university_name', '')
        second_university_location = request_data.get('2nd_university_location', '')
        skills = request_data.get('skills', '')
        achievements = request_data.get('achievements', '')
        languages = request_data.get('languages', '')

        print("📨 Sending request to OpenAI...")

        # Use same working prompt from before — do not modify
        user_data = f"""
You are an expert resume writer.

Your job:
- Rewrite and improve weak fields (Summary, Job Descriptions, Skills, Achievements, Languages).
- Keep factual fields unchanged (Full Name, Address, Phone, Email, University names, Job Titles, Dates).

Return only a clean JSON object with these exact fields:

- full_name
- current_job_title
- address
- phone_number
- email
- summary
- current_company_name
- current_job_start_date
- current_job_description
- previous_company_name
- previous_job_title
- previous_job_start_date
- previous_job_end_date
- previous_job_description
- old_company_name
- old_job_title
- old_job_start_date
- old_job_end_date
- old_job_description
- 1st_university_major
- 1st_university_name
- 1st_university_location
- 2nd_university_major
- 2nd_university_name
- 2nd_university_location
- skills
- achievements
- languages

User Information:

Full Name: {full_name}
Current Job Title: {current_job_title}
Address: {address}
Phone Number: {phone_number}
Email: {email}
Summary: {summary}
Current Company:
- Name: {current_company_name}
- Start Date: {current_job_start_date}
- Description: {current_job_description}
Previous Company:
- Name: {previous_company_name}
- Job Title: {previous_job_title}
- Start Date: {previous_job_start_date}
- End Date: {previous_job_end_date}
- Description: {previous_job_description}
Older Company:
- Name: {old_company_name}
- Job Title: {old_job_title}
- Start Date: {old_job_start_date}
- End Date: {old_job_end_date}
- Description: {old_job_description}
Education:
- {first_university_major} at {first_university_name} ({first_university_location})
- {second_university_major} at {second_university_name} ({second_university_location})
Skills: {skills}
Achievements: {achievements}
Languages: {languages}

VERY IMPORTANT:
- For **Summary**, write a strong 3-line professional summary.
- For **each Job Description** (current, previous, old), create **2 to 3 strong bullet points**, NOT a single line.
- For **Skills**, generate clean bullet points (one per line).
- For **Achievements**, rephrase to sound executive-level and result-driven.
- For **Languages**, list separately and clearly.

Example for Job Description:
[
"Bullet 1",
"Bullet 2",
"Bullet 3"
]

Example for Skills:
[
"Skill 1",
"Skill 2",
"Skill 3"
]
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional resume writer."},
                {"role": "user", "content": user_data}
            ],
            temperature=0.5,
            max_tokens=2000,
            request_timeout=60
        )

        print("✅ OpenAI responded successfully.")
        ai_response = json.loads(response['choices'][0]['message']['content'])

        # Only formatting text output for Google Docs placeholders (DO NOT CHANGE INPUT/PROMPT)
        result = {
            "full_name": full_name,
            "current_job_title": current_job_title,
            "address": address,
            "phone_number": phone_number,
            "email": email,
            "summary": ai_response.get("summary", ""),
            "current_company_name": current_company_name,
            "current_job_start_date": current_job_start_date,
            "current_job_description": format_bullets(ai_response.get("current_job_description", [])),
            "previous_company_name": previous_company_name,
            "previous_job_title": previous_job_title,
            "previous_job_start_date": previous_job_start_date,
            "previous_job_end_date": previous_job_end_date,
            "previous_job_description": format_bullets(ai_response.get("previous_job_description", [])),
            "old_company_name": old_company_name,
            "old_job_title": old_job_title,
            "old_job_start_date": old_job_start_date,
            "old_job_end_date": old_job_end_date,
            "old_job_description": format_bullets(ai_response.get("old_job_description", [])),
            "1st_university_major": first_university_major,
            "1st_university_name": first_university_name,
            "1st_university_location": first_university_location,
            "2nd_university_major": second_university_major,
            "2nd_university_name": second_university_name,
            "2nd_university_location": second_university_location,
            "skills": format_bullets(ai_response.get("skills", [])),
            "achievements": ai_response.get("achievements", ""),
            "languages": format_bullets(ai_response.get("languages", []), symbol="")
        }

        return jsonify(result), 200

    except Exception as e:
        print(f"🔥 ERROR: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def index():
    return "Resume Builder API is running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
