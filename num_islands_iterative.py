import collections


class IterativeGraph:

    def __init__(self, r, c, gen_area):
        self.rows = r
        self.cols = c
        self.gen_area = gen_area
        self.visited = set()
        self.num_islands = 0

    def bfs(self, r, c):
        q = collections.deque()  # keep a queue to track of connected components
        q.append((r, c))  # append the coords of the visited cell
        self.visited.add((r, c))  # update the set to signify that we visited this cell

        while q:
            (row, col) = q.popleft()

            neighbors = [[1, -1], [1, 0], [1, 1], [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1]]
            for nr, nc in neighbors:
                r = row + nr
                c = col + nc

                # Check each neighbor to see if it is a connected component.
                if (r in range(rows) and c in range(cols)
                        and (r, c) not in self.visited
                        and self.gen_area[r][c] == 1):
                    q.append((r, c))  # Add a new connected component
                    self.visited.add((r, c))  # Coord is in the queue, so mark it as visited

    def dfs(self, r, c):
        q = collections.deque()  # keep a queue to trace connected components
        self.visited.add((r, c))  # update the set to signify that we visited this cell
        q.append((r, c))  # append the coords of the visited cell

        while q:
            (row, col) = q.pop()

            neighbors = [[1, -1], [1, 0], [1, 1], [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1]]
            for dr, dc in neighbors:
                r = row + dr
                c = col + dc

                # Check each neighbor to see if it is a connected component.
                if (r in range(rows)
                        and c in range(cols)
                        and self.gen_area[r][c] == 1
                        and (r, c) not in self.visited):
                    q.append((r, c))  # Add a new connected component
                    self.visited.add((r, c))  # Coord is in the queue, so mark it as visited

    def num_islands(self):
        if not self.gen_area:
            return 0

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in self.visited and self.gen_area[r][c] == 1:
                    self.bfs(r, c)   # breadth first search
                    # self.dfs(r, c)     # depth first search
                    self.num_islands += 1

        return self.num_islands


full_area = [[1, 1, 0, 0, 1],
             [0, 1, 0, 1, 0],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]

rows = len(full_area)
cols = len(full_area[0])

graph = IterativeGraph(rows, cols, full_area)

print(f"Number of Islands: {graph.num_islands()}")