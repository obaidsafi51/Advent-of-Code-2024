import re

# File path
file_path = "/home/obaidsafi31/Desktop/Advent-of-Code-2024/Day 3/input.txt"

def calculate_sum_with_conditions(file_path):
    # Read the file content
    with open(file_path, "r") as file:
        data = file.read()
    
    # Regex patterns
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # State to track if mul instructions are enabled
    mul_enabled = True
    total_sum = 0

    # Scan through the file for instructions
    instructions = re.finditer(f"{do_pattern}|{dont_pattern}|{mul_pattern}", data)
    for match in instructions:
        if match.group(0) == "do()":
            mul_enabled = True
        elif match.group(0) == "don't()":
            mul_enabled = False
        else:  # It's a mul(X,Y)
            if mul_enabled:
                x, y = map(int, match.groups())
                total_sum += x * y

    return total_sum

# Calculate and print the result
result = calculate_sum_with_conditions(file_path)
print("Total sum of enabled mul operations:", result)
