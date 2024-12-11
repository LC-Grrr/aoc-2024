input = open("day_11\input.txt", "r").read()

input = [int(x) for x in input.split(' ')]

count_splits_cache = {}

def count_splits(stone, blinks):
    key = (stone, blinks)
    return count_splits_cache.setdefault(key, compute_count_splits(stone, blinks))

def compute_count_splits(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return count_splits(1, blinks - 1)
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        parts = [int(stone_str[:len(stone_str) // 2]), int(stone_str[len(stone_str) // 2:])]
        return sum(count_splits(part, blinks - 1) for part in parts)
    else:
        return count_splits(stone * 2024, blinks - 1)

total = sum([count_splits(stone, 25) for stone in input])
print(total)

