import re

def text_match(text):
    regex = re.compile(r'AB{2,3}')
    mo = regex.search(text)
    if mo == None:
        return 'Not matched'
    else:
        return 'Matched'

print(text_match("A"))
print(text_match("ABC"))
print(text_match("ABBC"))