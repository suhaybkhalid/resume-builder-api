import openai
from docx import Document

# Set up OpenAI API key
openai.api_key = "OPENAI_API_KEY"  # Replace with your actual API key

def generate_resume_text(user_resume_input):
    prompt = f"""
    Format the following user input into a professional, one-page resume:

    Name: {user_resume_input.get('name', ' ')}
    Email: {user_resume_input.get('email', ' ')}
    Phone: {user_resume_input.get('phone', ' ')}
    Address: {user_resume_input.get('address', ' ')}

    Summary (strict to 3 lines max): {user_resume_input.get('summary', ' ')}

    Experience:
    {user_resume_input.get('experience', ' ')}

    Education:
    {user_resume_input.get('education', ' ')}

    Skills (limit to 7-12 skills): {user_resume_input.get('skills', ' ')}

    Achievements (limit to 3 bullet points): {user_resume_input.get('achievements', ' ')}

    Languages: {user_resume_input.get('languages', ' ')}

    Ensure each job has a maximum of 3 bullet points for description.
    Keep the resume concise, structured, and formatted professionally.
    """

    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

def save_resume_to_docx(resume_text, filename="resume.docx"):
    doc = Document()
    for line in resume_text.split("\n"):
        doc.add_paragraph(line.strip())
    doc.save(filename)

# Example user input dictionary (Replace with actual input from Google Form)
user_resume_input = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1 234 567 890",
    "address": "New York, NY",
    "summary": "Experienced Project Manager with expertise in Agile methodologies and process optimization.",
    "experience": """
    Project Manager, Tech Corp (2020-2023)
    - Led cross-functional teams to deliver software solutions.
    - Managed Agile workflows to increase efficiency by 20%.
    - Oversaw $2M budget projects successfully.

    Business Analyst, Innovate Ltd. (2017)
    - Analyzed business data to improve operational efficiency.
    - Developed new strategies, reducing costs by 15%.
    - Implemented automation tools, increasing productivity.
    """,
    "education": """
    Master of Business Administration (MBA), Harvard University, 2015
    Bachelor of Science in Computer Science, Stanford University, 2012
    """,
    "skills": "Project Management, Agile, Data Analysis, SQL, Communication, Leadership, Risk Management",
    "achievements": """
    - Implemented ERP system, cutting costs by 15%.
    - Spearheaded Agile transformation, reducing project timelines.
    - Led a team of 10+ members to complete high-impact projects.
    """,
    "languages": "English, Spanish"
}

# Generate and save resume
formatted_resume_text = generate_resume_text(user_resume_input)
save_resume_to_docx(formatted_resume_text)
print("Resume saved successfully as resume.docx")


