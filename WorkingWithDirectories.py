from pathlib import Path

# Absolute path - Starts from the root of the hard disk and works outward from there.
# c:\Program Files\Microsoft
# Related path - A related path starts from the current directory and then points somewhere else

path1 = Path("ecommerce") # If we do not pass an argument, default is current directory
print(path1.exists()) # Returning boolean value representing existence of class parameter

path2 = Path("emails")
# print(path2.mkdir()) # Creation of a relative directory
# print(path2.rmdir()) # Deletiob of object directory

path3 = Path()
for file in path3.glob('*'): # The glob method searches for files or directories using a pattern
    print(file)