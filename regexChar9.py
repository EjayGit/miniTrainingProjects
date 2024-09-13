import re 

def find_words(text):
    regex = re.compile(r'\b\w{3,5}\b')
    mo = regex.findall(text)
    if mo != None:
        return mo

find_words("I like Python for Everyone course. It is the best one out there.")