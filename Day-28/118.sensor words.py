with open(r"C:\Users\91910\Documents\GitHub\Python-Codes\Day-28\sample.txt") as f:
    p = f.read()

p = p.replace("Donkey", "####")

with open(r"C:\Users\91910\Documents\GitHub\Python-Codes\Day-28\sample.txt", "w") as f:
    p = f.write(p)
