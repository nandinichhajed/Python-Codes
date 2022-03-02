class Employe:
    compeny = "Google"
    
Nandini = Employe()
Archit = Employe()

print(Nandini.compeny) 
print(Archit.compeny)

Employe.compeny = "Youtube"
print(Nandini.compeny) 
print(Archit.compeny)