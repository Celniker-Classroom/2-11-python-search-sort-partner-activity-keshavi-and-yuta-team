
from random import randint 


numbers = [] 
randomnumber=randint(1,20)
for index in range(10): 
    numbers.append(randint(1,20)) 

print("Generated List:" ,numbers) 
print("searching for numbers:" ,randomnumber)


if randomnumber in numbers:
    print("Number",randomnumber,"found in the list!")
else:
    print("Number",randomnumber,"not found in the list.")