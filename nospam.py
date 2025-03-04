menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

# Remove "spam" from each list and print the list
for meals in menu:
    for index in range(len(meals) - 1, -1, -1):
        if meals[index] == "spam":
            del meals[index]
            # meals.remove("spam") it can remove to confusion as it removes random spam
    print(meals)
    print(", ".join(meals))  # it won't modify the list

# for meals in menu:
#     for item in (meals[:]):
#         if item == "spam":
#             meals.remove("spam")
#     print(meals)

# for meals in menu:
#     no = meals.count("spam")
#     print(no)
#     i = 1
#     while i <= no:
#         meals.remove("spam")
#         i += 1
#     print(meals)

# Print the items as long as it's not "spam"
# for meals in menu:
#     for item in meals:
#         if "spam" not in item:
#             print(item, end=", ")
#     print()


