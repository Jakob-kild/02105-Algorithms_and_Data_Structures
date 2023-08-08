import heapq

class Dijkstras:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.weights = [float('inf')] * (self.n + 1)

    def add_edge(self, i, j, weight): #undirected
        self.graph[i].append((j, weight))
        self.graph[j].append((i, weight))

    def relax(self, u, v, edge_weight, queue):
        if self.weights[v] > self.weights[u] + edge_weight:
            self.weights[v] = self.weights[u] + edge_weight
            heapq.heappush(queue, (self.weights[v], v))

    def minimum_spanning_tree_weight(self):

        min_heap = [(0, 1)]  # (weight, node)
        self.weights[1] = 0

        while min_heap:
            weight, current_node = heapq.heappop(min_heap)

            if weight > self.weights[current_node]:
                continue

            for neighbor, neighbor_weight in self.graph[current_node]:
                if current_node > 1:
                    included_box_weight = neighbor_weight + 5
                    self.relax(current_node, neighbor, included_box_weight, min_heap)
                else:
                    self.relax(current_node, neighbor, neighbor_weight, min_heap)


        return self.weights[1:]  # Exclude the weight at index 0

N, M = map(int, input().split())

graph = Dijkstras(N)

for _ in range(M):
    b_i, b_j, price = map(int, input().split())
    graph.add_edge(b_i, b_j, price)

print(" ".join(map(str, graph.minimum_spanning_tree_weight())))
