data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, -1, -1):
#     if min_valid >= data[index] or data[index] >= max_valid:
#         del data[index]
#         print(index, data)

# This code is efficient because in the previous one.
# the index lookups on line 8 is not very efficient than enumerate
top_index = len(data) - 1
# print(top_index)
for index, value in enumerate(reversed(data)):
    if value <= min_valid or value >= max_valid:
        print((top_index - index), value)
        del data[(top_index - index)]

#
print(data)
