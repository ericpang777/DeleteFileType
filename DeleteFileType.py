#! python3
import os

path = "C:\\Users\\"  # Put path to folder where you want to search
file_type = ""  # File Type

def get_files(str):
    if(str == "print"):
        # Prints files about to be deleted
        for file in os.listdir(path):
            if file.endswith(file_type):
                print(file)
        return

    if(str == "delete"):
        # Deletes files
        for file in os.listdir(path):
            if file.endswith(file_type):
                tempPath = path + "\\" + file
                os.remove(tempPath)
    return

file_type = input("What file type do you want to remove?\n").strip()
print("Make sure you edited this program to include the folder path!\n")
print("Do you want to remove these files (forever) ending with " + file_type + "?\n")
get_files("print")

if input("\n(y) Yes | (n) No\n").strip().lower() == "y":
    get_files("delete")
else:
    raise SystemExit