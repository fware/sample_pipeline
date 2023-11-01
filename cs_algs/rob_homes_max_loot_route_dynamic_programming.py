import collections


class IterGraph:
    def __init__(self, r, c, hood):
        self.rows = r
        self.cols = c
        self.num_homes = r * c
        self.hood = hood
        self.visited = set()
        self.total_loot = 0

    def max_loot_path_search(self, r, c):
        q = collections.deque()  # keep queue to track connected homes.
        q.append((r, c))  # append home coordinates
        self.visited.add((r, c))  # update the set of visited homes
        self.total_loot += self.hood[r][c]  # Add the first looted home.  It is iterative, so have to add now.

        while q:
            max_loot = 0
            current_r = None
            current_c = None

            (row, col) = q.popleft()

            neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for nr, nc in neighbors:
                r = row + nr  # point to the neighbor location
                c = col + nc

                # check each viable neighbor
                if (r in range(self.rows)
                        and c in range(self.cols)
                        and (r, c) not in self.visited):

                    self.visited.add((r, c))

                    if self.hood[r][c] > max_loot:
                        max_loot = self.hood[r][c]
                        current_r = r
                        current_c = c

            if len(self.visited) < self.num_homes:
                q.append((current_r, current_c))
            self.total_loot += max_loot

    def loot_homes(self):
        if not self.hood:
            return 0

        self.max_loot_path_search(0, 0)
        return self.total_loot


neighborhood = [[3, 1, 2, 1, 2],
                [4, 8, 5, 4, 8],
                [1, 3, 1, 5, 7],
                [8, 7, 1, 6, 9]]

rows = len(neighborhood)
cols = len(neighborhood[0])

g = IterGraph(rows, cols, neighborhood)
print(f"The robbery loot of the neighborhood is: {g.loot_homes()}")
