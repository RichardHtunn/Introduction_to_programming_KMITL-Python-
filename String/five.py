print(" *** Center-starting Spiral Rectangle ***")

userInput = input("Enter side direction: ").split()

s = int(userInput[0])        
d = userInput[1].lower() 
start = int(userInput[2]) if len(userInput) == 3 else 1 


m = [[0] * s for _ in range(s)]


move = {
    "up":    (-1, 0),
    "right": (0, 1),
    "down":  (1, 0),
    "left":  (0, -1)
}


o = ["up", "right", "down", "left"]


while o[0] != d:
    o = o[1:] + o[:1]


# r = c = s // 2
r = (s-1)//2
c = (s-1)//2

if s % 2 == 0:
    r = s // 2 - 1
    c = s // 2 - 1

m[r][c] = start


num = start + 1
steps = 1
dir_index = 0

while num < start + s * s:
    for _ in range(2):
        dr, dc = move[o[dir_index]]
        for _ in range(steps):
            if num > start + s * s - 1:
                break
            r += dr
            c += dc
            m[r][c] = num
            num += 1
        dir_index = (dir_index + 1) % 4
    steps += 1

width = len(str(start + s*s - 1))
for row in m:
    print(" ".join(f"{x:>{width}}" for x in row))

print("===== End of program ======")