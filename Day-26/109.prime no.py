n = int(input())
prime = True
for i in range(2, n):
    if (n % i == 0):
        prime = False
        break
        
if prime:
    print("its a prime no")
    
else:
    print("non prime")