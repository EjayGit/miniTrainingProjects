import pathlib

# Rename 1 file
def renameFile(filename, newname, filetype):
    seqLen = 0
    currentPath = pathlib.Path.cwd()
    # Find files in cwd
    for item in currentPath.iterdir():
        # If filename and file type of our search
        if item.stem == filename and item.suffix == filetype:
            updateName = newname + filetype
            item.rename(updateName)
            print(f"Filename was successfully changed from {filename+filetype} to {updateName}")
            return
        elif filename == 'ALL':
            updateName =  newname + str(seqLen) + filetype
            item.rename(updateName)
            seqLen += 1
            print(f"Filename was successfully changed from {item.name} to {updateName}")
            return
    print(f"The file(s) do(es) not exist.")
    return

renameFile('test', 'test1', '.txt')

# Rename all filenames