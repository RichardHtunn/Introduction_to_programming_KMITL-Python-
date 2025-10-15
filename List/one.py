print(" *** Sum odd / Subtract even ***")
numbers = input("Enter numbers : ")

numbers_str = numbers.split()

numbers_list = []
numbers_list_odd = []
numbers_list_even = []
for n in numbers_str:
    numbers_list.append(int(n))

for num in numbers_list:
    if num == -1:
        break
    else:
        if num % 2 == 0:
            numbers_list_even.append(num)
        else:
            numbers_list_odd.append(num)

sumOne = sum(numbers_list_even)
sumTwo = sum(numbers_list_odd)

sumTh = sumTwo - sumOne

print(f"Sum is {sumTh:,}")
print("===== End of program =====")

