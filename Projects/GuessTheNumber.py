import random
number=random.randint(1,50)

print("-"*20)
print("Guess the Number B/t 1-50 ?")
print("You have Five Chances !!!")


for num in range(5):
    print("-" * 20)
    guess=int(input("Enter your Guess: "))


    if guess==number:
        print("-" * 20)
        print("Right Guess!! Congratulations You Win")
        break

    elif guess>number:
        print("-"*20)
        print("Too High")


    elif guess<number:
        print("-" * 20)
        print("Too Low")

    else:
        print("-"*20)
        print("Wrong Guess!")
        print("-"*20)
else:
    print("Number is =",number)
    print("-"*20)
