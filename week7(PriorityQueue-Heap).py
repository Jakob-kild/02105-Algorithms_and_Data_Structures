class MaxHeap:
    def __init__(self):
        self.nodes = []

    def max(self):
        return self.nodes[0]

    def extract_max(self):
        if not self.nodes:
            return None

        max = self.max()
        last_val = self.nodes.pop()

        if self.nodes:
            self.nodes[0] = last_val
            self.bubble_down(0)
        return max

    def insert(self, x):
        self.nodes.append(x)
        self.bubble_up(len(self.nodes) - 1)

    def increase_key(self, x, k):
        self.nodes[x] = k
        self.bubble_up(x - 1)

    def bubble_up(self, n):
        while n > 0:
            if self.nodes[self.parent(n)] < self.nodes[n]:
                self.nodes[self.parent(n)], self.nodes[n] = self.nodes[n], self.nodes[self.parent(n)]
                n = self.parent(n)
            else:
                break

    def bubble_down(self, n):
        while True:
            largest = n
            if self.right(n) < len(self.nodes) and self.nodes[self.right(n)] > self.nodes[largest]:
                largest = self.right(n)
            if self.left(n) < len(self.nodes) and self.nodes[self.left(n)] > self.nodes[largest]:
                largest = self.left(n)
            if largest != n:
                self.nodes[largest], self.nodes[n] = self.nodes[n], self.nodes[largest]
                n = largest
            else:
                break

    def print_heap(self):
        #print(" ".join(str(value) for key, value in self.nodes.items()))
        return " ".join(map(str, self.nodes))


    def parent(self, x):
        return (x-1) // 2

    def left(self, x):
        return x * 2 + 1

    def right(self, x):
        return x * 2 + 2


N = int(input())

heap = MaxHeap()

for _ in range(N):
    command = input().split()
    if command[0] == "I":
        heap.insert(int(command[1]))
    elif command[0] == "P":
        print(heap.print_heap())
    elif command[0] == "E":
        extract = heap.extract_max()
        if extract is not None:
            print(extract)
    else:
        print("error")
