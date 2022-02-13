def game():
    return 456

score = game()
with open(r"C:\Users\91910\Documents\GitHub\Python-Codes\Day-28\HeighScore.txt") as f:
    txt = f.read()

    if txt == '' :
        with open(r"C:\Users\91910\Documents\GitHub\Python-Codes\Day-28\HeighScore.txt", 'w') as f:
            f.write(str(score))
                
    elif int(txt) < int(score) :
        with open(r"C:\Users\91910\Documents\GitHub\Python-Codes\Day-28\HeighScore.txt", 'w') as f:
            f.write(str(score))
            
            
game()