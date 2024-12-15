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

def move_horizontally(pos, move):
    while True:
        pos = tuple(map(sum, zip(pos, move)))
        pos_value = warehouse_map[pos[0]][pos[1]]
        if pos_value == "#": return False
        elif pos_value == ".":
            if move[1] == 1:
               warehouse_map[pos[0]][pos[1]] = "]" 
            else: warehouse_map[pos[0]][pos[1]] = "[" 

            while warehouse_map[pos[0]][pos[1] - move[1]] != "@":
                pos = (pos[0], pos[1] - move[1])
                warehouse_map[pos[0]][pos[1]] = "]" if warehouse_map[pos[0]][pos[1]] == "[" else "["
            return True

def move_vertically(positions, move):
    involved_boxes = set(positions)
    next_positions = set(positions)
    while True:
        involved_boxes |= next_positions
        if len(next_positions) == 0:
            boxes_dict = {(x,y): warehouse_map[x][y] for (x,y) in involved_boxes}
            for box in involved_boxes:
                if not (box[0] - move[0], box[1]) in boxes_dict:
                    warehouse_map[box[0]][box[1]] = "."
                warehouse_map[box[0] + move[0]][box[1]] = boxes_dict[box]
            return True
        positions = next_positions.copy()
        next_positions.clear() 
        for pos in positions:
            next_pos = tuple(map(sum, zip(pos, move)))
            next_pos_value = warehouse_map[next_pos[0]][next_pos[1]]
            if next_pos_value == "[":
                next_positions.add(next_pos)
                next_positions.add((next_pos[0], next_pos[1] + 1))
            elif next_pos_value == "]":
                next_positions.add(next_pos)
                next_positions.add((next_pos[0], next_pos[1] - 1))
            elif next_pos_value == "#":
                return False


i = 0
while input[i] != "":
    modified_input = []
    for char in input[i]:
        if char == "#":
            modified_input += ["#", "#"]
        elif char == "O":
            modified_input += ["[", "]"]
        elif char == ".":
            modified_input += [".", "."]
        else:
            modified_input += ["@", "."]
            cur_pos = (i, modified_input.index("@"))

    warehouse_map.append(modified_input)
    i += 1

i += 1
while i < len(input):
    movements += input[i]
    i += 1

for move in movements:
    destination = tuple(map(sum, zip(cur_pos, movement_dict[move])))
    destination_value = warehouse_map[destination[0]][destination[1]]

    if destination_value == "[" or destination_value == "]":
        if move == "<" or move == ">":
            open_spot = move_horizontally(destination, movement_dict[move])
        else:
            if destination_value == "[":
                open_spot = move_vertically([destination, (destination[0], destination[1] + 1)], movement_dict[move])
            else: open_spot = move_vertically([destination, (destination[0], destination[1] - 1)], movement_dict[move])
        if open_spot:
            warehouse_map[destination[0]][destination[1]] = "@"
            warehouse_map[cur_pos[0]][cur_pos[1]] = "."
            cur_pos = destination
    elif destination_value == ".":
        warehouse_map[destination[0]][destination[1]] = "@"
        warehouse_map[cur_pos[0]][cur_pos[1]] = "."
        cur_pos = destination

for i in range(len(warehouse_map)):
    for j in range(len(warehouse_map[i])):
        if warehouse_map[i][j] == "[":
            total += 100 * i + j

print(f"The sum of all boxes' final GPS coordinates is {total}")
