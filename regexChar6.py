import re

def text_match(text):
    regex = re.compile(r'^[A-Z]+_[A-Z]+$')
    mo = regex.search(text)
    if mo == None:
        return 'Not matched'
    else:
        return 'Matched'

text_match("BB_CCAA")
text_match("aabb_DDDEFF")
text_match("ADRGT_BCDEe")