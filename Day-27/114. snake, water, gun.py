import random

def gamewin(comp, you):
    if comp == you:
        return None
    
    
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    
    
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
        
        
    elif comp == 'g':
        if you == 'w':
            return False
        elif you == 's':
            return True
            
        


print("Computer's turn: snake(s), water(w), gun(g)?")
p = random.randint(1, 3)
if p == 1:
    comp = 's'
elif p == 2:
    comp = 'w'
elif p == 3:
    comp = 'g'    
# print(p)

you = input("Computer's turn: snake(s), water(w), gun(g)?")

a = gamewin(comp, you)

print(f"comp choose {comp}")
print(f"you choose {you}")


if a == None:
    print("its a tie")
elif a:
    print("you win")
else:
    print("you loss")
    