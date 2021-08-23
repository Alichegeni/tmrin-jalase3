array = []

help = True

lenght = int(input("Enter Array length: "))

for i in range (lenght):

    num = int(input('enter number= '))
    array.append(num)

for j in range (lenght - 1):

    if array[j] > array [j + 1]:
        help = False
        break

if help :
    print('sort') 

else:
    print('not sort')
