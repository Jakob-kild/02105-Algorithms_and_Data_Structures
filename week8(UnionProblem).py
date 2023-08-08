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

    def connected(self, i, j):
        if self.find(i) == self.find(j):
            return "YES"
        else:
            return "NO"


N, M = map(int, input().split())

Set = WeightedUnion(N)

for _ in range(M):
    command = input().split()
    if command[0] == "C":
        print(Set.connected(int(command[1]), int(command[2])))
    elif command[0] == "A":
        Set.union(int(command[1]), int(command[2]))
    else:
        print("error")
