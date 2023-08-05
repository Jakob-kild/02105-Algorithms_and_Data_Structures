class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))

    def find(self, i):
        return self.id[i]

    def union(self, i, j):
        iID = self.find(i)
        jID = self.find(j)

        if iID != jID:
            for k in range(len(self.id)):
                if self.id[k] == iID:
                    self.id[k] = jID


# Read input
N, M = map(int, input().split())  # Number of sets and operations
union_find = UnionFind(N)

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