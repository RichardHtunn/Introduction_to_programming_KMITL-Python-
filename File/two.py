print(" *** Find Empty lines ***")
fname = input("Enter file name : ")

fhand = open(fname, 'r')

total = 0
empty = 0

for line in fhand:
    total += 1
    if line.strip() == "":
        empty += 1

print("Empty lines =>", empty)
print("Total lines =>", total)
