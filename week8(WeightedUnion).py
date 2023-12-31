class WeightedUnion:
    def __init__(self, n):
        self.parent_arr = list(range(n))
        self.size_arr = [1] * n  # Stores the size of each tree

    def find(self, i):
        if self.parent_arr[i] != i:
            self.parent_arr[i] = self.find(self.parent_arr[i])
        return self.parent_arr[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id != j_id:
            if self.size_arr[i_id] < self.size_arr[j_id]:
                self.parent_arr[i_id] = j_id
                self.size_arr[j_id] += self.size_arr[i_id]
            else:
                self.parent_arr[j_id] = i_id
                self.size_arr[i_id] += self.size_arr[j_id]


N = int(input())
M = int(input())

Set = WeightedUnion(N)

for _ in range(M):
    command = input().split()
    if command[0] == "F":
        print(Set.find(int(command[1])))
    elif command[0] == "U":
        Set.union(int(command[1]), int(command[2]))
    else:
        print("error")
