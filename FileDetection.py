import os

path = "C:\\Users\\Micha\\Desktop\\imhere.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location does not exist!")