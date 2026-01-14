from maze import Maze
from generator import dfs
from path import find_path
from render import draw_maze

maze = Maze(20, 20)
dfs(maze)

path = find_path(maze)
draw_maze(maze, path=path, filename="maze.png")