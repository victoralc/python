array = ["banana", "apple", "strawberry", "elderberries", "cucumbers", "dates"]

# Read operation is efficient. Straightforward to find example: array[3]
print(array[3])

# Search operation
# Basic search operation is linear search. Less efficient than reading.
# It searches through all the array until find the element.

#Insert takes O(N) at the worst case: It needs to shift all elements to insert a value
array.insert(5, "mango")

#Deletion takes O(N) at the worst case: It needs to shift all elements after remove a value
array.remove("apple")
