print(" *** Adding number ***")
user_input = input("Enter your words : ").split()

for i in range(len(user_input)):
    new_input = user_input[i]
    if i % 2 == 1:
        new_input = new_input[::-1]
    print(f"{new_input}{i+1} ",end="")
print()

print("==== End of program =====")


