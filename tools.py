"""
tools.py

This module defines LangChain-compatible tools that enable an AI agent
to execute terminal commands, perform web searches, and generate Python
test cases.

Description:
- Provides a safe interface for executing Linux terminal commands without
  using shell execution.
- Integrates SerpAPI to support real-time web search and technical research.
- Includes a test case generation utility for creating structured and
  comprehensive Python test prompts.
- All functions are exposed as LangChain tools using the `@tool` decorator.

This module contains only tool definitions and is intended to be imported
by the agent initialization layer.
"""

import subprocess
from typing import List, Union

from langchain_core.tools import tool

from client import client
from logger_config import setup_logger


@tool
def execute_terminal_command(commands: Union[str, List[str]]) -> str:
    """
    Summary:
        Safely executes one or more Linux terminal commands and returns their output.

    Args:
        commands (Union[str, List[str]]): A single command string or a list of
        command strings to be executed sequentially.

    Returns:
        str: Combined stdout and stderr output for all executed commands,
        including command context.
    """

    if isinstance(commands, str):
        commands = [commands]
    
    results = []
    for cmd in commands:
        try:
            # Use list format and avoid shell=True for security
            result = subprocess.run(
                cmd.split(),  # Split command into list
                capture_output=True,
                text=True,
                timeout=30
            )
            output = result.stdout if result.stdout else result.stderr
            results.append(f"Command: {cmd}\nOutput: {output}")
        except Exception as e:
            results.append(f"Command: {cmd}\nError: {str(e)}")
    
    return "\n\n".join(results)

@tool
def web_search_tool(query: str, num_results: int = 5) -> str:
    """
    Summary:
        Performs a web search using SerpAPI and returns formatted search results.

    Args:
        query (str): Search query optimized for technical or informational content.
        num_results (int): Number of search results to return (default is 5).

    Returns:
        str: A formatted string containing titles, URLs, and descriptions
        of the search results.
    """
    try:
        # Perform search
        results = client.search({
            'engine': 'google',
            'q': query,
            'num': num_results,
            'hl': 'en',
            'gl': 'us'
        })
        
        # Extract and format organic results
        if 'organic_results' not in results:
            return "No results found."
        
        formatted_results = []
        for idx, result in enumerate(results['organic_results'][:num_results], 1):
            title = result.get('title', 'No title')
            link = result.get('link', 'No link')
            snippet = result.get('snippet', 'No description available')
            
            formatted_results.append(
                f"{idx}. {title}\n"
                f"   URL: {link}\n"
                f"   Description: {snippet}\n"
            )
        
        return "\n".join(formatted_results)
        
    except Exception as e:
        return f"Search error: {str(e)}"
    

@tool
def generate_test_cases(
    function_code: str,
    test_framework: str = "pytest",
    num_test_cases: int = 3
) -> str:
    """
    Summary:
        Generates structured Python test cases for a given function or class.

    Args:
        function_code (str): Complete Python function or class code to be tested.
        test_framework (str): Testing framework to use (pytest or unittest).
        num_test_cases (int): Number of test cases to generate.

    Returns:
        str: A formatted string containing generated, runnable test code.
    """

    prompt = f"""
    Generate {num_test_cases} comprehensive test cases for the following Python function
    using {test_framework} framework:
    
    {function_code}
    
    Include:
    - Positive test cases (normal inputs)
    - Edge cases (boundary values)
    - Negative test cases (invalid inputs)
    
    Format the output as complete, runnable test code.
    """
    
    # This would connect to your LLM
    # For now, returning the prompt structure
    return prompt