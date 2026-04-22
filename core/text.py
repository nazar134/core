import os

def textfile(): 
    print("do you want to create a text file? 1")
    print("do you want to write in the text file? 2")
    print("do you want to delete the text file? 3")
    answer = input("")

    if answer == "1":
            fn = input("what do you want to name the file? ")
            with open(fn + ".txt", "w") as f:           
                print("what do you want to write in the file?")
                text = input("")
                f.write(text)
                    
    if answer == "2":
            fkn = input("what is the name of the file? ")
            try:
                with open(fkn + ".txt", "r") as f:
                    print(f.read())
                with open(fkn + ".txt", "a") as f:
                    print("what do you want to write in the file?")
                    text = input("")
                    f.write(text)
            except FileNotFoundError:
                print("file not found")

    if answer == "3":
            fnj = input("what is the name of the file? ")
            if fnj == "history":
                print("you can't delete history file")
                return
            try:
                os.remove(fnj + ".txt")
            except FileNotFoundError:
                print("file not found")

        
    
