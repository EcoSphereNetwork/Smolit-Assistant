import logging
from .localai_agent import query_localai
from .openai_agent import query_openai
from .async_agents import async_query_localai, async_query_openai
from .shellgpt_agent import execute_shell_command

logging.getLogger(__name__).info("Agents module initialized.")
