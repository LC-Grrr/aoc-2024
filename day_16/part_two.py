from queue import PriorityQueue

input = open("day_16\input.txt", "r").read().splitlines()

maze = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
max_score = 999999999999
queue = PriorityQueue()
    
for i in range(len(input)):
    if "S" in input[i]:
        start_pos = (i, input[i].index("S"))
        queue.put((0, ([start_pos], 0)))
    maze.append(list(input[i]))

counter = 0
visited = {}
best_paths = set()
potential_paths = set()

while queue.qsize() > 0:
    score, (path, dir_ind) = queue.get()

    if maze[path[-1][0]][path[-1][1]] == "E":
        best_paths |= set(path)
        max_score = score
        break;

    if (path[-1], dir_ind) in visited and visited[(path[-1], dir_ind)] <= score:
        continue

    visited[((path[-1], dir_ind))] = score

    next_pos = tuple(map(sum, zip(path[-1], directions[dir_ind % 4])))

    if maze[next_pos[0]][next_pos[1]] != "#":
        new_path = path.copy()
        new_path += [next_pos]
        queue.put((score + 1, (new_path, dir_ind)))
    
    queue.put((score + 1000, (path.copy(), dir_ind - 1)))
    queue.put((score + 1000, (path.copy(), dir_ind + 1)))

queue.put((0, ([start_pos], 0)))
visited.clear()

while queue.qsize() > 0:
    score, (path, dir_ind) = queue.get()

    if score > max_score: break

    if (path[-1], dir_ind) in visited and visited[(path[-1], dir_ind)] <= score:
        if visited[(path[-1], dir_ind)] == score and path[-1] in best_paths:
            best_paths |= set(path)
        continue

    visited[((path[-1], dir_ind))] = score

    next_pos = tuple(map(sum, zip(path[-1], directions[dir_ind % 4])))

    if maze[next_pos[0]][next_pos[1]] != "#":
        new_path = path.copy()
        new_path += [next_pos]
        queue.put((score + 1, (new_path, dir_ind)))
    
    queue.put((score + 1000, (path.copy(), dir_ind - 1)))
    queue.put((score + 1000, (path.copy(), dir_ind + 1)))


print(f"{len(best_paths)} tiles are part of at least one of the best paths through the maze")

    
    



