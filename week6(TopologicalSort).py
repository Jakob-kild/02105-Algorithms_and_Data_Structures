import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False
        self.in_degree = 0

    def add_neighbor(self, new_neighbor):
        if new_neighbor not in self.neighbors:
            self.neighbors.append(new_neighbor)


class Graph:
    def __init__(self):
        self.nodes = {}
        self.in_degree_table = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].add_neighbor(self.nodes[to_node])
            self.nodes[to_node].in_degree += 1

        # Print the sorted nodes
        #for node in self.in_degree_table:
        #    print(f"Node {self.nodes[node].value}: In-degree {self.nodes[node].in_degree}")

    def topologicalSort(self, N):
        #self.in_degree_table = sorted(self.nodes, key=lambda node: self.nodes[node].in_degree)
        queue = deque()

        #queue all nodes with in-degree 0
        for node in range(1, N+1):
            if self.nodes[node].in_degree == 0:
                queue.append(node)

        courses_taken = 0
        semesters = 0


        while courses_taken < N:
            semesters += 1

            queue_size = len(queue)
            for i in range(queue_size):
                course = queue.popleft()
                for neighbor in self.nodes[course].neighbors:
                    neighbor.in_degree -= 1
                    if neighbor.in_degree == 0:
                        queue.append(neighbor.value)

            courses_taken += queue_size

        return semesters

N, M = map(int, input().split())
graph = Graph()

for _ in range(M):
    u, v = map(int, input().split())
    graph.add_node(u)
    graph.add_node(v)
    graph.add_edge(u, v)

print(graph.topologicalSort(N))

