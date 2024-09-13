from pathlib import Path

path_test = Path.cwd() / 'archive' / 'test.txt'
print(f'File name: {path_test.name}')
print(f'File directory: {path_test.parent}')
print(f'Parent File directory: {path_test.parent.parent}')
print(f'File name without extension: {path_test.stem}')
print(f'File extension: {path_test.suffix}')

def displayDirContent():
    entries = Path.cwd()
    for entry in entries.iterdir():
        print(f'File name: {entry.name}')
        print(f'File folder: {entry.parent}')
        print(f'File name w/o ex: {entry.stem}')
        print(f'File ex: {entry.suffix}')
        print()

displayDirContent()

path = Path.cwd()
fileNames = path.glob('*.py')
for fileName in fileNames:
    print(fileName.stem)

dirPath = Path("archive/")
dirPath.mkdir()