empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for numbers_list in numbers:
    print(numbers_list)

    for value in numbers_list:
        print(value)


# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)
#
# digits = sorted("4258465135")
# print(digits)  # returns in ascending order as list of strings
#
# digits = list("4258465135")
# print(digits)
#
# more_numbers = list(numbers)
# print(more_numbers)
# more_numbers = numbers[:]
# print(numbers)
# print(more_numbers)
# more_numbers = numbers.copy()
# more_numbers[1][2] = 20
# print(more_numbers)
# print(more_numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)
#
# even.extend(odd)
# print(even)
# another_even = even
# print(another_even)
# even.sort()
# print(even)
# print(another_even)
#
# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("mississippi".count("iss"))
