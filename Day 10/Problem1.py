from collections import deque

def parse_map(input_map):
    """Convert the topographic map input into a 2D grid."""
    return [list(map(int, line)) for line in input_map.strip().split("\n")]

def find_trailheads(grid):
    """Find all trailhead positions (height 0)."""
    trailheads = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def bfs_trail(grid, start):
    """Perform BFS to find all reachable 9s from a trailhead."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    reachable_nines = set()

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if (nr, nc) not in visited and grid[nr][nc] == grid[r][c] + 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    if grid[nr][nc] == 9:
                        reachable_nines.add((nr, nc))

    return len(reachable_nines)

def calculate_trailhead_scores(grid):
    """Calculate the total score for all trailheads."""
    trailheads = find_trailheads(grid)
    total_score = 0

    for trailhead in trailheads:
        total_score += bfs_trail(grid, trailhead)

    return total_score

# Read input topographic map from a file
with open("/home/obaidsafi31/Desktop/Advent-of-Code-2024/Day 10/input.txt", "r") as file:
    input_map = file.read()

# Process the map and calculate scores
grid = parse_map(input_map)
total_score = calculate_trailhead_scores(grid)

print("Total score of all trailheads:", total_score)
