import re
def mat():
    print("write the math problem you want to calculate")
    mah = input()
    ma = eval(mah)
    print(ma)
    q = input("do you want to save the result? (y/n)")
    if q == "y":
        l = input("do you want to have new file? (y/n)")
        if l == "n":
            try:
                name = input("enter the name of the file: ")
                with open(name + ".txt", "a") as f:
                    f.write(str(ma))
            except FileNotFoundError:
                print("File not found.")
           
        if l == "y":            
            name = input("enter the name of the file: ")
            with open(name + ".txt", "w") as f:
                f.write(str(ma))


def formula():
    print("write the formula you want to calculate")
    print("did you have the file with the formula? (y/n)")
    m = input()
    if m == "y":
        name = input("enter the name of the file: ")
        try:
            with open(name + ".txt", "r") as f:
                form = f.read()
                print("the formula is",form)
        except FileNotFoundError:
            print("File not found.")
            return
    if m == "n":
        print("write the formula you want to calculate")
        form = input()
    frm = form

    
    h = re.split(r'[\+\-\*\/\(\)\s]+', form)
    h = [x for x in h if x and not x.isdigit()]
    
    for j in h:
        print("what is the value of",j)
        v = input()
        form = form.replace(j,v)
    for k in form:
        for l in h:
            if k == l:
                form = form.replace(k,v)
    result = eval(form)
    print("the result is",result)
    if m == "n":

        print("do you want to save the formula? (y/n)")
        save = input()
        if save == "y":
            name = input("enter the name of the file: ")
            with open(name + ".txt", "w") as f:
                f.write(frm)


    

                                

            
    
    
def funct():
    print("write the function you want to calculate")
    print("did you have the file with the function? (y/n/quadra)")
    m = input().strip().lower()

    if m == "y":
        name = input("enter the name of the file: ").strip()
        try:
            with open(name + ".txt", "r") as f:
                form = f.read().strip()
                print("the function is", form)
        except FileNotFoundError:
            print("File not found.")
            return
    elif m == "n":
        print("write the function you want to calculate")
        form = input().strip()
    elif m == "quadra":
        print("chose the type of the quadratic function standard(a*x**2 + b*x + c)/mynus(a*x**2 + b*x + c)")
        q = input()
        if q == "standard":
            form = "a*x**2 + b*x + c"
        elif q == "mynus":
            form = "a*x**2 - b*x + c"
    else:
        print("Invalid option")
        return

    frm = form  

   
    h = re.split(r'[\+\-\*\/\(\)\s]+', form)
    h = [x for x in h if x and not x.isdigit()]

    org_form = form
    qw = []

    if m == "quadra":
        print("the formula is", form)
        print("enter the coefficient values:")
        
        print("what is the value of a?")
        a = input().strip()
        print("what is the value of b?")
        b = input().strip()
        print("what is the value of c?")
        c_coeff = input().strip()

        org_form = form.replace("a", a).replace("b", b).replace("c", c_coeff)

        try:
            a_val = float(a)
            b_val = float(b)
            c_val = float(c_coeff)
            vertex_x = -b_val / (2 * a_val)
            print("the peak(x) is", vertex_x)

            vertex_y = eval(org_form.replace("x", str(vertex_x)))
            print("the peak(y) is", vertex_y)
        except Exception as e:
            print("Error calculating quadratic peak:", e)

    else:  
        for j in h:
            if j != "x" and j != "y":
                print(f"what is the value of {j}?")
                v = input().strip()
                org_form = org_form.replace(j, v)

    if "x" in h:
        for i in range(-100, 100):          
            try:
                val = eval(org_form.replace("x", str(i)))
                qw.append((i, val))        
            except:
                pass 

    print("the result is", qw)

    if m == "n":
        print("do you want to save the function? (y/n)")
        save = input().strip().lower()
        if save == "y":
            name = input("enter the name of the file: ").strip()
            with open(name + ".txt", "w") as f:
                f.write(frm)








