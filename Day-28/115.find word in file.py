def fun():
    f = open(r"C:\Users\91910\Documents\GitHub\Python-Codes\Day-28\poems.txt")
    txt = f.read()
    # print(txt)
    if ("twinkle") in txt:
        print("yes")
    else:
        print("no")
    f.close()

fun()

# alternative
def fun():
    with open(r"C:\Users\91910\Documents\GitHub\Python-Codes\Day-28\poems.txt") as f:
        txt = f.read()
        if ("twinkle") in txt:
            print("yes")
        else:
            print("no")


fun()