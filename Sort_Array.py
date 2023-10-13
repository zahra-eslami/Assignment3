import random
array=[]
array_size=0
i=1
sort="no"

print("We want to check your array for Ascending sort")
try:
    array_size=int(input("please enter the size of your array : "))
except:
    print("You must enter an integer number:")

while array_size!= len(array):
    try:
        x=int(input(f"please enter your {i} number: "))
        array.append(x)
        i+=1
    except:
       print("please enter an integer number")
i=1
for i in range(array_size-1): 
    if array[i]>array[i+1]:
        sort=input("your array isn't sort\nIf you want to sort your array enter yes : ")
        break
    else:
        print(f"you have a sorted array\n your array ={array}")

#bubble sort
if sort=="yes":
    i=0
    for i in range(array_size-1):
        for j in range(array_size-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    print(f"Your sorted array is ={array}")                