import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# API key and model URL (replace with your actual LLM API key and endpoint)
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL_URL = "https://api.groq.com/v1/llama-3.1-8b-instant"

# Default date range (1 year ago to today)
DEFAULT_START_DATE = "2023-12-24"  # Placeholder; you'll dynamically compute this
DEFAULT_END_DATE = "2024-12-24"    # Placeholder; you'll dynamically compute this
