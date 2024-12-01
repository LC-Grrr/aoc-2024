input = open("day_01\input.txt", "r")

distance = 0
left_list = []
right_list = []

for line in input:
    values = [x for x in line.strip().split()]
    left_list += [int(values[0])]
    right_list += [int(values[1])]
    
left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    distance += abs(left_list[i] - right_list[i])

print(f"The total distance between the lists is {distance}")


