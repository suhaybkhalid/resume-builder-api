from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["POST"])
def generate_resume():
    try:
        request_data = request.get_json()

        # Extract all fields safely
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

        # 🚫 Prevent calling OpenAI if key data is missing
        required_fields = [full_name, current_job_title, email, summary]
        if not all(required_fields):
            print("❌ Missing required fields. Skipping OpenAI call.")
            return jsonify({"error": "Missing required fields"}), 400

        print("📨 Sending resume request to OpenAI...")

        # Create the strong prompt
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
- Expand the Professional Summary into 3–4 strong sentences.
- For each company, generate 3 impactful bullet points describing key achievements and contributions.
- Organize Skills into clear neat bullet points (grouped if possible into technical and soft skills).
- Strengthen the Achievements section to sound result-driven and impressive.
- Format the Languages properly.
- Format the full resume cleanly with proper section breaks.
- Write in professional English language.
- Do NOT include these instructions in the output.
"""

        # 🔥 Call OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional resume writer."},
                {"role": "user", "content": user_data}
            ],
            temperature=0.7,
            max_tokens=2000
        )

        print("✅ OpenAI responded successfully.")

        generated_resume = response['choices'][0]['message']['content']
        return jsonify({"resume": generated_resume}), 200

    except Exception as e:
        print(f"🔥 ERROR: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def index():
    return "Resume Builder API is running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
