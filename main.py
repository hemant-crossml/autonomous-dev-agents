"""
main.py
-------
Non-interactive example demonstrations without context memory.
Each example runs independently with comprehensive logging for debugging.
"""

import traceback

from langchain_core.messages import HumanMessage

from agent import agent
from prompt import system_prompt, example_1_query, example_2_query, example_3_query
from logger_config import setup_logger

# Initialize logger for main module
logger = setup_logger(__name__)


# Define example queries


# Message structures (no context memory - each is independent)
message1 = {
    "messages": [
        system_prompt,
        example_1_query
    ]
}

message2 = {
    "messages": [
        system_prompt,
        example_2_query
    ]
}

message3 = {
    "messages": [
        system_prompt,
        example_3_query
    ]
}


if __name__ == "__main__":
    logger.info("="*70)
    logger.info("APPLICATION STARTED - NON-INTERACTIVE MODE")
    logger.info("="*70)
    
    # ==================== Example 1: Web Search ====================
    try:
        logger.info("\n[EXAMPLE 1] Starting web search example")
        logger.info(f"[EXAMPLE 1] User query: {example_1_query.content}")
        
        print("\n" + "="*70)
        print("EXAMPLE 1: Web Search for Python Best Practices")
        print("="*70)
        print(f"\nQuery: {example_1_query.content}\n")
        print("Processing...\n")
        
        response1 = agent.invoke(message1)
        
        logger.info(f"[EXAMPLE 1] Agent invocation completed successfully")
        logger.debug(f"[EXAMPLE 1] Response messages count: {len(response1['messages'])}")
        logger.debug(f"[EXAMPLE 1] Final message type: {type(response1['messages'][-1])}")
        
        print("Response:")
        print("-" * 70)
        print(response1["messages"][-1].content)
        print("-" * 70)
        
        logger.info(f"[EXAMPLE 1] Output displayed to user")
        
    except KeyError as e:
        logger.error(f"[EXAMPLE 1] KeyError - missing expected key in response: {e}", exc_info=True)
        print(f"\n--- Example 1 FAILED ---")
        print(f"Error: Missing expected data in response - {e}")
        
    except Exception as e:
        logger.error(f"[EXAMPLE 1] Unexpected error occurred: {e}", exc_info=True)
        logger.debug(f"[EXAMPLE 1] Full traceback:\n{traceback.format_exc()}")
        print(f"\n--- Example 1 FAILED ---")
        print(f"Error: {e}")
    
    # ==================== Example 2: Test Case Generation ====================
    try:
        logger.info("\n[EXAMPLE 2] Starting test case generation example")
        logger.info(f"[EXAMPLE 2] User query: {example_2_query.content[:100]}...")
        
        print("\n" + "="*70)
        print("EXAMPLE 2: Generate Pytest Test Cases")
        print("="*70)
        print(f"\nQuery: Generate tests for calculate_discount function\n")
        print("Processing...\n")

        response2 = agent.invoke(message2)
        
        logger.info(f"[EXAMPLE 2] Agent invocation completed successfully")
        logger.debug(f"[EXAMPLE 2] Response messages count: {len(response2['messages'])}")
        
        print("Response:")
        print("-" * 70)
        print(response2["messages"][-1].content)
        print("-" * 70)
        
        logger.info(f"[EXAMPLE 2] Output displayed to user")
        
    except KeyError as e:
        logger.error(f"[EXAMPLE 2] KeyError - missing expected key in response: {e}", exc_info=True)
        print(f"\n--- Example 2 FAILED ---")
        print(f"Error: Missing expected data in response - {e}")
        
    except Exception as e:
        logger.error(f"[EXAMPLE 2] Unexpected error occurred: {e}", exc_info=True)
        logger.debug(f"[EXAMPLE 2] Full traceback:\n{traceback.format_exc()}")
        print(f"\n--- Example 2 FAILED ---")
        print(f"Error: {e}")
    
    # ==================== Example 3: Terminal Command Execution ====================
    try:
        logger.info("\n[EXAMPLE 3] Starting terminal command example")
        logger.info(f"[EXAMPLE 3] User query: {example_3_query.content}")
        
        print("\n" + "="*70)
        print("EXAMPLE 3: Execute Terminal Commands")
        print("="*70)
        print(f"\nQuery: {example_3_query.content}\n")
        print("Processing...\n")
        
        response3 = agent.invoke(message3)
        
        logger.info(f"[EXAMPLE 3] Agent invocation completed successfully")
        logger.debug(f"[EXAMPLE 3] Response messages count: {len(response3['messages'])}")
        
        print("Response:")
        print("-" * 70)
        print(response3["messages"][-1].content)
        print("-" * 70)
        
        logger.info(f"[EXAMPLE 3] Output displayed to user")
        
    except KeyError as e:
        logger.error(f"[EXAMPLE 3] KeyError - missing expected key in response: {e}", exc_info=True)
        print(f"\n--- Example 3 FAILED ---")
        print(f"Error: Missing expected data in response - {e}")
        
    except Exception as e:
        logger.error(f"[EXAMPLE 3] Unexpected error occurred: {e}", exc_info=True)
        logger.debug(f"[EXAMPLE 3] Full traceback:\n{traceback.format_exc()}")
        print(f"\n--- Example 3 FAILED ---")
        print(f"Error: {e}")
    
    logger.info("="*70)
    logger.info("ALL EXAMPLES COMPLETED")
    logger.info("="*70)
    
    print("\n" + "="*70)
    print("✅ ALL EXAMPLES COMPLETED")
    print("="*70 + "\n")