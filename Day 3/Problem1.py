import re

# File path
file_path = "/home/obaidsafi31/Desktop/Advent-of-Code-2024/Day 3/input.txt"

def calculate_sum(file_path):
    # Read the file content
    with open(file_path, "r") as file:
        data = file.read()
    
    # Regex to match valid mul(X,Y) patterns
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches
    matches = re.findall(pattern, data)
    
    # Compute the sum of results
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

# Calculate and print the result
result = calculate_sum(file_path)
print("Total sum of all valid mul operations:", result)
