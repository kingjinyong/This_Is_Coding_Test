n, k = map(int, input().split())

count = 0
while n >= k:               # n이 k 이상이라면 k로 계속 나누기
    if n % k != 0:          # 나누어 떨어지지 않는다면?
        n -= 1              # 1 빼주고
        count += 1          # 횟수 업
    n //= k                 # 나누어 떨어지면 나누기
    count += 1
# 자 이제 n이 k보다 작아졌어
while n > 1:            # 남은 수 1씩 뺴주면서 횟수 업
    n -= 1
    count += 1
print(count)
#---------- 단순하게 푸는 방법이었대... ----------

n, k = map(int, input().split()) # 17 4로 주어졌다면?
count = 0

while True:
    # n == k 로 나누어떨어지는 수 가 될 때까지 1씩 빼기 -> 수식으로 구해버림
    target = (n//k)*k   # target = (17//4) * 4 -> target = 4*4 = 16
    count += (n - target)   # count += 17 - 16 -> count += 1
    n = target  # n = 16
    # n이 k보다 작을 때(더 이상 나눌 쑤 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    count += 1
    n //= k     # n = 16//4 -> n = 4
    # -> 이후 반복

# 마지막으로 남은 수에 대하여 1씩 빼기 -> 이거도 수식으로 해버림
count += (n - 1)
print(count)
