available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]
computer_parts = []
current_choice = "-"
valid_choices = []

for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)  # remove elements form a list
        else:
            print("Adding {} to shopping list".format(chosen_part))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print("Your shopping list {}".format(computer_parts))