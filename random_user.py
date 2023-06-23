import random

def cs(x):
    low = 1
    high = x
    feed = " "
    while feed != 'c':
        guess = random.randint(low,high)
        feed = input(f"Is my guess {guess} is too high(h) or too low(l) or correct(c)")
        if feed == 'h':
            high = high-1
        elif feed == 'l':
            low = low+1
        else:
            print(f"Gotcha! computer guessed your number {guess} correctly")

cs(10)