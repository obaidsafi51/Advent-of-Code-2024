from collections import defaultdict, deque

def read_map_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def get_neighbors(x, y, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            yield nx, ny

def bfs_region_area_and_perimeter(grid, visited, start_x, start_y):
    plant_type = grid[start_x][start_y]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    area = 0
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    while queue:
        x, y = queue.popleft()
        area += 1
        
        for nx, ny in get_neighbors(x, y, rows, cols):
            if grid[nx][ny] == plant_type:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
            else:
                perimeter += 1

        # Check edges for perimeter
        if x == 0 or x == rows - 1:
            perimeter += 1
        if y == 0 or y == cols - 1:
            perimeter += 1

    return area, perimeter

def calculate_total_fence_price(file_path):
    grid = read_map_from_file(file_path)
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    total_price = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                area, perimeter = bfs_region_area_and_perimeter(grid, visited, i, j)
                price = area * perimeter
                total_price += price

    return total_price

if __name__ == "__main__":
    file_path = input("Enter the path to the input file: ").strip()
    total_price = calculate_total_fence_price(file_path)
    print(f"The total price of fencing all regions on the map is: {total_price}")
