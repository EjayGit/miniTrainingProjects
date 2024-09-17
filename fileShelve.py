import shelve

dictKey = input('Enter a key: ')
with shelve.open('shelveFile') as shFile:
    shFile['miller'] = 'a person who owns or works in a corn mill'
    shFile['programmer'] = 'a person who writes computer programs'
    shFile['app'] = 'an application'
    print(shFile.get(dictKey, 'The key does not exist'))
