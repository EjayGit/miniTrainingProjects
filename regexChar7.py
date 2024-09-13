import re

def text_match(text):
    regex = re.compile(r'[c|C]\w+[e|E]')
    mo = regex.findall(text)
    if mo != None:
        return mo

text = 'I come to CTRE every year'
text_match(text)