print(" *** Creating Dictionary 2 ***")
user_input = input("Enter text : ").split()

user_input_dict = {}
for i in range(0, len(user_input) - 1, 2):
    key = user_input[i]
    item = int(user_input[i+1])
    if key in user_input_dict:
        user_input_dict[key] += item
    else:
        user_input_dict[key] = item

print(user_input_dict)