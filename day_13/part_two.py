import re
import numpy as np

input = open("day_13\input.txt", "r").read().split("\n\n")
total = 0

def is_roundable(nr):
    closest_int = round(nr)
    return ((abs(nr - closest_int) <= 0.01) or (abs(closest_int - nr) <= 0.01))

for claw_machine in input:
    numbers = [int(x) for x in re.findall('\d+', claw_machine)]
    coeffs = np.array([[numbers[0], numbers[2]], [numbers[1], numbers[3]]])
    results = np.array([numbers[-2] + 10000000000000, numbers[-1] + 10000000000000])
    A, B = np.linalg.solve(coeffs, results)
    if is_roundable(A) and is_roundable(B):
        total += 3 *round(A) + round(B)
    
    
print(f"To win all prizes you would need to spend a total of {total} tokens")

