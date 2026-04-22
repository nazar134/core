import file_engine
import math 
import text


while True:
    try:
        command = input("Enter a command: ")

        
        with open("history.txt", "a") as f:
            f.write(command + "\n")
        if command == "file engine":
            file_engine.fileen()
        if command == "math engine":
            math.mat()
        if command == "formula engine":
            math.formula()
        if command == "text engine":
            text.textfile()
        if command == "history":
            try:
                with open("history.txt", "r") as f:
                    print(f.read())
            except FileNotFoundError:
                with open("history.txt", "w") as f:
                    f.write("")
        if command == "clear history":
            with open("history.txt", "w") as f:
                f.write("")
        if command == "funct engine":
            math.funct()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
       
        
        
    
    

    