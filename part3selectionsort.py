from random import randint 

searchnumber = int(input("Insert a number 1-20 to look for in a list. There are only 10 numbers generated in the list."))

numbers = []

sum = 0

for index in range(10): 
    numbers.append(randint(1,20)) 


print(numbers)
smallest = numbers[0]
largest = numbers[0]

for index in numbers :
    sum += index
print ("The sum is" , sum)
for index in range(1, len(numbers)): 
   if numbers[index] < smallest:
       smallest = numbers[index] 

numbers.sort()
print("the sorted list is" ,numbers)
doubledlist = [i*2 for i in numbers]
print("The doubled version of the list is" ,doubledlist)
print("The first half of the sorted list is",numbers[0:5])
print("The second half of the sorted list is",numbers[5:11])
print("The smallest number in the list is:", smallest)
largest = numbers[0]


for index in range(1, len(numbers)): 
   if numbers[index] > largest:
       largest = numbers[index] 


print("The largest number in the list is:", largest)

rangeoflist=largest-smallest
print ("This list has a range pf ")
comparisons = 0  # Initialize the counter for comparisons
found=False


for index in numbers:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if index == searchnumber:
        found=True
        print("Number",searchnumber, "found after", comparisons, "comparisons!") 
        break
if found==False:
    print("Number",searchnumber, " not found after", comparisons, "comparisons.") 

