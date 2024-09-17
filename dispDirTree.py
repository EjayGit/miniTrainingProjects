import pathlib

def displayTree():
    directory = pathlib.Path.cwd()
    print(f"+ {directory}")
    entries = sorted(directory.glob("**/*")) # or .rglob("*")
    for entry in entries:
        depth = len(entry.relative_to(directory).parts)
        spacer = '   ' * depth
        print(f"{spacer}+ {entry.name}")

root = pathlib.Path.cwd()
childPath = pathlib.Path("C:/Users/user/Documents/AI/Learning/Udemy")
relPath = childPath.relative_to(root)
print(len(relPath.parts))
displayTree()