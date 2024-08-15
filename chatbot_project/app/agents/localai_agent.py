import requests
from config import settings
from app.utils import handle_error
import logging

def query_localai(prompt):
    try:
        response = requests.post(settings.localai_api_endpoint, json={"prompt": prompt})
        if response.status_code == 200:
            return response.json().get('response', "No response from LocalAI")
        else:
            logging.error(f"Error contacting LocalAI: {response.status_code} - {response.text}")
            return f"Error contacting LocalAI: {response.status_code}"
    except Exception as e:
        logging.error(f"Error in LocalAI agent: {str(e)}")
        return handle_error(e)
