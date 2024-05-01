t = int(input())
ary = []
for i in range(t):
    data = input().split()
    ary.append((data[0], int(data[1])))

ary = sorted(ary, key=lambda x: x[1])

for i in ary:
    print(i[0], end=" ")