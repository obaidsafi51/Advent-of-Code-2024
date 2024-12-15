def parse_input(file_path):
    """Parses the input file and returns a list of machines."""
    machines = []
    with open(file_path, 'r') as f:
        blocks = f.read().strip().split('\n\n')
        for block in blocks:
            lines = block.split('\n')
            button_a = list(map(int, [lines[0].split('+')[1].split(',')[0], lines[0].split('+')[2]]))  # Extract A values
            button_b = list(map(int, [lines[1].split('+')[1].split(',')[0], lines[1].split('+')[2]]))  # Extract B values
            prize = list(map(int, [lines[2].split('=')[1].split(',')[0], lines[2].split('=')[2]]))     # Extract prize coordinates
            machines.append((button_a, button_b, prize))
    return machines


def calculate_min_cost(machine):
    """Calculates the minimum cost to win a prize for a given machine."""
    (a_x, a_y), (b_x, b_y), (p_x, p_y) = machine

    min_cost = float('inf')
    for a_presses in range(101):
        for b_presses in range(101):
            x_pos = a_presses * a_x + b_presses * b_x
            y_pos = a_presses * a_y + b_presses * b_y

            if x_pos == p_x and y_pos == p_y:
                cost = a_presses * 3 + b_presses * 1
                min_cost = min(min_cost, cost)

    return min_cost if min_cost != float('inf') else None

def solve(file_path):
    """Solves the problem for all machines and returns the total cost."""
    machines = parse_input(file_path)
    total_cost = 0
    prizes_won = 0

    for machine in machines:
        min_cost = calculate_min_cost(machine)
        if min_cost is not None:
            prizes_won += 1
            total_cost += min_cost

    return prizes_won, total_cost

if __name__ == "__main__":
    input_file = "C:\\Users\\Obaid\\Desktop\\Advent of Code\\index.txt"
    prizes_won, total_cost = solve(input_file)
    print(f"Prizes won: {prizes_won}")
    print(f"Total cost: {total_cost}")
