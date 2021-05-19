def binary_search(list, target):

    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list ")


numbers = [45, 3, 7, 89, 2, 10, 8, 9, 25, 17, 13, 11, 1, 60, 36, 15, 4, 18]
numbers.sort()

print(numbers)

result = binary_search(numbers, 10)
verify(result)