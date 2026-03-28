def normalize_token(raw_token):
    if raw_token.startswith("Bearer "):
        return raw_token
    return f"Bearer {raw_token}"