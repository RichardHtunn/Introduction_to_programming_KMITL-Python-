print(" *** File Error Handling ***")
try:
    fname, word = input("Enter file name and word : ").split()
    fhand = open(fname, 'r')
except:
    print("Error can not open file =>", fname)
    print("===== End of program =====")
    quit()

total = 0
count = 0
line_sum = 0

for lineno, line in enumerate(fhand, start=1):
    total += 1
    if word in line:
        count += 1
        line_sum += lineno

if count > 0:
    print(f'Number of lines having "{word}" => {count}')
    print("Sum of line number =>", format(line_sum, ","))
print("Total lines =>", format(total, ","))
print("===== End of program =====")
