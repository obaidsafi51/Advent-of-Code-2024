def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Parse the grid
    grid = []
    moves = ""
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            grid.append(list(line))
        elif line:
            moves += line

    return grid, moves

def find_robot(grid):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '@':
                return r, c

    return None

def move_robot(grid, moves):
    rows = len(grid)
    cols = len(grid[0])

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    robot_pos = find_robot(grid)

    for move in moves:
        dr, dc = directions[move]
        new_r, new_c = robot_pos[0] + dr, robot_pos[1] + dc

        if not (0 <= new_r < rows and 0 <= new_c < cols):
            continue  # Skip move if out of bounds

        if grid[new_r][new_c] == '.':  # Move robot to empty space
            grid[robot_pos[0]][robot_pos[1]] = '.'
            grid[new_r][new_c] = '@'
            robot_pos = (new_r, new_c)

        elif grid[new_r][new_c] == 'O':  # Push the box if possible
            box_r, box_c = new_r + dr, new_c + dc
            if 0 <= box_r < rows and 0 <= box_c < cols and grid[box_r][box_c] == '.':
                grid[robot_pos[0]][robot_pos[1]] = '.'
                grid[new_r][new_c] = '@'
                grid[box_r][box_c] = 'O'
                robot_pos = (new_r, new_c)

    return grid

def calculate_gps_sum(grid):
    gps_sum = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'O':
                gps_sum += 100 * r + c

    return gps_sum

def main(file_path):
    grid, moves = read_input(file_path)
    moves = moves.replace("\n", "")  # Ensure moves are continuous without unintended line breaks
    final_grid = move_robot(grid, moves)
    gps_sum = calculate_gps_sum(final_grid)
    return gps_sum

if __name__ == "__main__":
    file_path = input("Enter the path to the input file: ").strip()
    result = main(file_path)
    print(f"The sum of all boxes' GPS coordinates is: {result}")
