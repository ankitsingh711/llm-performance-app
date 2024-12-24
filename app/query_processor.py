import json
from datetime import datetime
from app.date_handler import parse_date
from app.model_inference import query_llm
from app.json_formatter import format_to_json
from app.utils import log_error

def process_query(user_query: str):
    try:
        # Extract company name, metric, and dates using LLM
        llm_response = query_llm(user_query)
        
        # Extract data from the LLM response
        companies = llm_response.get('companies', [])
        parameters = llm_response.get('parameters', [])
        dates = llm_response.get('dates', {})
        
        # Handle missing dates by using defaults
        start_date = parse_date(dates.get('start', 'default'))
        end_date = parse_date(dates.get('end', 'default'))
        
        # Create structured data
        result_data = format_to_json(companies, parameters, start_date, end_date)
        
        return json.dumps(result_data, indent=4)
    
    except Exception as e:
        log_error(f"Error processing query: {str(e)}")
        return json.dumps({"error": str(e)}, indent=4)
