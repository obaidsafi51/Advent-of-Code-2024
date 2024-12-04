def read_grid_from_file(file_path):
    """Reads the grid from a file and returns it as a list of strings."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_word(grid, word):
    """Finds all occurrences of a word in the grid in all possible directions."""
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),    # Horizontal right
        (1, 0),    # Vertical down
        (1, 1),    # Diagonal down-right
        (1, -1),   # Diagonal down-left
        (0, -1),   # Horizontal left
        (-1, 0),   # Vertical up
        (-1, -1),  # Diagonal up-left
        (-1, 1)    # Diagonal up-right
    ]
    
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                # Check if the word can fit starting from this position in this direction
                if all(0 <= r + i * dr < rows and
                       0 <= c + i * dc < cols and
                       grid[r + i * dr][c + i * dc] == word[i]
                       for i in range(word_len)):
                    count += 1
    
    return count

# Main execution
if __name__ == "__main__":
    # File containing the word search grid
    input_file = "/home/obaidsafi31/Desktop/Advent-of-Code-2024/Day 4/input.txt"
    # Read the grid from the file
    grid = read_grid_from_file(input_file)
    # Count all occurrences of the word "XMAS"
    total_occurrences = find_word(grid, "XMAS")
    print(f"Total occurrences of 'XMAS': {total_occurrences}")
