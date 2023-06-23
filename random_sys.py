import random

def func(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f"Enter a number between 1 and {x}:"))
        if guess>random_number:
            print("eee! your guess is too high")
        elif guess<random_number:
            print("eee! your guess is too low")
        else:
            print(f"Hurray!,your guess {random_number} is correct")
            break

func(10)