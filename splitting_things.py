pangram = """The quick brown 
fox jumps\tover 
the lazy dog"""

words = pangram.split()
print(words)

number = "9, 223, 373, 036, 854, 775, 807"
print(number.split(", "))

# values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
print(generated_list)
values_lists = "".join(generated_list).split()
print(values_lists)

# int_list = []
# for value in values_lists:
#     int_list.append(int(value))
# print(int_list)


for index in range(len(values_lists)):
    values_lists[index] = int(values_lists[index])
print(values_lists)
