import openai
from config import OPENAI_API_KEY, OPENAI_BASE_URL, GPT_MODEL

client = openai.OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL
)

def generate_ai_reply(subject, body):
    """
    Generate GPT-powered reply for an email
    """
    prompt = f"Write a polite, professional reply to this email.\n\nSubject: {subject}\nBody: {body}\n\nReply:"
    
    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    
    return response.choices[0].message.content
