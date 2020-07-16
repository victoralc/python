names = ["Victor", "Maria", "Joao", "Alcantara"]

print("Lenght: " + str(len(names)))
print("Ordered: " + str(sorted(names)))
names.append("Pedro")
print("Adding: " + str(names))
print(" & ".join(sorted(names)))

computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
for part in computer_parts:
    print()
    print(computer_parts[2])
    print(computer_parts[0:2])
    print(computer_parts[-1])