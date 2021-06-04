import time


def print_even_numbers():
    start = time.time()
    number = 2
    while number <= 100000:
        if number % 2 == 0:
            print(number)
        number += 1
    stop = time.time()
    print("The time of the run: ", stop - start)


def print_even_numbers_2():
    start = time.time()
    number = 2
    while number <= 100000:
        print(number)
        number += 2
    stop = time.time()
    print("The time of the run: ", stop - start)


if __name__ == '__main__':
    #print_even_numbers()
    print_even_numbers_2()