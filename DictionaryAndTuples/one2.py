print(" *** Creating Dictionary ***")
user_input = input("Enter text : ").split()

user_input_dict = {}
for i in range(0, len(user_input) - 1, 2):
    key = user_input[i]
    item = user_input[i+1]
    user_input_dict[key] = item

print(user_input_dict)

    