import os
import glob
import shutil

for fileName in glob.glob("*.py"):
    newPath = os.path.join('archive', fileName)
    print(newPath)
    shutil.move(fileName, newPath)
    