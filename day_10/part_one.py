input = open("day_10\input.txt", "r").read().splitlines()

total = 0
directions = [(1,0), (0,1), (-1, 0), (0, -1)]

def add_padding(matrix):
    padding_row = ['!' * (len(matrix[0]) + 2)]
    padded_matrix = [f"{'!'}{row}{'!'}" for row in matrix]
    return padding_row + padded_matrix + padding_row

def expand(pos, value):
    if value == 9: visited.add(pos)
    else:
        for (dy, dx) in directions:
            if input[pos[0] + dy][pos[1] + dx] == str(value + 1):
                expand((pos[0] + dy,pos[1] + dx), value +1)

input = add_padding(input)

for i in range(len(input)):
    for j in range(len(input[i])):
        visited = set()
        if not input[i][j] == "0":
            continue
        expand((i,j), 0)
        total += len(visited)
        

print(f"The sum of the scores of all trailheads is {total}")