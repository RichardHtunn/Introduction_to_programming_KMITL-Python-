def init_square(square_type, size):
    if square_type == 0:
        # Type 0: Borders filled with '*'
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    print(" *", end="")   # keep alignment
                else:
                    print("  ", end="")  # double space
            print()

    elif square_type == 1:
        # Type 1: Borders with numbers (aligned)
        for i in range(size):
            for j in range(size):
                if i == 0:  # top row
                    print(f"{j+1:2}", end=" ")
                elif i == size - 1:  # bottom row
                    print(f"{size-j:2}", end=" ")
                elif j == 0:  # left column
                    print(f"{i+1:2}", end=" ")
                elif j == size - 1:  # right column
                    print(f"{size-i:2}", end=" ")
                else:
                    print("  ", end=" ")
            print()

    elif square_type == 2:
        # Type 2: Alternating border + diagonals '*'
        if size % 2 == 0:
            print("Type 2 square doesn't support an even number")
            return

        for i in range(size):
            for j in range(size):
                if i == j or i + j == size - 1:
                    print(" *", end="")
                elif i == 0 or j == 0 or i == size - 1 or j == size - 1:
                    if (i + j) % 2 == 0:
                        print(" *", end="")
                    else:
                        print(" @", end="")
                else:
                    print("  ", end="")
            print()


# Main program
print("*** Draw square ***")
user_input = input("Enter type and size: ").split()
t = int(user_input[0])
s = int(user_input[1])
init_square(t, s)
print("===== End of program =====")
