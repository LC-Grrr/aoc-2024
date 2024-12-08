input = open("day_07\input.txt", "r").read().splitlines()
total = 0

def test_true(value, result, terms, operator):
    if len(terms) == 0:
        if value == result:
            return result
        else: return False
    else:
        if operator == "+":
            value += terms[0]
        if operator == "*":
            value *= terms[0]
        return test_true(value, result, terms[1:], "+") or test_true(value, result, terms[1:], "*")
        
for line in input:
    split_line = line.split(" ")
    result, terms = int(split_line[0][:-1]), [int(x) for x in split_line[1:]]
    total += test_true(terms[0], result, terms[1:], "+") or test_true(terms[0], result, terms[1:], "*")

print(f"The total calibration result is {total}")
    



