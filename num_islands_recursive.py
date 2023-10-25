# Program to count islands in boolean 2D matrix
class Graph:

    def __init__(self, r, c, g):
        self.ROW = r
        self.COL = c
        self.graph = g

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def in_range(self, i, j, visited):
        # to be True:
        # row number is in range,
        # column number is in range,
        # visited is False
        # graph cell is 1
        return (0 <= i < self.ROW and
                0 <= j < self.COL and
                not visited[i][j] and self.graph[i][j])

    # A utility function to do DFS for a 2D
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices

    def dfs(self, i, j, visited):

        # These arrays are used to get row and
        # column numbers of 8 neighbours
        # of a given cell
        neighbors = [(-1, -1), (-1, 0), (-1, -1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        # Mark this cell as visited
        visited[i][j] = True

        # Recurse for all connected neighbours
        for (m, n) in neighbors:
            if self.in_range(i + m, j + n, visited):  # Check the cell for first visit
                self.dfs(i + m, j + n, visited)

    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix

    def countIslands(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize num_islands as 0 and traverse
        # through the all cells of given matrix
        num_islands = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island num_islands once finished with the search.
                    self.dfs(i, j, visited)
                    num_islands += 1

        return num_islands


graph = [[1, 1, 0, 0, 1],
         [0, 1, 0, 1, 0],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

row = len(graph)
col = len(graph[0])

graph = Graph(row, col, graph)

print("Number of islands is:")
print(graph.countIslands())
