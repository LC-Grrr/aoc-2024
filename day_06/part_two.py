input = open("day_06\input.txt", "r").read().splitlines()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
solutions = set()
dir_ind = 0
counter = 0

def check_loop(cur_pos, d_ind):    
    max = 0
    while True:      
        max += 1
        if max > 10000: return True
        dy, dx = directions[d_ind % 4]
        if input[cur_pos[0] + dy][cur_pos[1] + dx] == "!":
            return False
        elif input[cur_pos[0] + dy][cur_pos[1] + dx] == "#":
            d_ind += 1   
        else:
            cur_pos = (cur_pos[0] + dy, cur_pos[1] + dx)


def add_padding(matrix):
    padding_row = ['!' * (len(matrix[0]) + 2)]
    padded_matrix = [f"{'!'}{row}{'!'}" for row in matrix]
    return padding_row + padded_matrix + padding_row

for i in range(len(input)):
    for j in range(len(input[i])):
         if input[i][j] == "^":
            pos = (i + 1, j + 1)
            break

input = add_padding(input)
input = [list(string) for string in input]


while True:

    dy, dx = directions[dir_ind % 4]

    if input[pos[0] + dy][pos[1] + dx] == "!":
        break;
    
    next = input[pos[0] + dy][pos[1] + dx]
    input[pos[0] + dy][pos[1] + dx] = "#"
    if check_loop(pos, dir_ind):
        solutions.add((pos[0] + dy, pos[1] + dx))
    input[pos[0] + dy][pos[1] + dx] = next

    if input[pos[0] + dy][pos[1] + dx] == "#":
        dir_ind += 1
    else:
        pos = (pos[0] + dy, pos[1] + dx)
    
    
print(len(solutions))
