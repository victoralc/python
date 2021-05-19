# Complexity Time Total O(n2)
def selection_sort(a_list):
    # Complexity Time O(n)
    for i in range(0, len(a_list)):
        small = find_smaller(a_list, i)
        swap(a_list, i, small)


def swap(a_list, current, other):
    a_list[current], a_list[other] = a_list[other], a_list[current]


# Complexity Time O(n)
def find_smaller(a_list, i):
    return a_list.index(min(a_list[i:]))


numbers = [45, 3, 7, 89, 2, 10, 8, 9, 25, 17, 13, 11, 1, 60, 36, 15, 4, 18]

selection_sort(numbers)

print(numbers)