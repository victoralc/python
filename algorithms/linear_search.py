def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list ")


numbers = [45, 3, 7, 89, 2, 10, 8, 9, 25, 17, 13, 11, 1, 60, 36, 15, 4, 18]

result = linear_search(numbers, 10)
verify(result)

