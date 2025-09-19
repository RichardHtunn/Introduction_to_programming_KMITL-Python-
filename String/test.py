# print("Hello\nWorld")
# print("Name\tAge\tCountry")
# print("Alice\t25\tUSA")
# print("Bob\t30\tCanada")

# print("\x48\x65\x6c\x6c\x6f")

# print("1, \N{GREEK CAPITAL LETTER DELTA}")
# print("2, \N{BLACK HEART SUIT}")
# print("3, \u03A9")
# print("4, \U0001F600")
# print("5, \101")
# print("6, \141")

# for width in [8,11]:
#     for precision in [2,3,4,5]:
#         print(f'{3.14159:{width}.{precision}}')

n = [3.1514, -42, 1024.0]
for num in n:
    print(f'{num:>+9,.2f}')

for num in n:
    print(f'{num:>-9,.2f}')

for num in n :
    print(f'{num:=+9,.2f}')