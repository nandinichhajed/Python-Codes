words = ["donkey", "kaddu", "mota", "pagal"]

with open(r"C:\Users\91910\Documents\GitHub\Python-Codes\Day-28\sample.txt") as f:
    p = f.read()

for word in words:
    p = p.replace(word, "#$%&*^@")
    with open(r"C:\Users\91910\Documents\GitHub\Python-Codes\Day-28\sample.txt", 'w') as f:
        f.write(p)