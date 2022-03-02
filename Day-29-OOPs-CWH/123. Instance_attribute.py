class Employe:
    compeny = "Google"
    salarry = 100 # class attribute
    
Nandini = Employe()
Archit = Employe() 

Nandini.salarry = 300
Archit.salarry = 200 # instance attribute

print(Nandini.salarry) 
print(Archit.salarry)