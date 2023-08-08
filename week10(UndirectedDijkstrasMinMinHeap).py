class MinHeap:
    def __init__(self):
        self.nodes = [(0, 0)]  # Use a dummy element at index 0

    def min(self):
        return self.nodes[1]

    def extract_min(self):
        if len(self.nodes) <= 1:
            return None

        min_val = self.min()
        last_val = self.nodes.pop()

        if len(self.nodes) > 1:
            self.nodes[1] = last_val
            self.bubble_down(1)
        return min_val

    def insert(self, x):
        self.nodes.append(x)
        self.bubble_up(len(self.nodes) - 1)

    def decrease_key(self, node, new_weight):
        for i, (n, q) in enumerate(self.nodes):
            if n == node:
                self.nodes[i] = (n, new_weight)
                self.bubble_up(i)
                break

    def bubble_up(self, n):
        while n > 0:
            if self.nodes[self.parent(n)] > self.nodes[n]:
                self.nodes[self.parent(n)], self.nodes[n] = self.nodes[n], self.nodes[self.parent(n)]
                n = self.parent(n)
            else:
                break

    def bubble_down(self, n):
        while True:
            smallest = n
            if self.left(n) < len(self.nodes) and self.nodes[self.left(n)] < self.nodes[smallest]:
                smallest = self.left(n)
            if self.right(n) < len(self.nodes) and self.nodes[self.right(n)] < self.nodes[smallest]:
                smallest = self.right(n)
            if smallest != n:
                self.nodes[smallest], self.nodes[n] = self.nodes[n], self.nodes[smallest]
                n = smallest
            else:
                break

    def print_heap(self):
        return " ".join(map(str, self.nodes))

    def parent(self, x):
        return (x - 1) // 2

    def left(self, x):
        return x * 2 + 1

    def right(self, x):
        return x * 2 + 2


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
            queue.decrease_key(v, self.weights[v])
            queue.insert((v, edge_weight))

    def minimum_spanning_tree_weight(self):

        min_heap = MinHeap()
        min_heap.insert((1, 0))  # (node, weight)
        self.weights[1] = 0


        while True:
            min_val = min_heap.extract_min()
            if min_val is None:
                break

            current_node = min_val[0]
            current_weight = min_val[1]

            if current_weight > self.weights[current_node]:
                continue

            for neighbor, neighbor_weight in self.graph[current_node]:
                self.relax(current_node, neighbor, neighbor_weight, min_heap)




        return self.weights[1:]  # Exclude the weight at index 0


N, M = map(int, input().split())

graph = Dijkstras(N)

for _ in range(M):
    b_i, b_j, price = map(int, input().split())
    graph.add_edge(b_i, b_j, price)

print(" ".join(map(str, graph.minimum_spanning_tree_weight())))
