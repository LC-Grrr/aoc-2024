input = open("day_04\input.txt", "r").read().splitlines()
XMAS = "XMAS"
count = 0
rows, cols = len(input), len(input[0])
directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

def search(x, y):
    matches_found = 0
    for dx, dy in directions:
        cur_x, cur_y = x, y
        for i in range(4):
            if not (0 <= cur_x < rows and 0 <= cur_y < cols) or input[cur_x][cur_y] != XMAS[i]:
                break
            cur_x += dx
            cur_y += dy
        else:
            matches_found += 1
    return matches_found



for row in range(rows):
    for col in range(cols):
        if input[row][col] == "X":
            count += search(row, col)

print(f"XMAS appears {count} times")
