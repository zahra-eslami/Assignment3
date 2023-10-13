
try:
    snake_array=[]
    array_size=int(input("please enter snake length: "))
    for i in range(array_size):
        if (i % 2 ) == 0 :
            snake_array.append("🀄")
        else:
            snake_array.append("🧧")
    for i in range(array_size):
        print(snake_array[i],end="")
except:
    print("You must inter an integer number") 