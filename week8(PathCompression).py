class PathCompression:
    def __init__(self, n):
        self.id_arr = list(range(n))
        self.size_arr = [1] * n  # Stores the size of each tree

    def find(self, i):
        if self.id_arr[i] != i:
            self.id_arr[i] = self.find(self.id_arr[i])
        return self.id_arr[i]

    def print(self):
        print(self.id_arr)

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id != j_id:
            if self.size_arr[i_id] < self.size_arr[j_id]:
                self.id_arr[i_id] = j_id
                self.size_arr[j_id] += self.size_arr[i_id]
            else:
                self.id_arr[j_id] = i_id
                self.size_arr[i_id] += self.size_arr[j_id]


N = int(input())
M = int(input())

Set = PathCompression(N)

for _ in range(M):
    command = input().split()
    if command[0] == "F":
        print(Set.find(int(command[1])))
        Set.print()
    elif command[0] == "U":
        Set.union(int(command[1]), int(command[2]))
    else:
        print("error")
