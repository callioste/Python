from maze import Maze
import random
from directions import DIR

def dfs(maze):
    stack = [(0, 0)]
    maze.grid[0][0].visited = True

    while stack:
        r, c = stack[-1]
        cell = maze.grid[r][c]

        neighbors = []

        for d, (dr, dc, opposite) in DIR.items():
            nr = r + dr
            nc = c + dc

            if 0 <= nr < maze.rows and 0 <= nc < maze.cols:
                if not maze.grid[nr][nc].visited:
                    neighbors.append((d, nr, nc, opposite))

        if neighbors:
            d, nr, nc, opposite = random.choice(neighbors)

            cell.walls[d] = False
            maze.grid[nr][nc].walls[opposite] = False

            maze.grid[nr][nc].visited = True
            stack.append((nr, nc))
        else:
            stack.pop()

    maze.grid[0][0].walls['W'] = False
    maze.grid[maze.rows - 1][maze.cols - 1].walls['E'] = False

    return maze