import os
from datetime import datetime

def formatDatetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formatted_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formatted_date

def displayCwd():
    cwd = os.getcwd()
    print(f"Current wd is: {cwd}")

def upOneDirLvl():
    os.chdir("../")

def displayEntriesInDir():
    entries = os.scandir()
    for entry in entries:
        info = entry.stat()
        print(f"{entry.name}. Creation date: {formatDatetime(info.st_birthtime)}")
        print(f"{entry.name}. Access date: {formatDatetime(info.st_atime)}")
        print(f"{entry.name}. Size: {info.st_size}")

def display_directories(directory):
    entries = os.scandir(directory)
    for entry in entries:
        if entry.is_dir():
            print(f"Directory name: {entry.name}")

def displayFiles(directory):
    entries = os.scandir(directory)
    for entry in entries:
        if entry.is_file():
            print(f"File name: {entry.name}")

displayCwd()
upOneDirLvl()
displayCwd()
displayEntriesInDir()
display_directories('../')
displayFiles('../')