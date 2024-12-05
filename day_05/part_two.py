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

def order(sequence):
    ordered_sequence = []
    length = len(sequence)
    j = 0
    while len(ordered_sequence) < length:
        if not sequence[j] in register or not any(number in sequence for number in register[sequence[j]]):
            ordered_sequence = [sequence[j]] + ordered_sequence
            sequence.pop(j)
            j = 0
            continue
        j += 1
    return ordered_sequence
            


while input[i] != "":
    split = [int(x) for x in input[i].split("|")] 
    try: register[split[0]] += [split[1]]
    except: register[split[0]] = [split[1]]
    i += 1

i += 1

while i < len(input):
    sequence = [int(x) for x in input[i].split(",")]
    if not check_validity(sequence): 
        sequence = order(sequence)
        total += sequence[(len(sequence)- 1)//2]
    i += 1

print(f"The middle page numbers of the new correctly ordered updates sum up to {total}")
