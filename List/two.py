print(" *** Reverse Even ***")
user_input = input("Enter integers : ").split()

one = []
for x in user_input:
    one.append(int(x))
print(one)

evens = []
for x in one:
    if x % 2 == 0:
        evens.append(x)

evens = evens[::-1]

result = []
ei = 0
for x in one:
    if x % 2 == 0:
        result.append(evens[ei])
        ei += 1
    else:
        result.append(x)

print(result)
print("===== End of program =====")