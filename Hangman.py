import random

Words_Bank=["rose","lily","lotus","sunflower","tulip","jasmine","iris","orchid","snowdrop","daisy"]
User_Mistake=0
right_guess=[]
wrong_guess=[]

#x=random.randint(0,len(Words_Bank)-1)
#Word=Words_Bank[x]

Word=random.choice(Words_Bank)
print(Word,len(Word))

while User_Mistake<6:
    for i in range(len(Word)):
        if Word[i] in right_guess:
            print(Word[i], end=" ")
        else:
            print("-",end=" ")
    
    User_Char=input("\nPlease enter your guess :")
    User_Char=User_Char.lower()
    if len(User_Char)==1:
        if User_Char in Word:
            print("👍")
            right_guess.append(User_Char)
            if len(right_guess)==len(Word):
                print(f"\n 🏆 You Win 🏆 \n The correct word is: {Word}")
                print(f"You with total guesses : {len(right_guess)+len(wrong_guess)} guesses and {len(wrong_guess)} wrong guess ")

                break
        else:
            print("👎")
            User_Mistake+=1
            wrong_guess.append(User_Char)
    else:
        print("You can guess only one character at every step, Try Again")

if User_Mistake==6:
    print(" ☠ Game Over ☠ ")
   

