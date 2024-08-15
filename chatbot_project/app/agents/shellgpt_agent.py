import subprocess
from app.utils import handle_error
import logging

ALLOWED_COMMANDS = ["ls", "pwd", "whoami", "echo", "date"]

def execute_shell_command(command):
    try:
        command_name = command.split()[0]
        if command_name not in ALLOWED_COMMANDS:
            logging.warning(f"Attempt to execute disallowed command: {command_name}")
            return f"Error: Command '{command_name}' is not allowed."

        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            logging.info(f"Command executed successfully: {command}")
            return result.stdout.strip()
        else:
            logging.error(f"Command execution failed: {command} - {result.stderr.strip()}")
            return f"Error: {result.stderr.strip()}"
    except Exception as e:
        logging.error(f"Error in Shell-GPT agent: {str(e)}")
        return handle_error(e)
