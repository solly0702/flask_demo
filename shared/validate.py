import re

def validate(form):
    errors = {}
    if " " in form('username') or not(3 < len(form('username')) < 20):
        errors['username'] = "Username must be more than 3 and less than 20 letters withouth containing space"
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", form('email')):
        errors['email'] = "Email format is invalid"
    if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', form('password')):
        errors['password'] = "Password must be 8 length long with containing at least one capital letter and number"
    if form('password') != form('password_cf'):
        errors['password_cf'] = "Password doesn't match"
    if form('term') != "on":
        errors['term'] = "Term mush be checked"

    if bool(errors) == True:
        errors['isValid'] = False
    else:
        errors['isValid'] = True

    return errors
