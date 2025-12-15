def mask_email(email: str) -> str:
    local_part, domain = email.split("@")
    masked_local = f"{local_part[0]}{'*' * (len(local_part)-2)}{local_part[-1]}"
    return f"{masked_local}@{domain}"
