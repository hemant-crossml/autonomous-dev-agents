"""
LangChain Agent Initialization Module

Summary:
This module is responsible for initializing a LangChain agent using a
preconfigured language model and a set of custom tools.

Description:
- Imports a language model client.
- Registers tools for terminal command execution, web search, and
  automated Python test case generation.
- Sets up structured logging.
- Creates and validates a LangChain agent instance with proper
  error handling and logging for observability.

If agent creation fails, the error is logged with stack trace details
and re-raised to ensure failure visibility.
"""

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