string1 = "he's "
string2 = "probably "
string3 = "for the "
string4 = "pining"
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

print("Hello " * 5)

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "wednesday"

print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")

age = 30
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "Feb", "May", "May", "Jun", "Jul", "Aug"))

print("""
    Jan: {2}
    Feb: {0}
    Mar: {1}
    Apr: {2}
    May: {0}
    Jun: {1}
    Jul: {2}
    Aug: {1}
""".format(1,2,3,4,4,5,5,6))

for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(1, i ** 2, i ** 3))


print("Pi is approximately {0:8}".format(22/7))

