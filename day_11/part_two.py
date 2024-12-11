from functools import lru_cache

input = open("day_11\input.txt", "r").read()

input = [int(x) for x in input.split(' ')]

def split_stone(stone):
    length = len(str(stone))
    mid = 10 ** (length // 2)
    return stone // mid, stone % mid

@lru_cache(None)
def count_splits(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return count_splits(1, blinks - 1)
    if len(str(stone)) % 2 == 0:
        left, right = split_stone(stone)
        return count_splits(left, blinks - 1) + count_splits(right, blinks - 1)
    else:
        return count_splits(stone * 2024, blinks - 1)

total = sum([count_splits(stone, 75) for stone in input])
print(total)

