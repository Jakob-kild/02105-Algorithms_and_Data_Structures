import heapq

class DijkstrasMST:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.weights = [float('inf')] * (self.n + 1)
        self.parents = [None] * (self.n + 1)

    def add_edge(self, i, j, weight):  # directed
        self.graph[i].append((j, weight))

    def relax(self, u, v, edge_weight, queue):
        if self.weights[v] > self.weights[u] + edge_weight:
            self.weights[v] = self.weights[u] + edge_weight
            self.parents[v] = u  # Update parent for MST construction
            heapq.heappush(queue, (self.weights[v], v))

    def minimum_spanning_tree_weight(self, source):
        min_heap = [(0, source)]  # (weight, node)
        self.weights[source] = 0

        while min_heap:
            weight, current_node = heapq.heappop(min_heap)

            if weight > self.weights[current_node]:
                continue

            for neighbor, neighbor_weight in self.graph[current_node]:
                self.relax(current_node, neighbor, neighbor_weight, min_heap)

        return self.weights[1:], self.parents[1:]  # Return weights and parents

N, M, source = map(int, input().split())
#the nodes have to be 1-indexed
graph = DijkstrasMST(N)

for _ in range(M):
    b_i, b_j, price = map(int, input().split())
    graph.add_edge(b_i, b_j, price)

weights, parents = graph.minimum_spanning_tree_weight(source)
print("Minimum Spanning Tree Weights:", " ".join(map(str, weights)))
print("Parent Nodes (plus 1) for MST:", " ".join(map(str, parents)))




