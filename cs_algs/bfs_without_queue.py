# Function to find the distance
# from the source to other nodes
def BFS(curr, N, vis, dp, v, adj):
    while (curr <= N):

        # Current node
        node = v[curr - 1]
        print(node, end=", ")

        for i in range(len(adj[node])):

            # Adjacent node
            next = adj[node][i]

            if ((not vis[next]) and (dp[next] < dp[node] + 1)):
                # Stores the adjacent node
                v.append(next)

                # Increases the distance
                dp[next] = dp[node] + 1

                # Mark it as visited
                vis[next] = True

        curr += 1


# Function to print the distance
# from source to other nodes
def bfsTraversal(adj, N, source):
    # Initially mark all nodes as false
    vis = [False] * (N + 1)

    # Initialize distance array with 0
    dp = [0] * (N + 1);
    v = []

    v.append(source)

    # Initially mark the starting
    # source as 0 and visited as true
    dp = 0
    vis = True

    # Call the BFS function
    BFS(1, N, vis, dp, v, adj)


# Driver code
if __name__ == '__main__':
    # No. of nodes in graph
    N = 4

    # Creating adjacency list
    # for representing graph
    adj = [[] for _ in range(N + 1)]
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[2].append(0)
    adj[2].append(3)
    adj[3].append(3)

    # Following is BFS Traversal
    # starting from vertex 2
    bfsTraversal(adj, N, 2)
