import re

def check_char(text):
    regex = re.compile(r'[a-zA-Z0-9]')
    mo = regex.findall(text)
    return mo

print(check_char("ABCDEFabef1250"))
print(check_char("*&%@#{"))