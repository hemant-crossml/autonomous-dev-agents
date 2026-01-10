import subprocess
from typing import List, Union

from langchain_core.tools import tool

from client import client
from logger_config import setup_logger


@tool
def execute_terminal_command(commands: Union[str, List[str]]) -> str:
    """
    Executes Linux terminal commands safely and returns the output.
    
    Args:
        commands: A single command string or list of command strings to execute
        
    Returns:
        The stdout/stderr output from command execution
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
    Searches the web using SerpAPI and returns relevant results.
    
    Args:
        query: The search query string
        num_results: Number of results to return (default: 5)
        
    Returns:
        A formatted string containing search results with titles, links, and snippets
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
    """Generate Python test cases for a given function.
    
    Args:
        function_code: The Python function code to generate tests for
        test_framework: Testing framework to use (pytest, unittest)
        num_test_cases: Number of test cases to generate
        
    Returns:
        Generated test cases as a formatted string
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