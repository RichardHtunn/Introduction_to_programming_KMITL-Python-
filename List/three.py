print("*** Minimum Occurrence ***")
nums = input("Enter some numbers: ").split()
nums = [int(x) for x in nums]

min_count = len(nums) + 1
result = None

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    if count < min_count:
        min_count = count
        result = nums[i]

print("==>", result)
print("===== End of program =====")