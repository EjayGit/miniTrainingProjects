from datetime import datetime
import pathlib

def findLastModified(directory):
    time = 0
    resultFile = pathlib.Path(".")
    entries = directory.iterdir()
    for entry in entries:
        metaData = entry.stat()
        if time < metaData.st_mtime:
            time = metaData.st_mtime
            resultFile = entry.name
    return f"Date modified: {datetime.fromtimestamp(time)}, Filename: {resultFile}"

directory = pathlib.Path.cwd()
print(findLastModified(directory))