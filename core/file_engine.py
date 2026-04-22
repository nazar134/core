import os


def fileen():
    print("do you want to create new file 1")
    print("do you want to open a file 2")
    print("do you want to delete file 3")
    fi = input()
    if fi == "1":
        print("please write full name with file name")
        m = input()
        open(m,"w").close()
    if fi == "2":
        print("please write full name with file name")
        mm = input()
        try:
            os.system(f"open '{mm}' ")
        except FileNotFoundError:
            print("File not found.")
    if fi == "3":
        print("please write full name with file name")
        mmm = input()
        if mmm == "history.txt" or mmm == "math" or mmm == "text" or mmm == "file_engine" or mmm == "command_engine":
            print("you can't delete this file because it is important for the program <3")
            return
        try:
            os.remove(mmm)
        except FileNotFoundError:
            print("File not found.")


