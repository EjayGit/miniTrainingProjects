import os

def top_down_walk():
    for dirpath, dirnames, files in os.walk('../', topdown=False):
        print("Directory: ", dirpath)
        print("---Includes these directories---")
        for dirname in dirnames:
            print(dirname)
        print("---Includes these files---")
        for file in files:
            print(file)
        print()

top_down_walk()