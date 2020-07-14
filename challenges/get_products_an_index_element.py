# Given an array you should return new array with a product of all numbers

# Solution 1
numbers = [1,2,3,4,5]
products = []

product = 1
# Brute force
for n in numbers:
    product = product * n

for n in numbers:
    p = product
    p = p // n
    products.append(p)

print(products) # products = [120, 60, 40, 30, 24]

# Solution 2

# Take before ith element subarray and post ith elements subarray
# Usar uma tecnica de pre compute subarrays





