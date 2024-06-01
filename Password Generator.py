import random
import string
password_number=int(input("Generate A Random Password:"))
character_list=[i for i in string.ascii_letters]
numbers=[j for j in string.digits]
symbols=["!","@","#","$","%","^","&","*"]
character_list.extend(numbers)
character_list.extend(symbols)
result=''
for i in range(password_number):
   result+=random.choice(character_list)
print(f"The Random Password is: {result}")
