import matplotlib.pyplot as plt

def draw_maze(maze, filename="maze.png", path=None):
    
    try:
        rows, cols = maze.rows, maze.cols

        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_aspect('equal')
        ax.axis('off')

        for r in range(rows):
            for c in range(cols):
                cell = maze.grid[r][c]

                x = c
                y = rows - r

                if cell.walls['N']:
                    ax.plot([x, x+1], [y, y], color='black', linewidth=2)
                if cell.walls['S']:
                    ax.plot([x, x+1], [y-1, y-1], color='black', linewidth=2)
                if cell.walls['W']:
                    ax.plot([x, x], [y-1, y], color='black', linewidth=2)
                if cell.walls['E']:
                    ax.plot([x+1, x+1], [y-1, y], color='black', linewidth=2)

        if path:
            for i in range(len(path) - 1):
                r1, c1 = path[i]
                r2, c2 = path[i + 1]

                x1 = c1 + 0.5
                y1 = rows - r1 - 0.5
                x2 = c2 + 0.5
                y2 = rows - r2 - 0.5

                ax.plot([x1, x2], [y1, y2], color='red', linewidth=3)

        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
    except Exception as exc:
        raise RuntimeError(f"Failed to draw maze to '{filename}': {exc}") from exc
