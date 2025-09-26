print("*** Permutation ***")

def permutation(str1,str2):
    return sorted(str1) == sorted(str2)

user_input = input("Enter two strings: ").split("/")
str1, str2 = user_input[0], user_input[1]

if permutation(str1,str2):
    print("String1 and String2 are permutation")
else:
    print("String1 and String2 are not permutation")

print("===== End of program =====")