class Kruskals:
    def __init__(self, n):
        self.N = n
        self.edges = []
        self.parent_arr = list(range(n + 1))

    def add_edge(self, i, j, weight):
        self.edges.append((i, j, weight))

    def find_parent(self, i):
        if self.parent_arr[i] == i:
            return i

        self.parent_arr[i] = self.find_parent(self.parent_arr[i])
        return self.parent_arr[i]

    def union(self, i, j):
        parent_i = self.find_parent(i)
        parent_j = self.find_parent(j)

        if parent_i != parent_j:
            self.parent_arr[parent_j] = parent_i

    def minimum_spanning_tree(self):
        self.edges.sort(key=lambda x: x[2])  # Sort edges based on price
        mst = []
        for edge in self.edges:
            u, v, weight = edge
            if self.find_parent(u) != self.find_parent(v):
                self.union(u, v)
                mst.append(edge)

            if len(mst) == self.N - 1:
                break

        return mst

N, M = map(int, input().split())

graph = Kruskals(N)

for _ in range(M):
    b_i, b_j, price = map(int, input().split())
    graph.add_edge(b_i, b_j, price)

mst_edges = graph.minimum_spanning_tree()

total_weight = sum(edge[2] for edge in mst_edges)
print("Minimum Spanning Tree Weight:", total_weight)
print("Minimum Spanning Tree Edges:")
for edge in mst_edges:
    print(edge)