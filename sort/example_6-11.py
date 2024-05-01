n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b = sorted(b, reverse=True)

for i in range(k):
    a[i], b[i] = b[i], a[i]
print(sum(a))