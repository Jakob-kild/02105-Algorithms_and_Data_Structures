
class QuickFind:
    def __init__(self, n):
        self.id_arr = list(range(n))

    def find(self, i):
        while i != self.id_arr[i]:
            i = self.id_arr[i]
        return self.id_arr[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        self.id_arr[i_id] = j_id


N = int(input())
M = int(input())

Set = QuickFind(N)

for _ in range(M):
    command = input().split()
    if command[0] == "F":
        print(Set.find(int(command[1])))
    elif command[0] == "U":
        Set.union(int(command[1]), int(command[2]))
    else:
        print("error")
