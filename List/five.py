print(" *** Rectangle down-left-up-left ***")
user_input = input("Enter width height : ").split()
width = int(user_input[0])
height = int(user_input[1])

rectangle = []
for i in range(height):
    rectangle.append([0] * width)

row, col = 0, width - 1 
direction = "down"

for num in range(1, width * height + 1):
    rectangle[row][col] = num

    if direction == "down":
        if row + 1 < height and rectangle[row + 1][col] == 0:
            row += 1
        else:
            direction = "left"
            col -= 1

    elif direction == "up":
        if row - 1 >= 0 and rectangle[row - 1][col] == 0:
            row -= 1
        else:
            direction = "left"
            col -= 1

    elif direction == "left":
        if row - 1 >= 0 and rectangle[row - 1][col] == 0:
            direction = "up"
            row -= 1
        elif row + 1 < height and rectangle[row + 1][col] == 0:
            direction = "down"
            row += 1
        else:
            col -= 1

for i in range(height):
    for j in range(width):
        print(f"{rectangle[i][j]:3}", end="")
    print()

print("===== End of program =====")
