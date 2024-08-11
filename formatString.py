custom_string = 'X-MAPDS-Confidence:0.8475'
splitString = custom_string.split(':')
for element in splitString:
    try:
        number = float(element)
        print(number)
    except ValueError:
        continue