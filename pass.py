import re

password = input("enter your password:")
def psw(password):
    while True:
        if len(password) < 8:
            return "weak:password must be grater than or equal to 8 characters"
        if not re.search(r'[a-z]', password):
            return "weak:password must contain atleast one lowcase characters"
        if not re.search(r'[A-Z]', password):
            return "weak:password must contain atleast one upparcase characters"
        if not re.search(r'\d', password):
            return "weak:password must contain atleast one number character"
        if not re.search(r"[!@#$%^&*()_+=;<>/]", password):
            return "weak:password must contain atleast one special character"
        break

psw(password)
strength=psw(password)
print(strength)
