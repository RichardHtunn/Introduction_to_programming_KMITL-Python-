shopping_dict = {
    "egg": 1,
    "ham": 1,
    "water": 1,
    "soda": 1,
}

user_input = input("Enter op, item : ")
slipt_user_input = user_input.split(",")

for s in slipt_user_input:
    pair = s.strip().split()
    if len(pair) != 2: #has to be 2 words since input required both operation and item
        print("Operation not supported!")

    op, item = pair[0] , pair[1].lower()
    if op == "a":
        shopping_dict[item] = shopping_dict.get(item,0) + 1
    elif op == "r":
        if item in shopping_dict:
            shopping_dict[item] -= 1
            if shopping_dict[item] == 0:
                shopping_dict.pop(item)
    else:
        print("Operation not supported")

print("Final shopping list ==>",shopping_dict)