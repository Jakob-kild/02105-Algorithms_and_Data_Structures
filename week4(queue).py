class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        dequeued_value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued_value

# Read input
N = int(input())
queue = Queue()
output = []

for _ in range(N):
    operation = input().split()
    if operation[0] == "E":
        x = int(operation[1])
        queue.enqueue(x)
    elif operation[0] == "D":
        dequeued_value = queue.dequeue()
        if dequeued_value is not None:
            output.append(dequeued_value)

# Print output
for val in output:
    print(val)