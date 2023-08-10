from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


    def bfs_tree(self, start):
        visited = set()
        queue = deque([start])

        bfs_tree = {}

        while queue:
            node = queue.popleft()
            visited.add(node)

            bfs_tree[node] = []

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    bfs_tree[node].append(neighbor)

        return bfs_tree

N, M = map(int, input().split())
graph = Graph()

for _ in range(M):
    u, v = map(int, input().split())
    #graph.add_edge(u)
    #graph.add_edge(v)
    graph.add_edge(u, v)


start_node = 7
bfs_tree = graph.bfs_tree(start_node)

print("BFS Tree:")
for node, neighbors in bfs_tree.items():
    print(node, "->", neighbors)