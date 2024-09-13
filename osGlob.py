import glob

def displayPy():
    pyFiles = glob.glob('*.py')
    print(pyFiles)
    
def displayOsFiles():
    pyFiles = glob.glob('os*')
    print(pyFiles)

def displayPyFiles():
    pyFiles = glob.iglob('*.py', recursive=True)
    for file in pyFiles:
        print(file)

displayPy()
displayOsFiles()
displayPyFiles()