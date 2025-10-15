print(" *** Reverse Even ***")
user_input = input("Enter integers : ").split()

user_input_list = []
for i in user_input:
    user_input_list.append(int(i)) 

even_list = []
odd_list = []

for number in range(len(user_input_list) - 1):
    if user_input_list[number] % 2 == 0:
        even_list.append(user_input_list[number])
    
print(even_list)
