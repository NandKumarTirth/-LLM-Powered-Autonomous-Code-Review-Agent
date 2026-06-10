from llm_reviewer import get_ai_review

code = """
def hello():
    print("hello")
"""

review = get_ai_review(code)

print(review)