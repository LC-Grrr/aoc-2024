import re

input = open("day_03\input.txt", "r").read()

total = 0

matches = re.findall(r"mul\(\d+,\d+\)", input)
for match in matches:
    numbers = re.findall(r'\d+', match)
    total += int(numbers[0]) * int(numbers[1])

print(f"The total result after adding all the multiplications is {total}")