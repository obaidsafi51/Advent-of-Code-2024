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


def topological_sort(pages, rules):
    from collections import defaultdict, deque
    
    # Build adjacency list and in-degree count
    graph = defaultdict(list)
    in_degree = {page: 0 for page in pages}
    
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
    
    # Perform topological sort
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []
    
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages


def reorder_updates(updates, rules):
    reordered_updates = []
    for update in updates:
        reordered_updates.append(topological_sort(update, rules))
    return reordered_updates


def find_middle_number(update):
    return update[len(update) // 2]


def calculate_sum_of_middle_pages_part_two(file_path):
    rules, updates = parse_input(file_path)
    
    valid_updates = []
    invalid_updates = []
    
    for update in updates:
        if is_update_valid(update, rules):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    
    # Reorder invalid updates
    reordered_updates = reorder_updates(invalid_updates, rules)
    
    # Find middle numbers
    middle_numbers = [find_middle_number(update) for update in reordered_updates]
    return sum(middle_numbers)


# File path for input
input_file = "/home/obaidsafi31/Desktop/Advent-of-Code-2024/Day 5/input.txt"  # Replace with the path to your input file

# Calculate the result
result = calculate_sum_of_middle_pages_part_two(input_file)
print(f"The sum of the middle page numbers after reordering is: {result}")
