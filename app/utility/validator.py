import re


def validate_name(name):

    if len(name) == 0:
        return False
    # if name == "":
    #     return False
    for char in name:
        if char == " ":
            return False
        elif not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
            return False
    return True


def validate_id(id):
    return True


def validate_phone_number(phone_number):
    return True
