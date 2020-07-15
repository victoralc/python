name = input("What's your name? ")
age = int(input("How old are you ? "))

if 18 <= age < 31:
    print("Welcome to Holidays, {}".format(name))
else:
    print("Sorry, you can try to enter in Holdays later")
