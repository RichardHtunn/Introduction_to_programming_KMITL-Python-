def generate_spiral(*args):
    h = int(args[0])
    matrix = [[''] * h for _ in range(h)]
    direction = args[1] if len(args) > 1 else 'right'  
    word = args[2] if len(args) > 2 else None 
    
    if h % 2 != 0:
        row, col = h // 2, h // 2
    else:
        if direction == 'right':
            row, col = h // 2 - 1, h // 2 - 1 
        elif direction == 'left':
            row, col = h // 2, h // 2 
        elif direction == 'up':
            row, col = h // 2, h // 2 - 1
        elif direction == 'down':
            row, col = h // 2 - 1, h // 2

    if direction == 'up':
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up -> right -> down -> left
    elif direction == 'down':
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # down -> left -> up -> right
    elif direction == 'left':
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # left -> up -> right -> down
    elif direction == 'right':
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right -> down -> left -> up

    current_direction = 0
    step_size = 1
    total_steps = 0
    steps_in_current_direction = 0
    count = 0
    
    if word:
        word = list(word)
        word_list_iter = []
        current_loop_time = 1
        loop_iter = 0
        for _ in range(h):
            word_list_iter.extend(word)
            loop_iter += 1
            if current_loop_time == loop_iter:
                word = [chr(ord(char) + 1) for char in word]
                current_loop_time += 1
                loop_iter = 0
        iter_count = 0
    else:
        num = 1

    while count < h * h:
        if word:
            matrix[row][col] = word_list_iter[iter_count]
            iter_count += 1
        else:
            matrix[row][col] = str(num)
            num += 1
            
        count += 1
        steps_in_current_direction += 1

        row += directions[current_direction][0]
        col += directions[current_direction][1]

        if steps_in_current_direction == step_size:
            current_direction = (current_direction + 1) % 4
            steps_in_current_direction = 0
            total_steps += 1
            if total_steps % 2 == 0:
                step_size += 1

    return matrix

def print_spiral(matrix):
    max_width = max(len(str(element)) for row in matrix for element in row)
    for row in matrix:
        col_index = 0 
        for element in row:
            if col_index == 0:
                print(f"{element:>{max_width}}", end=" ")
            else: 
                print(f"{element:>{max_width + 1}}", end=" ")
            col_index += 1
        print()

print(" *** Center-starting Spiral Rectangle XXX ***")
inp = input("Enter side [direction] [word] : ")

args = inp.split()

spiral_rectangle = generate_spiral( *args)

print_spiral(spiral_rectangle)

print('===== End of program ======')