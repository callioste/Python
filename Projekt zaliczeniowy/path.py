from directions import DIR

def find_path(maze):
    rows, cols = maze.rows, maze.cols
    start = (0, 0)
    goal = (rows - 1, cols - 1)

    stack = [(start, [start])]
    visited = {start}

    while stack:
        (r, c), path = stack.pop()

        if (r, c) == goal:
            return path

        cell = maze.grid[r][c]

        for d, (dr, dc, _) in DIR.items():
            if cell.walls[d]:
                continue

            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    stack.append(((nr, nc), path + [(nr, nc)]))

    return None
