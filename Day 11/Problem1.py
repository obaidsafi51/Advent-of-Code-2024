# Read input from file
def read_input(file_path):
    with open(file_path, 'r') as file:
        return list(map(int, file.read().strip().split()))

# Function to simulate the evolution of stones
def evolve_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left, right = str(stone)[:mid], str(stone)[mid:]
                new_stones.append(int(left))
                new_stones.append(int(right))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones

# Main function
def main():
    input_file = "/home/obaidsafi31/Desktop/Advent-of-Code-2024/Day 11/input.txt"  # Replace with the path to your input file
    stones = read_input(input_file)
    blinks = 25
    
    evolved_stones = evolve_stones(stones, blinks)
    print(f"Number of stones after {blinks} blinks: {len(evolved_stones)}")

if __name__ == "__main__":
    main()