import re

def is_decimal(text):
    regex = re.compile(r'^\d+\.\d{1,2}$')
    mo = regex.search(text)
    if mo != None:
        return True
    else:
        return False

is_decimal('123.11')
is_decimal('123.1')
is_decimal('123.123')