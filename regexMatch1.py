import re

def text_match(text):
    regex = re.compile(r'AB*')
    mo = regex.search(text)
    if mo == None:
        return 'Not matched'
    else:
        return 'Matched'

text_match("A")
text_match("ABC")
text_match("ABBC")