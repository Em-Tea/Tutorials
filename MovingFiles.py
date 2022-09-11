import os

source = "C:\\Users\\Micha\\Desktop\\copy.txt"
destination = "C:\\Users\\Micha\\Documents\\movedcopy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(f'{source} was moved')
except FileNotFoundError:
    print(f'{source} not found!')