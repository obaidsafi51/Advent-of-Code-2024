def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split("\n")
    
    # Split into rules and updates
    rules_section = []
    updates_section = []
    for line in lines:
        if "|" in line:
            rules_section.append(line.strip())
        else:
            updates_section.append(line.strip())
    
    # Parse rules
    rules = []
    for rule in rules_section:
        x, y = map(int, rule.split("|"))
        rules.append((x, y))
    
    # Parse updates
    updates = [list(map(int, update.split(","))) for update in updates_section if update]
    
    return rules, updates


def is_update_valid(update, rules):
    positions = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in positions and y in positions:
            if positions[x] > positions[y]:
                return False
    return True


def find_middle_number(update):
    return update[len(update) // 2]


def calculate_sum_of_middle_pages(file_path):
    rules, updates = parse_input(file_path)
    
    valid_updates = []
    for update in updates:
        if is_update_valid(update, rules):
            valid_updates.append(update)
    
    middle_numbers = [find_middle_number(update) for update in valid_updates]
    return sum(middle_numbers)


# File path for input
input_file = "/home/obaidsafi31/Desktop/Advent-of-Code-2024/Day 5/input.txt"  # Replace with the path to your input file

# Calculate the result
result = calculate_sum_of_middle_pages(input_file)
print(f"The sum of the middle page numbers is: {result}")
