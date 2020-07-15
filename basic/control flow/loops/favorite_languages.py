prog_lang = {1: "Python", 2: "Java", 3: "Go", 4: "Ruby", 5: "C/C++"}


def display_menu():
    print("Please choose your option from the list below:")
    for key, value in prog_lang.items():
        print("{}: \tLearn {}".format(key, value))


choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {} programming language".format(prog_lang[int(choice)]))
    else:
        display_menu()

    choice = input()
