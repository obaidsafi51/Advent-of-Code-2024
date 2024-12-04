def read_grid_from_file(file_path):
    """Reads the grid from a file and returns it as a list of strings."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def count_xmas_patterns(grid):
    """Counts all occurrences of the X-MAS pattern in the grid."""
    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(1, rows - 1):  # Avoid grid edges
        for c in range(1, cols - 1):  # Avoid grid edges
            if grid[r][c] == 'A':  # 'A' is the center of the X-MAS pattern
                # Check the top-left, center (A), and bottom-right diagonal for MAS (M → A → S)
                if (grid[r-1][c-1] == 'M' and grid[r][c] == 'A' and grid[r+1][c+1] == 'S') or \
                   (grid[r-1][c-1] == 'S' and grid[r][c] == 'A' and grid[r+1][c+1] == 'M'):
                    # Check the top-right, center (A), and bottom-left diagonal for MAS (M → A → S)
                    if (grid[r-1][c+1] == 'M' and grid[r][c] == 'A' and grid[r+1][c-1] == 'S') or \
                       (grid[r-1][c+1] == 'S' and grid[r][c] == 'A' and grid[r+1][c-1] == 'M'):
                        count += 1

    return count

# Main execution
if __name__ == "__main__":
    # File containing the word search grid
    input_file = "/home/obaidsafi31/Desktop/Advent-of-Code-2024/Day 4/input.txt"
    # Read the grid from the file
    grid = read_grid_from_file(input_file)
    # Count all occurrences of the X-MAS pattern
    total_occurrences = count_xmas_patterns(grid)
    print(f"Total occurrences of 'X-MAS': {total_occurrences}")
