class Cell:
    def __init__(self):
        self.walls = {
            'N': True,
            'S': True,
            'E': True,
            'W': True
        }

        self.visited = False