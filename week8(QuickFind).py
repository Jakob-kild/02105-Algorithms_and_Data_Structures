class QuickUnion:
    def __init__(self, n):
        self.id_arr = list(range(n))

    def find(self, i):
        return self.id_arr[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id != j_id:
            for k in range(len(self.id_arr)):
                if self.id_arr[k] == i_id:
                    self.id_arr[k] = j_id

N = int(input())
M = int(input())

Set = QuickUnion(N)

for _ in range(M):
    command = input().split()
    if command[0] == "F":
        print(Set.find(int(command[1])))
    elif command[0] == "U":
        Set.union(int(command[1]), int(command[2]))
    else:
        print("error")