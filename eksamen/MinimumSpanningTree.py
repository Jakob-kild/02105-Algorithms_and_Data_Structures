import heapq


class PrimsMST:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.mst_edges = []

    def add_edge(self, b1, b2, price):
        self.graph[b1].append((b2, price))
        self.graph[b2].append((b1, price))

    def find_minimum_spanning_tree(self):
        visited = [False] * (self.n + 1)
        min_heap = [(0, 1, -1)]  # Start with building 1 and initial cost 0, -1 indicates no parent
        total_cost = 0

        while min_heap:
            cost, current, parent = heapq.heappop(min_heap)

            if visited[current]:
                continue

            visited[current] = True
            total_cost += cost

            if parent != -1:
                self.mst_edges.append((parent, current))

            for neighbor, neighbor_cost in self.graph[current]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (neighbor_cost, neighbor, current))

        return total_cost

    def print_minimum_spanning_tree(self):
        print("Minimum Spanning Tree Edges:")
        for edge in self.mst_edges:
            print(edge)

N, M = map(int, input().split())
prim = PrimsMST(N)

for _ in range(M):
    b1, b2, price = map(int, input().split())
    prim.add_edge(b1, b2, price)

cheapest_total_price = prim.find_minimum_spanning_tree()
print("Minimum Spanning Tree Total Cost:", cheapest_total_price)
prim.print_minimum_spanning_tree()
