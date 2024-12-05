input = open("day_05\input.txt", "r").read().splitlines()
i = 0
total = 0
register = {}

def check_validity(sequence):
    for i in range(len(sequence)):
        if sequence[i] in register:
            if any(number in register[sequence[i]] for number in sequence[:i]):
                return False
    return True

while input[i] != "":
    split = [int(x) for x in input[i].split("|")] 
    try: register[split[0]] += [split[1]]
    except: register[split[0]] = [split[1]]
    i += 1

i += 1

while i < len(input):
    sequence = [int(x) for x in input[i].split(",")]
    if check_validity(sequence): total += sequence[(len(sequence)- 1)//2]
    i += 1

print(f"The middle page numbers of the correctly ordered updates sum up to {total}")
