import re

def extract_email(text):
    regex = re.compile(r'\S+@\S+')
    mo = regex.findall(text)
    if mo != None:
        return mo

text = """From test@appmillers.com Wen Jan  5 09:14:16 2022\nFrom info@appmillers.com Wen Jan  5 09:14:16 2022\nFrom elshad@appmillers.com Wen Jan  5 \nFrom redy@appmillers.com Wen Jan  5 \nFrom info@appmillers.com Wen Jan  5 """

extract_email(text)