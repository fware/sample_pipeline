from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # very important creation of graph
        # self.graph = gph

    def add_edge(self, u, v):
        self.graph[u].append(v)  # we need 2D data structure for edge info.

    def bfs(self, s):
        visited = [False for _ in range(max(self.graph) + 1)]

        q = []  # initialize q

        q.append(s)  # add the first node to queue
        visited[s] = True

        while q:
            s = q.pop()
            print(f"{s}")

            for i in self.graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# graph = {
#     0: [1, 2],
#     1: [2],
#     2: [0, 3],
#     3: [3]
#     }
# g = Graph(graph)

start_pt = 2
print(f"Breadth-First Search starting from {start_pt}:")
g.bfs(start_pt)
