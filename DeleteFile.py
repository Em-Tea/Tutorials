import os
import shutil

path = "folderfolder"

try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)  # REMOVE TREE - BE CAREFUL WITH THIS
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("You do not have permission to delete this")
except OSError:
    print("You cannot delete that with this function")
else:
    print("Target deleted...")

