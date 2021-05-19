def recursive_binary_search(my_list, target):
    if len(my_list) == 0:
        return False
    else:
        midpoint = (len(my_list)) // 2

        if my_list[midpoint] == target:
            return True
        else:
            if my_list[midpoint] < target:
                return recursive_binary_search(my_list[midpoint + 1:], target)
            else:
                return recursive_binary_search(my_list[:midpoint], target)


numbers = [45, 3, 7, 89, 2, 10, 8, 9, 25, 17, 13, 11, 1, 60, 36, 15, 4, 18]
numbers.sort()

result = recursive_binary_search(numbers, 10)
print("Target found: ", result)


