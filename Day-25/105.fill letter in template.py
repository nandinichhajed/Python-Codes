letter = '''Hiii, <|Name|>  
Thankyou for your details 
you are selected
regards,
Nandini
Date: <|Date|> '''

a = input("enter your name: ")
b = input("enter date: ")         
         
letter = letter.replace("<|Name|>", a)
letter = letter.replace("<|Date|>", b)

print(letter)
