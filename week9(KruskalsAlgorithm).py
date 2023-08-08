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

    def minimum_spanning_tree_weight(self):
        self.edges.sort(key=lambda x: x[2])  # Sort edges based on price
        mst = []
        total_weight = 0
        for edge in self.edges:
            u, v, weight = edge
            if self.find_parent(u) != self.find_parent(v):
                self.union(u, v)
                mst.append(edge)
                total_weight += weight

            if len(mst) == self.N - 1:
                break

        return total_weight


N, M = map(int, input().split())

graph = Kruskals(N)

for _ in range(M):
    b_i, b_j, price = map(int, input().split())
    graph.add_edge(b_i, b_j, price)

print(graph.minimum_spanning_tree_weight())

''' Union with balanced tree
    self.ranks = [0] * (n + 1)

    def union(self, i, j):
        root1 = self.find_parent(i)
        root2 = self.find_parent(j)

        if root1 == root2:
            return

        if self.ranks[root1] > self.ranks[root2]:
            self.parent_arr[root2] = root1
        else:
            self.parent_arr[root1] = root2
            if self.ranks[root1] == self.ranks[root2]:
                self.ranks[root2] += 1
'''