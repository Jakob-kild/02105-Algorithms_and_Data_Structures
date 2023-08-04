
kids = list(map(int, input().split()))
jealouse = []
if kids[0] < kids[1] and kids[0] < kids[2]:
    jealouse.append("Anna")
if kids[1] < kids[0]:
    jealouse.append("Laura")
if kids[2] < kids[0] or kids[2] < kids[1]:
    jealouse.append("Oscar")

if not jealouse:
    print("NONE")
else:
    for name in jealouse:
        print(name)
