# print("*** Creating Dictionary ***")
# user_input = input("Enter text : ").split()

# user_input_dict = {}

# for i in range(0, len(user_input) - 1, 2):
#     key = user_input[i]
#     value = user_input[i+1]
#     user_input_dict[key] = value

# print(user_input_dict)

print("*** Creating Dictionary ***")
user_input = input("Enter text : ").split()

user_input_dict = {}
for i in range(0, len(user_input) - 1, 2):
    key = user_input[i]
    value = int(user_input[i+1])
    if key in user_input_dict:
        user_input_dict[key] += value
    else:
        user_input_dict[key] = value

print(user_input_dict)