"""
copyfile() - copies contents of the file
copy() - copyfile() + permission mode + destination can be a directory
copy2() - copy() + copies metadata (file's creation and modification times)
"""

import shutil
shutil.copyfile("C:\\Users\\Micha\\Desktop\\imhere.txt", "C:\\Users\\Micha\\Desktop\\copy.txt")
# above we list a target file patch as an argument, then the destination and name of the copy of the file

