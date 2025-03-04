# for index, character in enumerate("abcdefgh"):
#     print(index, character)

# unpacking lecture codes
for t in enumerate("abcdefghi"):
    index, character = t
    print(index, character)

index, character = (0, "a")
print(index)
print(character)

print()
