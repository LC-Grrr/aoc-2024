input = open("day_12\input.txt", "r").read().splitlines()

directions = [(1,0), (0,1), (-1, 0), (0, -1)]
total = 0

def add_padding(matrix):
    padding_row = ['!' * (len(matrix[0]) + 2)]
    padded_matrix = [f"{'!'}{row}{'!'}" for row in matrix]
    return padding_row + padded_matrix + padding_row

def explore(char, i, j):
    global area, perimeter
    if not input[i][j] == char:
        perimeter += 1
        return
    
    visited.add((i,j))
    global_visited.add((i, j))
    area += 1
    for (dy, dx) in directions:
        if not (i + dy, j + dx) in visited:
            explore(char, i + dy, j + dx)
    

input = [list(line) for line in add_padding(input)]
ignore_list = ["!"]
global_visited = set()

for i in range(len(input)):
    for j in range(len(input[i])):
        if not input[i][j] in ignore_list and not (i, j) in global_visited:
            visited = set()
            area = 0
            perimeter = 0
            explore(input[i][j], i, j)
            total += area * perimeter

print(f"The total price of fencing all the regions is {total}")

