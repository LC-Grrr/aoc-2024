input = open("day_01\input.txt", "r")

similarity_score = 0
left_list = []
right_list = []

for line in input:
    values = [x for x in line.strip().split()]
    left_list += [int(values[0])]
    right_list += [int(values[1])]
    
set(left_list)

for target in left_list:
    for i in range(len(right_list)):
        if right_list[i] == target:
            similarity_score += target


print(f"The similarity score between the lists is {similarity_score}")


