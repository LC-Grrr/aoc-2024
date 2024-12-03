import re

input = open("day_03\input.txt", "r").read()

total = 0

split = input.split("do")
for do in split:
    if do[:3] == "n't": continue
    else:
        matches = re.findall(r"mul\(\d+,\d+\)", do)
        for match in matches:
            numbers = re.findall(r'\d+', match)
            total += int(numbers[0]) * int(numbers[1])
            
print(f"The total result after adding all the enabled multiplications is {total}")