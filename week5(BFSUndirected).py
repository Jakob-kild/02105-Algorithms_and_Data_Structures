import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False
        self.discovery_time = 0
        self.finish_time = 0

    def add_neighbor(self, new_neighbor):
        if new_neighbor not in self.neighbors:
            self.neighbors.append(new_neighbor)


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].add_neighbor(self.nodes[to_node]) #add edge both ways because of undirected graph
            self.nodes[to_node].add_neighbor(self.nodes[from_node])

    def BFS(self, start, target):
        queue = deque([start])

        while queue:
            current_node = queue.popleft()
            current_node.visited = True

            if current_node == target:
                return True

            for neighbor in current_node.neighbors:
                if not neighbor.visited:
                    queue.append(neighbor)
        return False


N, M, a, b = map(int, input().split())
graph = Graph()

for _ in range(M):
    u, v = map(int, input().split())
    graph.add_node(u)
    graph.add_node(v)
    graph.add_edge(u, v)

if a not in graph.nodes or b not in graph.nodes:
    print("NO")
else:
    graph.BFS(graph.nodes[a], graph.nodes[b])

    if graph.nodes[b].visited:
        print("YES")
    else:
        print("NO")
