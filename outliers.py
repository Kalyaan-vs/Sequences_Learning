# data = [4, 5, 123, 125, 134, 146, 154, 156, 157,
#         163, 168, 169, 178, 198, 234, 344, 350]
# data = [4, 5, 123, 125, 134, 146, 154, 156, 157,
#         163, 168, 169, 178, 198, 234]
# data = [123, 125, 134, 146, 154, 156, 157,
#         163, 168, 169, 178, 198, 234, 344, 350]
# data = [123, 125, 134, 146, 154, 156, 157,
#         163, 168, 169, 178, 198]
data = [4, 5, 234, 345, 350]
# data = []

data.sort()
print(data)
min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if min_valid <= data[index] <= max_valid:
        # We have the index of
        # the last item we need to keep.
        # Set 'start' to the position of next.
        # item to delete, which 1 is after 'index'
        start = index + 1
        break
print(start)  # for debugging
del data[start:]
print(data)

# Not efficient one
# stop = 0
# for index, value in enumerate(data):
#     if value <= max_valid:
#         stop = index
# print(stop)
# del data[stop + 1:]
# print(data)

# del data[0:3]
# print(data)
# del data[-3:-1]
# print(data)

# for i in range(10, -2, -1):
#     print(i)
