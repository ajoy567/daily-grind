def is_valid_email(email: str) -> tuple[bool, str]:
    """
    Validate an email address.
    
    there is exactly one @
    the part after the @ (the domain) contains a dot
    there are no spaces anywhere

    Args:
        email (str): The email address to validate.

    Returns:
        tuple[bool, str]: A tuple containing a boolean indicating if the email is valid and a string with the validation message.
    """
    
    if email.count('@') != 1:
        return False, "Email must contain exactly one '@' symbol."

    local_part, domain = email.split('@')

    if ' ' in email:
        return False, "Email must not contain any spaces."


    if '.' not in domain:
        return False, "Domain must contain a dot."
    
    if not local_part:
        return False, "Nothing before the '@'."

    if domain.startswith('.'):
        return False, "Domain must not start with a dot."

    if domain.endswith('.'):
        return False, "Domain must not end with a dot."

    return True, "Email is valid."


test_emails = [
    'riya@gmail.com',
    'riya.gmail.com',
    'riya@@gmail.com',
    'riya@gmail',
    'ri ya@gmail.com',
    '@gmail.com',
    'riya@.com',
    'riya@gmail.'
]

for email in test_emails:
    is_valid, message = is_valid_email(email)
    print(f"{email!r} -> {is_valid}, {message}")