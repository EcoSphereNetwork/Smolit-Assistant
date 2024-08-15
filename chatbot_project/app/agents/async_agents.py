import httpx
from config import settings
from app.utils import handle_error
import logging

async def async_query_localai(prompt):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(settings.localai_api_endpoint, json={"prompt": prompt})
            if response.status_code == 200:
                return response.json().get('response', "No response from LocalAI")
            else:
                logging.error(f"Error contacting LocalAI: {response.status_code}")
                return f"Error contacting LocalAI: {response.status_code}"
    except Exception as e:
        logging.error(f"Error in async LocalAI agent: {str(e)}")
        return handle_error(e)

async def async_query_openai(prompt, model="gpt-4"):
    headers = {"Authorization": f"Bearer {settings.openai_api_key}"}
    data = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 150,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("https://api.openai.com/v1/completions", headers=headers, json=data)
            if response.status_code == 200:
                return response.json().get("choices", [{}])[0].get("text", "No response from OpenAI").strip()
            else:
                logging.error(f"Error contacting OpenAI: {response.status_code}")
                return f"Error contacting OpenAI: {response.status_code}"
    except Exception as e:
        logging.error(f"Error in async OpenAI agent: {str(e)}")
        return handle_error(e)
