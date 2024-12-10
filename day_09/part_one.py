input = open("day_09\input.txt", "r").read()

disk_map = []
space_lengths = []

i = 0
while i < len(input):
    disk_map += [int(input[i]) * [i // 2]]
    try: 
        disk_map += [int(input[i + 1])]
        space_lengths += [int(input[i + 1])]
    except: pass
    i += 2

for j in range(len(space_lengths)):
    if space_lengths[j] > 0: 
        while space_lengths[j] > 0:
            k = len(disk_map) - 1
            while k > 0:
                if space_lengths[j] == 0: break;
                if not isinstance(disk_map[k], int):
                    if space_lengths[j] >= len(disk_map[k]):
                        space_lengths[j] -= len(disk_map[k])
                        if j * 2 == k: 
                            space_lengths[j] = 0
                            break
                        disk_map[j * 2] += disk_map[k]
                        disk_map[k] = ''
                    else:
                        disk_map[j * 2] += disk_map[k][-space_lengths[j]:]
                        disk_map[k] = disk_map[k][:-space_lengths[j]]
                        space_lengths[j] = 0
                k -= 1

disk_map = sum([x for x in disk_map if isinstance(x, list)], [])

total = 0

for i in range(len(disk_map)):
    total += i * disk_map[i]
    
print(f"The resulting filesystem checksum is {total}")


                    
