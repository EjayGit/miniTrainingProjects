import re

def passwordChecker(password):
    isStrong = False
    while isStrong == False:
        isStrong = True
        # must be min 8 chars long
        if len(password) < 8:
            print("The password must be at least 8 characters long.")
            isStrong = False
        # must have one upper case
        regexUpper = re.compile(r'[A-Z]')
        if regexUpper.search(password) == None:
            print("The password must include an upper case letter.")
            isStrong = False
        # must have one lower case
        regexLower = re.compile(r'[a-z]')
        if regexLower.search(password) == None:
            print("The password must include a lower case letter.")
            isStrong = False
        # must have one digit
        regexDigit = re.compile(r'[0-9]')
        if regexDigit.search(password) == None:
            print("The password must include a digit.")
            isStrong = False
        # must have one special char
        regexSpecial = re.compile(r'[!"£$%^&*()|\\\{\}:;@\'#~,<.>]')
        if regexSpecial.search(password) == None:
            print("The password must include a special character.")
            isStrong = False
        if isStrong == True:
            return print('Strong password')
    

password = input("Input your password: ")
passwordChecker(password)