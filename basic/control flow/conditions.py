age = int(input("How old are you ?"))

if 16 <= age <= 65:
    print('Have a good day at work')
else:
    print("Enjoy your free time")


print("--" * 10)

day = "Monday"
temperature = 30
raining = True

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn python")

if 1:
    print("true")
else:
    print("False")

name = "Carlos Victor"
if name:
    print("Hello, {}".format(name))
