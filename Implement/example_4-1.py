# 내 답안
n = int(input())

work_list = list(map(str, input().split()))

worker = [1, 1]

for w in work_list:
    if w == 'R' and worker[1] < n:
        worker[1] += 1
    if w == 'L' and worker[1] > 1:
        worker[1] -= 1
    if w == 'D' and worker[0] < n:
        worker[0] += 1
    if w == 'U' and worker[0] > 1:
        worker[0] -= 1
    print(worker)
print(*worker)

# 책 답안1

n = int(input())
x, y = 1, 1
plans = input().split()

work_type = ['R', 'L', 'D', 'U']

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for plan in plans:
    for i in range(len(work_type)):

        if plan == work_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

print(x, y)