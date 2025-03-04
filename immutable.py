# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
# kalyaan = "HI"
# abc = "Hi"
# print(id(kalyaan))
# print(id(abc))

result = "Correct"  # result just the name that we bound to the value
another_result = result
print(id(result))  # printing the ID of "Correct" here
print(id(another_result))  # printing the ID of "Correct" here

result += "ish"
# result rebounded to a new value. i.e, result destroyed and re-created
# because strings are immutable
print(result)
print(id(result))
print(another_result)  # Correct
# Because it still referenced to the value of result which created first
print(id(another_result))

