print(" *** Sum odd / Substract even ***")
user_input = input("Enter numbers : ").split()

user_input_list = []
for i in user_input:
    user_input_list.append(int(i))

odd_list = []
even_list = []
for j in user_input_list:
    if j % 2 == 0:
        even_list.append(j)
    else:
        odd_list.append(j)

sum = 0
for o in odd_list:
    if o == -1:
        break
    else:
        sum += o

print(f"Sum is {sum:,}")
