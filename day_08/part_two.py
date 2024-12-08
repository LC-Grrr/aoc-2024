input = open("day_08\input.txt", "r").read().splitlines()

column_length = len(input)
row_length = len(input[0])

antenna_map = {}
antinodes = set()

for i in range(column_length):
    for j in range(row_length):
        if not input[i][j] == ".":
            try: antenna_map[input[i][j]] += [(i, j)]
            except: antenna_map[input[i][j]] = [(i, j)]

for frequency in antenna_map:
    antennas = antenna_map[frequency]
    while len(antennas) > 1:
        test_antenna = antennas[0]
        for antenna in antennas[1:]:
            dy = test_antenna[0] - antenna[0]
            dx = test_antenna[1] - antenna[1]
            possible_antinode1 = test_antenna
            possible_antinode2 = antenna
            while all(0 <= possible_antinode1[i] < dim for i, dim in enumerate([column_length, row_length])):
                antinodes.add(possible_antinode1)
                possible_antinode1 = (possible_antinode1[0] + dy, possible_antinode1[1] + dx)
            while all(0 <= possible_antinode2[i] < dim for i, dim in enumerate([column_length, row_length])):
                 antinodes.add(possible_antinode2)
                 possible_antinode2 = (possible_antinode2[0] - dy, possible_antinode2[1] - dx)                 
        del antennas[0]

print(f"There's {len(antinodes)} unique locations containing an antinode")
    