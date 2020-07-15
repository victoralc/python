import random

highest = 10
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
guess = 0  # Initialise to any number that doesn't equal the answer
print('Please guess number between 1 and {}'.format(highest))

while guess != answer:
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed correctly")
        break
    else:
        if guess < answer:
            print('Please guess higher')
        else:  # guess must be greater than answer
            print("Please guess lower")
