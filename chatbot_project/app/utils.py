import logging
import re
import redis
import json
from config import settings

# Configure logging
logging.basicConfig(filename=settings.log_file, level=settings.log_level, format='%(asctime)s - %(levelname)s - %(message)s')

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def log_user_interaction(user_input, response):
    try:
        interaction = {
            "user_input": user_input,
            "response": response
        }
        logging.info(json.dumps(interaction))
    except Exception as e:
        logging.error(f"Error logging interaction: {str(e)}")

def handle_error(e):
    error_message = f"An error occurred: {str(e)}"
    logging.error(error_message)
    return error_message

def validate_input(user_input):
    if re.search(r'[;&|><]', user_input):
        raise ValueError("Invalid input detected.")
    return user_input

def cache_response(key, value, ttl=settings.cache_ttl):
    try:
        redis_client.setex(key, ttl, value)
    except Exception as e:
        logging.error(f"Error caching response: {str(e)}")

def get_cached_response(key):
    try:
        return redis_client.get(key)
    except Exception as e:
        logging.error(f"Error retrieving cached response: {str(e)}")
        return None
