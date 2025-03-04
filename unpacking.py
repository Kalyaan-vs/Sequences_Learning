a = b = c = d = e = f = 42
print(c)
print()

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking the tuples")

data = 1, 2, 76  # data represent tuple
x, y, z = data  # Here, we assigned x, y, and z to the value of tuple
print(data)
print(x)
print(y)
print(z)

print("Unpacking a list")

data_list = [12, 13, 14]
p, q, r = data_list
print(data_list)
print(p)
print(q)
print(r)

# data = x, y, z
# print(data == (x, y, z))  # True
# x = 10  # Here, x is rebounded to a new value 10
# print(data[0])  # But, doesn't change the value x in the tuple data
# print(data == (x, y, z))  # False
# print()
