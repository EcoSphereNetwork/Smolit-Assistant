import openai
from config import settings
from app.utils import handle_error
import logging

openai.api_key = settings.openai_api_key

def query_openai(prompt, model="gpt-4"):
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error in OpenAI agent: {str(e)}")
        return handle_error(e)
