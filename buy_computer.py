available_parts = [("computer", 50000),
                   ("monitor", 20000),
                   ("keyboard", 1000),
                   ("mouse", 1500),
                   ("mouse mat", 150),
                   ("hdmi cable", 300),
                   ]
# valid_choice = [int(i) for i in range(1, len(available_parts) + 1)]
# print(valid_choice)
# valid_choice = []
# for i in range(1, len(available_parts) + 1):
#     valid_choice.append(i)
# print(valid_choice)
PART_NAME = 0
PART_PRICE = 1
current_choice = None
computer_parts_price = 0
computer_parts = []  # create an empty list

while current_choice != 0:
    # if current_choice in valid_choice:
    if current_choice in range(1, len(available_parts) + 1):
        chosen_part = available_parts[current_choice - 1][PART_NAME]
        chosen_part_money = available_parts[current_choice - 1][PART_PRICE]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            computer_parts.remove(chosen_part)
            print(f"Removing {chosen_part}")
            computer_parts_price -= chosen_part_money
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
            computer_parts_price += chosen_part_money
        print(f"Your cart now contains {computer_parts} "
              f"with the total amount of  {computer_parts_price}")
    else:
        print("Please add option from the list below")
        # i = 1
        # for menu_items in available_parts:
        #     print(f"{i}. {menu_items}")
        #     i += 1
        for number, (part, price) in enumerate(available_parts):
            print(f"{number + 1}: {part:15} - RS.{price:<5}")
        print("0. To finish")

    current_choice = int(input())

print("So, your buying", computer_parts, f"And that will be ${computer_parts_price}")
# available_parts = ["computer",
#                    "monitor",
#                    "keyboard",
#                    "mouse",
#                    "mouse mat"
#                    ]
# current_choice = None
# computer_parts = []  # create an empty list
#
# while current_choice != 0:
#     if current_choice in len(available_parts):
#         print(f"Adding {current_choice}")
#         if current_choice == 1:
#             computer_parts.append("computer")
#         elif current_choice == 2:
#             computer_parts.append("monitor")
#         elif current_choice == 3:
#             computer_parts.append("keyboard")
#         elif current_choice == 4:
#             computer_parts.append("mouse")
#         elif current_choice == 5:
#             computer_parts.append("mouse mat")
#         else:
#             computer_parts.append("hdmi cable")
#     else:
#         print("Please add option from the list below")
#         # i = 1
#         # for menu_items in available_parts:
#         #     print(f"{i}. {menu_items}")
#         #     i += 1
#         for number, part in enumerate(available_parts):
#             print(f"{number + 1}: {part}")
#         print("0. To finish")
#
#     current_choice = int(input())
#
# print(computer_parts)
