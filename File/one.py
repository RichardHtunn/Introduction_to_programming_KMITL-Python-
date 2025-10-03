print(" *** Find Total lines ***")
fname = input("Enter file name : ")

fhand = open(fname, 'r')

print("property =>", fhand)

count = 0
for line in fhand:
    count += 1

print("Total lines :", format(count, ","))

print("===== End of progam =====")
