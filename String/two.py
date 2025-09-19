print(" *** Remove ODD characters ***")
user_input = input("Enter a string : ")

result = ""
for i in range(len(user_input)):
    if (i+1) % 2 == 0:
        result += user_input[i]

print(f"Even characters = {result}")
print("===== End of program =====")

