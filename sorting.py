pangram = "The quick brown fox jumps over a lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.33, 4.25, 1.24, 3.45, 9.87, 7.84]
sorted_numbers = sorted(numbers)
another_sorted_numbers = sorted_numbers
print(another_sorted_numbers)
print(sorted_numbers is another_sorted_numbers)
print(numbers)
print()
numbers.sort()
print(numbers)
print(another_sorted_numbers)
print(numbers is sorted_numbers)

missing_letters = sorted("8940910356 The quick brown fox jumps over a lazy dog",
                         key=str.casefold, reverse=True)

print(missing_letters)

names = ["Kalyaan",
         "Harish",
         "Suraj",
         "santhosh",
         "Deepak",
         "Sreya Basak",
         "amrin",
         "Keerthana",
         "partha",
         "Karthik"
         ]
names.sort(key=str.casefold)
print(names)
