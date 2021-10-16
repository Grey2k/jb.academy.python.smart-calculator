def check_email(string: str) -> bool:
    if " " in string:
        return False

    if "@" not in string:
        return False

    if "." not in string:
        return False

    if "@." in string:
        return False

    if string.rfind('.') < string.rfind('@'):
        return False

    return True
