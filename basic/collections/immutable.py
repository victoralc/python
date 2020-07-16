result = True
another_result = result

print(id(result))  # use of id
print(id(another_result))

result = False
print(id(result))

result = "Correct"
another_result = result + "is"
print(id(result))
print(id(another_result))