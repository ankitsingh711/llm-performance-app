from datetime import datetime, timedelta

def parse_date(date_str: str) -> str:
    if date_str == 'default':
        # Return default dates
        return datetime.today().strftime('%Y-%m-%d')
    
    try:
        # Try parsing as ISO format date
        return datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        pass
    
    # Handle relative dates like "last year", "last quarter"
    if date_str == "last year":
        return (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
    elif date_str == "last quarter":
        return (datetime.today() - timedelta(days=90)).strftime('%Y-%m-%d')
    elif date_str == "this quarter":
        return (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    # Default to today
    return datetime.today().strftime('%Y-%m-%d')
