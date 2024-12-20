import re
import numpy as np

input = open("day_13\input.txt", "r").read().split("\n\n")
total = 0

def is_valid_and_roundable(nr):
    closest_int = round(nr)
    return ((abs(nr - closest_int) <= 0.01) or (abs(closest_int - nr) <= 0.01)) and 0 <= nr <= 100

for claw_machine in input:
    numbers = [int(x) for x in re.findall('\d+', claw_machine)]
    coeffs = np.array([[numbers[0], numbers[2]], [numbers[1], numbers[3]]])
    results = np.array(numbers[-2:])
    A, B = np.linalg.solve(coeffs, results)
    if is_valid_and_roundable(A) and is_valid_and_roundable(B):
        total += 3 *round(A) + round(B)
    
    
print(f"To win the prizes you would need to spend a total of {total} tokens")

