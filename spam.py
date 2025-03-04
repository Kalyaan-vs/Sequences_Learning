menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

for meals in menu:
    if "spam" not in meals:
        print(meals)

        for item in meals:
            print(item, end=", ")
        print()

    else:
        print(f"{meals} has a spam count of {meals.count("spam")}")
