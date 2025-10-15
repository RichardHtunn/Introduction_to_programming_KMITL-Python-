print(" *** Median Mean ***")
data = input("Enter numbers : ").split()

list0 = data[:]   
list1 = []        
list2 = []       

for x in data:
    try:
        n = int(x, 0)   
        list1.append(n)
    except:
        list2.append(x)

print("list0 = ", list0)
print("list1 = ", list1)

if len(list1) > 0:
    mean = 0
    for n in list1:
        mean += n
    mean = mean / len(list1)

    if mean == int(mean):
        print("Mean =", int(mean))
    else:
        print("Mean = %.2f" % mean)


    sorted_list = list1[:]
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp

    print("sort =", sorted_list)

    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

    if median == int(median):
        print("Median =", int(median))
    else:
        print("Median = %.2f" % median)

print("list2 = ", list2)

print("===== End of program =====")