# Tuples are immutable

t = ("a", "b", "c")
print(t)

metallica = "Ride the Lighting", "Metallica", 1984
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)

x, y = 1, 2
print(x)
print(y)

data_list = [12, 23, 76]
x, y, z = data_list
print(x, y, z)

print(bool(1))

for index, character in enumerate("abcdefgh"):
    print(index, character)
