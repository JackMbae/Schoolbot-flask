# school_bot.py

import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

faq_responses = {
    "admission": "You can apply for admission through our school website or visit the admissions office.",
    "fees": "The school fees for each term are posted on the noticeboard and school portal.",
    "uniform": "The school uniform includes a navy blue skirt or trousers, white shirt, and a blue tie.",
    "timetable": "The class timetable is available in the school portal or from your class teacher.",
    "clubs": "We offer clubs like Drama, Science, Debate, Coding, and Football. Join one that interests you!"
}

def get_school_response(user_input):
    user_input = user_input.lower()
    for keyword, response in faq_responses.items():
        if keyword in user_input:
            return response
    return ask_gpt(user_input)

def ask_gpt(prompt):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "meta-llama/llama-3.3-8b-instruct:free",  # or another free model
            "messages": [
                {"role": "system", "content": "You are a helpful school assistant who answers student questions."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raises error for 4xx/5xx
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("OpenRouter error:", e)
        return "Sorry, I couldn't get a response from the AI service right now."
