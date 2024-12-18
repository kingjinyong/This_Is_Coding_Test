# 내 답안
n, k = map(int, input().split())

cnt = 0

while n != 1:
    cnt += 1
    if n % k == 0:
        n /= k
    else:
        n -= 1
print(cnt)

#책 답안1 (단순)
n, k = map(int, input().split())
result = 0

while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1

    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

#책 답안 (효율?)
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
print(result)