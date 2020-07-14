roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# Invalid Expressions
# LXIVXIIVIIVLDCM
# DCIXIVVILXIX
# LXIVXII
# LXIVXIIVIIVLDCM


# Roman to integer method
def roman_to_integer(s: str) -> int:
    array = list(s)

    for i in reversed(array):
        print(i)

    print(str(array))
    return 1


print(roman_to_integer("LXIV"))
