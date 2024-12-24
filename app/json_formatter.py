def format_to_json(companies, parameters, start_date, end_date):
    data = []
    
    for company in companies:
        for param in parameters:
            entry = {
                "company_name": company,
                "metric": param,
                "start_date": start_date,
                "end_date": end_date
            }
            data.append(entry)
    
    return data
