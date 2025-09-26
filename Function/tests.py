def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def sortAvoidNegativeNum(arr):
    # collect positive numbers
    positives = []
    for p in arr:
        if p >= 0:
            positives.append(p)

    # sort them
    positives = bubbleSort(positives)

    # rebuild result
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
user_input = list(map(int, input("Enter input : ").split()))
print("Normal sort :")
print(bubbleSort(user_input.copy()))
print("sort avoid negative number : ")
print(sortAvoidNegativeNum(user_input))
