import re

# TODO 1: Create Parser class which has text attribute
class Parser:
    def __init__(self, text):
        self.text = text

    def email(self):
        regex = re.compile(r'\S+@\S+')
        mo = regex.search(self.text)
        return mo.group()

    def phone(self):
        regex = re.compile(r'(\d\d\d)?(-|\s)\d\d\d-\d\d\d\d')
        mo = regex.search(self.text)
        return mo.group()

class UKParser(Parser):
    def __init__(self, text):
        super().__init__(text=text)

    def phone(self):
        regex = re.compile(r'\(?\d{5}\)?(-|\s)?\d{6} ')
        mo = regex.search(self.text)
        return mo.group()
    
string1 = "Please contact us on 012-123-4567, or us@bigdomain.com"
parser1 = Parser(string1)
print(parser1.phone())
print(parser1.email())

string2 = "Please contact us on (01530) 473838, or us@bigdomain.co.uk"
parser2 = UKParser(string2)
print(parser2.phone())
print(parser2.email())