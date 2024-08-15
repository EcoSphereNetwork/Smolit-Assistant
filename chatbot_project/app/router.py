from app.nlu import analyze_input
from app.agents.localai_agent import query_localai
from app.agents.openai_agent import query_openai
from app.agents.autogpt_agent import query_autogpt
from app.agents.shellgpt_agent import execute_shell_command
from app.utils import log_user_interaction, handle_error
import logging

def route_input(user_input):
    try:
        analysis = analyze_input(user_input)
        intent = analysis['intent']
        entities = analysis['entities']
        sentiment = analysis['sentiment']
        is_command = analysis['is_command']

        if is_command:
            response = execute_shell_command(user_input)
        elif intent == "action" and "COMMAND" in [label for _, label in entities]:
            response = query_autogpt(user_input)
        elif intent == "question":
            response = query_openai(user_input)
        elif sentiment < 0:
            response = query_autogpt(user_input)
        else:
            response = query_localai(user_input)

        log_user_interaction(user_input, response)
        return response
    
    except Exception as e:
        logging.error(f"Error in routing logic: {str(e)}")
        return handle_error(e)
