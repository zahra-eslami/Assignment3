#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.

import random
array=[]
array_size=0

try:
    array_size=int(input("please enter the size of array : "))
except:
    print("You must enter an integer number")

while array_size!= len(array):
    x=random.randint(1,1000)
    if x not in array:
        array.append(x)
if array_size>0:
    print("Your array list is: ",array)
else:
    print("Sorry, We cant create an array without an integer length")
