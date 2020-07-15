for i in range(10, 0, -2):  # not including the final number
    print("i is now {}".format(i))

for i in range(1, 11):
    for j in range(1, 11):
        print("{0} times {1} is {2}".format(j, i, i * j))