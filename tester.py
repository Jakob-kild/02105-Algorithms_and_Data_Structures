class WeightedPathCompressedUnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)

        if ri != rj:
            if self.size[ri] < self.size[rj]:
                self.parent[ri] = rj
                self.size[rj] += self.size[ri]
            else:
                self.parent[rj] = ri
                self.size[ri] += self.size[rj]


# Read input
N = int(input())  # Number of sets
M = int(input())  # Number of Find or Union operations
union_find = WeightedPathCompressedUnionFind(N)

# Process Find and Union operations
for _ in range(M):
    operation, *args = input().split()

    if operation == "F":
        X = int(args[0])
        root = union_find.find(X)
        print(root)
    elif operation == "U":
        X, Y = map(int, args)
        union_find.union(X, Y)
