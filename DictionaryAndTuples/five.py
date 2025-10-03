shopping_dict = {
    "egg": 1,
    "ham": 1,
    "water": 1,
    "soda": 1,
}

print("*** Shopping List 2 ***")
text = input("Enter some pairs of (operation, item): ")

commands = text.split(",")

for cmd in commands:
    parts = cmd.strip().split()
    if len(parts) != 2:
        print("Operation not supported!")
        exit()

    op, item = parts[0], parts[1].lower()

    if op == "a":
        shopping_dict[item] = shopping_dict.get(item, 0) + 1

    elif op == "r":
        if item in shopping_dict:
            shopping_dict[item] -= 1
            if shopping_dict[item] == 0:
                shopping_dict.pop(item)

    else:
        print("Operation not supported!")
        exit()

print("Final shopping dict is", shopping_dict)
