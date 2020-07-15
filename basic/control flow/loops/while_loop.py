#for i in range(10):
#    print("i is now {}".format(i))

i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

chosen_exit = ""
available_exits = ["north", "south", "east", "west"]
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose one exit")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
else:
    print("Thank you for playing")