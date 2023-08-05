class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None

        max_value = self.heap[0]
        last_value = self.heap.pop()

        if self.heap:
            self.heap[0] = last_value
            self._sift_down(0)

        return max_value

    def print_heap(self):
        print(" ".join(map(str, self.heap)))

    def _sift_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def _sift_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if (
                left_child_index < len(self.heap)
                and self.heap[left_child_index] > self.heap[largest]
            ):
                largest = left_child_index

            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] > self.heap[largest]
            ):
                largest = right_child_index

            if largest != index:
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                index = largest
            else:
                break


# Read input
N = int(input())
heap = MaxHeap()

# Process operations
for _ in range(N):
    operation = input().split()
    if operation[0] == "I":
        value = int(operation[1])
        heap.insert(value)
    elif operation[0] == "E":
        extracted = heap.extract_max()
        if extracted is not None:
            print(extracted)
    elif operation[0] == "P":
        heap.print_heap()