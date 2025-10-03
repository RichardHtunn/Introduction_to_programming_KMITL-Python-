print(" *** Find number of lines for specific word ***")
fname, word = input("Enter file name and word : ").split()

fhand = open(fname, 'r')

total = 0
count = 0

for line in fhand:
    total += 1
    if word in line:
        count += 1

print(f'Number of lines having "{word}" => {count}')
print("Total lines =>", total)
