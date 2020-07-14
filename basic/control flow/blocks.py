# Demonstration of If block
name = input("Please enter your name: ")
age = int(input("How old are you, {0} ?".format(name)))
print(age)

if age > 18:
    print("You are old enough to vote")
elif age < 18:
    print("The age is ok to enter.")
else:
    print("Please come back in {0} years".format(18 - age))
