input = open("day_06\input.txt", "r").read().splitlines()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_ind = 0
counter = 0

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

while True:
    dy, dx = directions[dir_ind % 4]
    if input[pos[0] + dy][pos[1] + dx] == "!":
        if input[pos[0]][pos[1]] == "." or input[pos[0]][pos[1]] == "^":
            input[pos[0]] = input[pos[0]][:pos[1]] + "X" + input[pos[0]][pos[1] + 1:]
            counter += 1
        break;
    elif input[pos[0] + dy][pos[1] + dx] == "#":
        dir_ind += 1
    else:
        if input[pos[0]][pos[1]] == "." or input[pos[0]][pos[1]] == "^":
            input[pos[0]] = input[pos[0]][:pos[1]] + "X" + input[pos[0]][pos[1] + 1:]
            counter += 1
        pos = (pos[0] + dy, pos[1] + dx)
    
    
print(counter)
