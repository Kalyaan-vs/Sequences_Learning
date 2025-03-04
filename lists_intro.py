computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "monitor",
                  "mouse mat"
                  ]
print(computer_parts)

# computer_parts[3] = "track ball"
# print(computer_parts)
computer_parts[1:5:2] = ["track ball", "pen-drive"]
print(computer_parts)
print(computer_parts.index("monitor", 2, 5))
print(computer_parts.pop(4))
computer_parts.remove("track ball")
print(computer_parts)
# for part in computer_parts:
#     print(part)
#
# print()
# print(computer_parts[2])
# print(computer_parts[:2])
# print(computer_parts[::2])
# print(computer_parts[5:0:-1])

