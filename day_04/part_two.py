input = open("day_04\input.txt", "r").read().splitlines()
count = 0
rows, cols = len(input), len(input[0])
directions = [
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

def search(x, y):
    m_count, s_count = 0, 0
    for dx, dy in directions:
        cur_x, cur_y = x + dx, y + dy
        if not (0 <= cur_x < rows and 0 <= cur_y < cols):
            break
        elif input[cur_x][cur_y] == "M": m_count += 1
        elif input[cur_x][cur_y] == "S": s_count += 1
        else: break
    return m_count >= 2 and s_count >= 2



for row in range(rows):
    for col in range(cols):
        if input[row][col] == "A":
            if search(row, col):
                count += 1

print(f"X-MAS appears {count} times")
