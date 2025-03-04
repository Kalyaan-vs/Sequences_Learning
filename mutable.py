shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
print(another_list)

shopping_list += ["cookies"]
print(shopping_list)
# print(id(shopping_list))
print(another_list)
# ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']
# Because the bounded value of shopping_lit got mutated
a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
b.append("cream")
print(c)
print(d)

print("Adding cake")
d.append("cake")
print(shopping_list)

print()
# z = a.count("cream")
# print(z)

# To count "c" in the string of the items in shopping_list
z = 0
for i in a:
    z += i.count("c")
print(z)

