# def init_square(square_type, size):
#     if square_type == 0:
#         for i in range(size):
#             for j in range(size):
#                 if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print()

#     elif square_type == 1:
#         for i in range(size):
#             for j in range(size):
#                 if i == 0: 
#                     print(j + 1, end=" ")
#                 elif i == size - 1:  
#                     print(size - j, end=" ")
#                 elif j == 0:  
#                     print(i + 1, end=" ")
#                 elif j == size - 1: 
#                     print(size - i, end=" ")
#                 else:
#                     print(" ", end=" ")
#             print()

#     elif square_type == 2:
#         if size % 2 == 0:
#             print("Type 2 square doesn't support an even number")
#             return

#         for i in range(size):
#             for j in range(size):
#                 if i == j or i + j == size - 1:
#                     print("*", end=" ")
#                 elif i == 0 or j == 0 or i == size - 1 or j == size - 1:
#                     if (i + j) % 2 == 0:
#                         print("*", end=" ")
#                     else:
#                         print("@", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print()


# print("*** Draw square ***")
# user_input = input("Enter type and size: ").split()
# t = int(user_input[0])
# s = int(user_input[1])
# init_square(t, s)
# print("===== End of program =====")

def init_square(square_type, size):
    if square_type == 0:
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    print("*", end=" ")   
                else:
                    print("  ", end="")  
            print()

    elif square_type == 1:
        for i in range(size):
            for j in range(size):
                if i == 0:
                    print(f"{j+1:2}", end=" ")
                elif i == size - 1:  
                    print(f"{size-j:2}", end=" ")
                elif j == 0:
                    print(f"{i+1:2}", end=" ")
                elif j == size - 1: 
                    print(f"{size-i:2}", end=" ")
                else:
                    print("  ", end=" ")
            print()

    elif square_type == 2:
        if size % 2 == 0:
            print("Type 2 square doesn't support an even number")
            return

        for i in range(size):
            for j in range(size):
                if i == j or i + j == size - 1:
                    print("*", end=" ")
                elif i == 0 or j == 0 or i == size - 1 or j == size - 1:
                    if (i + j) % 2 == 0:
                        print("*", end=" ")
                    else:
                        print("@", end=" ")
                else:
                    print("  ", end="")
            print()


print("*** Draw square ***")
user_input = input("Enter type and size: ").split()
t = int(user_input[0])
s = int(user_input[1])
init_square(t, s)
print("===== End of program =====")
