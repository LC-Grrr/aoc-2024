input = open("day_09\input.txt", "r").read()

disk_map = []
space_lengths = []

i = 0
while i < len(input):
    disk_map += [int(input[i]) * [i // 2]]
    try: 
        disk_map += [int(input[i + 1]) * ['.']]
        space_lengths += [int(input[i + 1])]
    except: pass
    i += 2

j = len(disk_map) - 1

while j > 0:
    k = 1
    while k < j:
        if disk_map[k].count('.') >= len(disk_map[j]):
            idx = disk_map[k].index('.')
            disk_map[k][idx:len(disk_map[j]) + idx] = [disk_map[j][0]] * len(disk_map[j])
            disk_map[j] = ['.' for elem in disk_map[j]]
            break;
        k += 2
    j -= 2


disk_map = sum([x for x in disk_map if isinstance(x, list)], [])

total = 0
for i in range(len(disk_map)):
    if disk_map[i] == '.': continue
    total += disk_map[i] * i

print(f"The resulting filesystem checksum is {total}")


                    
