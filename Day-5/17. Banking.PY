# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.

# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100

# Then, the output should be:
# 500

# Code
amount = 0
while True:
    a = input("Deposit/Withdrow/Balance/Quit?\nD/W/B/Q: ").lower()
    if a == "d":
        Deposit = input("How much ammount would you like to Deposit: ")
        amount = amount + int(Deposit)
    elif a == "w":
        Withdrow = input("How much ammount would you like to Withdrow: ")
        amount = amount - int(Withdrow)
    elif a == "b":
        print(f"your current balance is {amount}: ")
    else:
        break
        