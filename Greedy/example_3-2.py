# 내가 푼 답
n, m, k = map(int, input().split())

ary = list(map(int, input().split()))

ary.sort(reverse=True)

result = 0
cnt = 0

for i in range(m):
    cnt += 1
    if cnt != k:
        result += ary[0]
    elif cnt == k:
        result += ary[1]
        cnt = 0

print(result)

# 책 답안
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)

# 책 답안 2(수식 사용)
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

first_count = int(m // (k + 1)) * k
first_count += m % (k + 1)

result = 0
result += (first_count) * first  # 가장 큰 수 더해주기
result += (m - first_count) * second  # 두 번째로 큰 수 더하기

print(result)
