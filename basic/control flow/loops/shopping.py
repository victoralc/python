shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice", "oranges"]

item_to_find = "albatross"
found_at = None

# for index in shopping_list:
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

