input = open("day_15\input.txt", "r").read().splitlines()

warehouse_map = []
movements = ""
cur_pos = (0,0)
total = 0

movement_dict = {
    "v": (1, 0),
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1)
}

def find_open_spot(pos, move):
    while True:
        pos = tuple(map(sum, zip(pos, move)))
        pos_value = warehouse_map[pos[0]][pos[1]]
        if pos_value == "#": return False
        elif pos_value == ".": return pos


i = 0
while input[i] != "":
    if "@" in input[i]:
        cur_pos = (i, input[i].index("@"))
    warehouse_map.append(list(input[i]))
    i += 1

i += 1
while i < len(input):
    movements += input[i]
    i += 1

for move in movements:
    destination = tuple(map(sum, zip(cur_pos, movement_dict[move])))
    destination_value = warehouse_map[destination[0]][destination[1]]

    if destination_value == "O":
        open_spot = find_open_spot(destination, movement_dict[move])
        if open_spot:
            warehouse_map[open_spot[0]][open_spot[1]] = "O"
            warehouse_map[destination[0]][destination[1]] = "@"
            warehouse_map[cur_pos[0]][cur_pos[1]] = "."
            cur_pos = destination
    elif destination_value == ".":
        warehouse_map[destination[0]][destination[1]] = "@"
        warehouse_map[cur_pos[0]][cur_pos[1]] = "."
        cur_pos = destination

for i in range(len(warehouse_map)):
    for j in range(len(warehouse_map[i])):
        if warehouse_map[i][j] == "O":
            total += 100 * i + j

print(f"The sum of all boxes' GPS coordinates is {total}")
