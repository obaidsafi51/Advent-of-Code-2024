
# Function to check if a report is safe
def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are between 1 and 3 or -1 and -3
    if all(1 <= diff <= 3 for diff in differences):
        return True  # Increasing
    if all(-3 <= diff <= -1 for diff in differences):
        return True  # Decreasing
    
    return False  # Not safe

# Function to check if a report is safe with the Problem Dampener
def is_safe_with_dampener(report):
    if is_safe(report):
        return True  # Already safe

    # Check if removing one level makes the report safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the i-th level
        if is_safe(modified_report):
            return True  # Safe after removing one level

    return False  # Not safe even with dampener

# Read the dataset from a file
def read_dataset(file_path):
    with open(file_path, 'r') as file:
        # Parse each line into a list of integers
        return [list(map(int, line.split())) for line in file]

# Path to your dataset file
file_path = '/home/obaidsafi31/Desktop/Advent-of-Code-2024/Day 2/input.txt'

# Read and process the dataset
data = read_dataset(file_path)

# Count the number of safe reports
safe_reports_with_dampener = sum(is_safe_with_dampener(report) for report in data)

# Output the result
print(f"Number of safe reports with the Problem Dampener: {safe_reports_with_dampener}")
