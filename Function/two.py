def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr

def sortAvoidNegativeNum(arr):
    positives = []
    for p in arr:
        if p >= 0:
            positives.append(p)
        
    positives = bubbleSort(positives)

    result = []
    position = 0
    for num in arr:
        if num < 0:
            result.append(num)
        else:
            result.append(positives[position])
            position += 1
    return result

print("*** Sort avoid negative number ***")
user_input = input("Enter Input : ").split()
user_input_list = []
for i in user_input:
    user_input_list.append(int(i))

print("Normal sort :")
print(bubbleSort(user_input_list.copy()))
print("sort avoid negative number : ")
print(sortAvoidNegativeNum(user_input_list))

print("===== End of program =====")