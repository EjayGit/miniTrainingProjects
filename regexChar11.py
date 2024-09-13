import re

def remove_zero(text):
    resultString = re.sub(r'\.0*', '.',text)
    return resultString

remove_zero("211.07.095.122")