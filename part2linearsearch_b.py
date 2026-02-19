from random import randint 


numbers = [] 
randomnumber=randint(1,20)
for index in range(10): 
    numbers.append(randint(1,20)) 

print("Generated List:" ,numbers) 
print("searching for numbers:" ,randomnumber)

comparisons = 0  # Initialize the counter for comparisons
found=False


for index in numbers:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if numbers == randomnumber:
        found=True
        print("Number",randomnumber, "found after", comparisons, "comparisons!") 
        break
    else:
        print("Number",randomnumber, " not found after 10 comparisons")
        break

       
        



