def get_top_states_query():
    return """
        SELECT state, SUM(amount) AS total_amount 
        FROM aggregated_transaction 
        GROUP BY state 
        ORDER BY total_amount DESC 
        LIMIT 10
    """

def get_yearwise_trend_query():
    return """
        SELECT year, SUM(amount) AS total_amount 
        FROM aggregated_transaction 
        GROUP BY year
    """

def get_transaction_types_query():
    return """
        SELECT transaction_type, SUM(amount) AS total_amount 
        FROM aggregated_transaction 
        GROUP BY transaction_type 
        ORDER BY total_amount DESC
    """

def get_quarterly_growth_query():
    return """
        SELECT year, quarter, SUM(amount) AS total_amount 
        FROM aggregated_transaction 
        GROUP BY year, quarter 
        ORDER BY year, quarter
    """