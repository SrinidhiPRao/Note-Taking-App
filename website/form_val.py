from re import search

def check_email(mail):
    if search(r"^.+@.+\..+", mail):
        return True
    return False

def check_name(name):
    if search(r"[a-zA-Z+]", name):
        return True
    return False

def check_password(password1, password2):
    
    if password1 == password2 and len(password1) >= 8:
        return True
    return False

