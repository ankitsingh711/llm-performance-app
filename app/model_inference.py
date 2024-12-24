import requests
from app.config import LLM_API_KEY, LLM_MODEL_URL

def query_llm(user_query: str) -> dict:
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "prompt": user_query,
        "max_tokens": 500
    }

    response = requests.post(LLM_MODEL_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        # Simulating the expected LLM response
        # In reality, you would need to parse the response accordingly
        return response.json()  
    else:
        raise Exception(f"LLM API Error: {response.status_code} - {response.text}")
