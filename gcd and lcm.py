#import math
#print(math.gcd(int(input()),int(input())))
#print(math.lcm(int(input()),int(input())))

first_number=0
second_number=0
f_number=0
s_number=0

user_choice=input("Enter gcd or lcm to calculate it between your numbers: ")
user_choice=user_choice.lower()

if(user_choice=="gcd" or user_choice=="lcm"):
    first_number=int(input("Enter your first number:"))
    second_number=int(input("Enter your second number:"))
    f_number=first_number
    s_number=second_number

    if first_number < second_number:
        first_number,second_number=second_number,first_number

    while second_number!=0:
        result=first_number%second_number
        first_number=second_number
        second_number=result
    
    final_result=first_number

    if user_choice=="lcm":
        final_result=(f_number*s_number)/final_result     

    print(f"you choose to calculate {user_choice} between {f_number} and {s_number}.\nthe result is = {int(final_result)}")

else:
    print("we only calculate gcd or lcm, try again")

