import random
number=random.randint(1,10)
for i in range(0,3):
    user=int(input("Guess the number"))
    if user==number:
        print("Hurry!!")
        print("You guess the right number it's ",number)
        break
if user!=number:
    print("You guess incorrect number.The number is ",number)