import google.generativeai as genai

API_KEY = "AIzaSy..."

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_ai_review(code):

    prompt = f"""
You are a professional senior software engineer.

Review the following Python code and provide:

1. Code quality assessment
2. Potential issues
3. Best practice suggestions
4. Readability improvements
5. Final verdict

Python Code:

{code}
"""

    response = model.generate_content(prompt)

    return response.text