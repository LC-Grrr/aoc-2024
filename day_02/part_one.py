input = open("day_02\input.txt", "r")

counter = 0

for line in input:
    line = [int(x) for x in line.strip().split()]
    
    difference_constraint = all(1 <= abs(line[i] - line[i + 1]) <= 3 for i in range(len(line) - 1))
    
    is_increasing = all(line[i] < line[i + 1] for i in range(len(line) - 1))
    is_decreasing = all(line[i] > line[i + 1] for i in range(len(line) - 1))
    
    if (is_increasing or is_decreasing) and difference_constraint: counter += 1

print(counter)


