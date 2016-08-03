#! python3
import os

path = "C:\\Users\\"  # Put path to folder where you want to search
fileType = '.sfk'  # File Type

def GetFiles(str):
    if(str == "print"):
        # Prints files about to be deleted
        for file in os.listdir(path):
            if file.endswith(fileType):
                print(file)
        return

    if(str == "delete"):
        # Deletes files
        for file in os.listdir(path):
            if file.endswith(fileType):
                tempPath = path + "\\" + file
                os.remove(tempPath)
    return

print("Make sure you edited this program to include the folder path!\n")
print("Do you want to delete these files ending with "+fileType+"?\n")
GetFiles("print")

if input("\n(y) Yes | (n) No\n").strip().lower() == "y":
    GetFiles("delete")
else:
    raise SystemExit