def safe_lower(text):
    return text.lower() if isinstance(text, str) else text