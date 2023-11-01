import collections


class IterGraph:
    def __init__(self, r, hood):
        self.num_homes = r
        self.hood = hood

    def steal_skip_search(self, r):
        total_loot = 0
        q = collections.deque()  # keep queue to track connected homes.
        q.append(r)  # append home coordinates

        while q:
            current_r = q.popleft()
            steal_home_bound = current_r + 2  # locate the "steal home" to steal
            skip_home_bound = current_r + 1   # locate the "skip home" to steal

            steal_first = self.hood[current_r] + self.hood[steal_home_bound]
            skip_first = self.hood[skip_home_bound]

            if steal_first > skip_first:
                max_loot = steal_first
                next_index = steal_home_bound + 2  # jump 2 to skip next home
            else:
                max_loot = skip_first
                next_index = skip_home_bound + 2  # jump 2 to skip the next home

            if next_index < self.num_homes - 1 and next_index is not None:  # Move on to next viable home
                q.append(next_index)
            elif next_index == self.num_homes - 1:  # Are we at the last home?
                max_loot += self.hood[self.num_homes - 1]

            total_loot += max_loot

        return total_loot

    def loot_homes(self, index):
        if not self.hood:
            return 0

        total_loot = self.steal_skip_search(index)
        return total_loot


neighborhood = [3, 1, 2, 1, 2, 4, 8, 5, 4, 8, 1, 3, 1, 5, 7, 8, 7, 1, 6, 9]

rows = len(neighborhood)
first_home_index = 0

g = IterGraph(rows, neighborhood)
print(f"The robbery loot of the neighborhood is: {g.loot_homes(first_home_index)}")
