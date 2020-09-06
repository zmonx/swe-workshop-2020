import re


def validate_name(name):

    pattern = re.compile(r"[^\u0E00-\u0E7Fa-zA-Z' ]|^'|'$|''")
    if len(name) == 0:
        return False
    # if name == "":
    #     return False
    for char in name:
        if char == " ":
            return False
        elif not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ") or pattern):
            return False
    return True


def validate_id(id):
    return True


def validate_phone_number(phone_number):
    return True
