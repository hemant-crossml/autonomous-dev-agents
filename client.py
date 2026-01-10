"""
LLM and External API Client Initialization Module

Summary:
This module initializes and configures external service clients required
by the application, including the Gemini chat model and the SerpAPI client.

Description:
- Creates a ChatGoogleGenerativeAI instance using the Gemini 2.5 Flash Lite
  model with controlled generation parameters for deterministic responses.
- Initializes a SerpAPI client for performing web search operations.
- Uses centralized logging to track successful initialization and capture
  detailed error information during failures.
- Ensures failures are surfaced by re-raising exceptions after logging.

All API credentials are securely loaded from the `cred` module.
"""
import serpapi
from langchain_google_genai import ChatGoogleGenerativeAI


from cred import gemini_api_key, serpapi_api_key
from logger_config import setup_logger

# Initialize logger for this module
logger = setup_logger(__name__)

logger.info("Initializing Gemini chat model client")

try:
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        api_key=gemini_api_key,
        temperature=0.2,
        top_p=0.9,
        top_k=40,
        max_output_tokens=512,   # output length cap
    )
    logger.info("Gemini model initialized successfully")
    logger.debug(f"Model config: model=gemini-2.5-flash-lite, temp=0.2, top_p=0.9, top_k=40, max_tokens=512")
except Exception as e:
    logger.error(f"Failed to initialize Gemini model: {str(e)}", exc_info=True)
    raise

# Initialize SerpAPI client
logger.info("Initializing Serp api client")
try:
    client = serpapi.Client(api_key=serpapi_api_key)
    logger.info("Serp api client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialized Gemini model :{str(e)}",exc_info=True)
    raise

