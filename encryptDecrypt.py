alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

message = input("Enter your message:\n").upper()
shift_number = int(input("Enter the shift number:\n"))

def refactor(position, cryptType):
    if cryptType == 'encrypt':
        return (position - 26)
    elif cryptType == 'decrypt':
        return (position + 26)

def crypt(message, shift_number):
    msg = ""
    for char in message:
        if char in alphabet:
            pos = alphabet.index(char)
            cryptPos = pos + shift_number
            if cryptPos > 25:
                refactor(cryptPos, 'encrypt')
            elif cryptPos < 0:
                refactor(cryptPos, 'decrypt')
            msg += alphabet[cryptPos]
        else:
            msg += char
    return msg

selection = input("Is this message for encryption (e), or decryption (d)? ")
if selection == 'e':
    encryptMsg = crypt(message, shift_number)
    print(encryptMsg)
else:
    decryptMsg = crypt(message, shift_number)
    print(decryptMsg)