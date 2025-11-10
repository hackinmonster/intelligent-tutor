def clean_date(date_str):
    """Return only the date (YYYY-MM-DD) from an ISO timestamp."""
    if not date_str:
        return None
    return date_str.split("T")[0]
