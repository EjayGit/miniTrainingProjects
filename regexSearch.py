import re

def find_three_con(text):
    match = re.search('\d\d\d', text)
    if match != 'None':
        return match.group()
    else:
        return 'Not found'

text = 'My phone number is: 234-456-8765'
print(find_three_con(text))