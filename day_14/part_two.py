input = open("day_14\input.txt", "r").read().splitlines()
import re

DIMS = [101, 103]
vector_dict = {}

def apply_vector(vector, positions):
    new_positions = []
    for pos in positions:
        for j in range(2):
            pos[j] += vector[j]
            if pos[j] < 0:
                pos[j] = DIMS[j] + pos[j]
            elif pos[j] >= DIMS[j]:
                pos[j] = pos[j] - DIMS[j]
        new_positions.append(pos)
        currently_occupied.add((pos[0], pos[1]))
    return new_positions

for line in input:
    numbers = [int(x) for x in re.findall('-?\d+', line)]
    try: vector_dict[(numbers[2], numbers[3])] += [[numbers[0], numbers[1]]]
    except: vector_dict[(numbers[2], numbers[3])] = [[numbers[0], numbers[1]]]

i = 1
while True:
    currently_occupied = set()
    for vector in vector_dict:
        vector_dict[vector] = apply_vector(vector, vector_dict[vector])
    if len(currently_occupied) == len(input):
        break
    i += 1

print(f"{i} seconds elapse before the robots display the easter egg")




