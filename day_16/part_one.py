from queue import PriorityQueue

input = open("day_16\input.txt", "r").read().splitlines()

maze = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
score = 0
queue = PriorityQueue()
    
for i in range(len(input)):
    if "S" in input[i]:
        queue.put((0, ((i, input[i].index("S")), 0)))
    maze.append(list(input[i]))

visited = {}

while queue.qsize() > 0:
    score, (pos, dir_ind) = queue.get()
    if maze[pos[0]][pos[1]] == "E":
        total = score
        break

    if (pos, dir_ind) in visited and visited[(pos, dir_ind)] <= score:
        continue

    visited[((pos, dir_ind))] = score

    next_pos = tuple(map(sum, zip(pos, directions[dir_ind % 4])))

    if maze[next_pos[0]][next_pos[1]] != "#":
        queue.put((score + 1, (next_pos, dir_ind)))
    
    queue.put((score + 1000, (pos, dir_ind - 1)))
    queue.put((score + 1000, (pos, dir_ind + 1)))

print(f"The lowest score a reindeer could possible get is {total}")

    
    



