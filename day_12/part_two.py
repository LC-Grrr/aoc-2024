input = open("day_12\input.txt", "r").read().splitlines()

directions = [(1,0), (0,1), (-1, 0), (0, -1)]
total = 0

def add_padding(matrix):
    padding_row = ['!' * (len(matrix[0]) + 2)]
    padded_matrix = [f"{'!'}{row}{'!'}" for row in matrix]
    return padding_row + padded_matrix + padding_row

def explore(char, i, j):
    global area, sides   
    visited.add((i,j))
    global_visited.add((i,j))
    area += 1
    for (dy,dx) in directions:
        if input[i + dy][j + dx] != char:
            sides += [((dy,dx), (i,j))]
        elif not (i + dy, j + dx) in visited:
            explore(char, i + dy, j + dx)

def calculate_sides(sides):
    unique_sides = 0
    while len(sides) > 0:
        current_side = sides[0]
        sides = explore_side(current_side, sides[0:])
        unique_sides += 1
        if current_side in sides: sides.remove(current_side)
    return unique_sides
        
def explore_side(side, sides):
    if side[0] == (1, 0) or side[0] == (-1, 0):
        targets = [(side[0], (side[1][0], side[1][1] - 1)), (side[0], (side[1][0], side[1][1] + 1))]
        for target in targets:
            if target in sides:
                sides.remove(target)
                sides = explore_side(target, sides)
    elif side[0] == (0, 1) or side[0] == (0, -1):
        targets = [(side[0], (side[1][0] + 1, side[1][1])), (side[0], (side[1][0] - 1, side[1][1]))]
        for target in targets:
            if target in sides:
                sides.remove(target)
                sides = explore_side(target, sides)
    return sides
            
input = [list(line) for line in add_padding(input)]
global_visited = set()

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] != "!" and not (i, j) in global_visited:
            visited = set()
            area = 0
            sides = []
            explore(input[i][j], i, j)
            total += area * calculate_sides(sides)
print(f"The total price of fencing all the regions is {total}")

