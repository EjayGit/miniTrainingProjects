import re

def start_ae(text):
    regex = re.compile(r'[ae]\w+')
    mo = regex.findall(text)
    return mo
    
text = "The following example creates a list with 50 elements. All elements are then added to the list when the list is created."
start_ae(text)