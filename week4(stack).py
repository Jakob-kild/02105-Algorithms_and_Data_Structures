class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            return None
        popped_value = self.top.data
        self.top = self.top.next
        return popped_value

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node


N = int(input())

stack = Stack()
output = []

for _ in range(N):
    operation = input().split()
    if operation[0] == "PU":
         stack.push(operation[1])
    elif operation[0] == "PO":
         popped_value = stack.pop()
         if popped_value is not None:
             output.append(popped_value)

for val in output:
    print(val)
