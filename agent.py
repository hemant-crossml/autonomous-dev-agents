from langchain.agents import create_agent

from client import model
from tools import execute_terminal_command,web_search_tool,generate_test_cases
from logger_config import setup_logger

logger = setup_logger(__name__)

logger.info("Initializing LangChain agent")

tools =[execute_terminal_command,web_search_tool,generate_test_cases]
logger.info("Initializing LangChain agent")

try:
    agent = create_agent(model=model, tools=tools)
    logger.info("Agent created successfully")
except Exception as e:
    logger.error(f"Failed to create agent: {str(e)}", exc_info=True)
    raise