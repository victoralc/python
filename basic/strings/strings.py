name = "Carlos Victor de Alcantara Carleial"
print(name[5:10])
print(len(name))

# Slices

parrot = "Norwegian Blue"

# Up to but not including
print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[0:9])  # IN
print(parrot[:9])

print(parrot[10:14])
print(parrot[:6] + parrot[6:])
print(parrot[6:])

print(parrot[:])

letters = "abcdefghijklmnopqrstuvwxyz"

print(parrot[0:6:2]) # Norwed

number = "9,223;372;036.854:775,807"

separators = number[1::4]
print(number[1::4])

name = "Carlos Victor de Alcantara Carleial"

print(name[1][0])
