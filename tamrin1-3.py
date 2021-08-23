import random

n = int(input("Enter Array length:"))

array = []

for i in range(n):
    x = random.randint(0, 100) 
    if x not in array:
        array.append(x)
print (array)