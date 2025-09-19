# print(" *** String Diamond ***")

# word = input("Enter string : ")

# length = len(word)
# mid = length // 2
# for i in range(mid):
#     substring = word[mid - i: mid + i + 1]
#     for s in range(mid - i):
#         print(" ", end="")
#     print(substring)

# print(word)

# for i in range(mid - 1, -1, -1):
#     substring = word[mid - i: mid + i + 1]
#     for s in range(mid - i):
#         print(" ", end="")
#     print(substring)

# print("===== End of program =====")

# print(" *** String Diamond ***")

# word = input("Enter string : ")
# length = len(word)

# if length % 2 == 0:
#     mid1 = length // 2 - 1
#     mid2 = length // 2
#     upper_start = [(mid1, mid2)]
# else:
#     mid = length // 2
#     upper_start = [(mid, mid)]

# i = 1
# while True:
#     start, end = upper_start[-1]

#     new_start = start - 1
#     new_end = end + 1
#     if new_start < 0 or new_end >= length:
#         break
#     upper_start.append((new_start, new_end))


# for start, end in upper_start:

#     spaces = (length - (end - start + 1)) // 2
#     for s in range(spaces):
#         print(" ", end="")

#     for k in range(start, end + 1):
#         print(word[k], end="")
#     print()


# print(word)


# for start, end in reversed(upper_start):
#     spaces = (length - (end - start + 1)) // 2
#     for s in range(spaces):
#         print(" ", end="")

#     for k in range(start, end + 1):
#         print(word[k], end="")
#     print()

# print("===== End of program =====")

print(" *** String Diamond ***")

w = input("Enter string : ")
n = len(w)

# odd or even middle
if n % 2 == 1:  
    start = end = n // 2
else:  
    start = n // 2 - 1
    end = n // 2

# top half (including middle line)
while start >= 0 and end < n:
    piece = w[start:end+1]
    print(" " * start + piece)
    start -= 1
    end += 1

# bottom half
start += 2
end -= 2
while start <= (n // 2 if n % 2 else n // 2 - 1):
    piece = w[start:end+1]
    print(" " * start + piece)
    start += 1
    end -= 1

print("===== End of program =====")