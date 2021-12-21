oldname = input("enter the name of the file: ")
newname = input("enter the new name of the file: ")

with open(oldname, "r") as f:
    text = f.read()

with open(newname , "w") as f:
    f.write(text)

os.remove(oldname)    