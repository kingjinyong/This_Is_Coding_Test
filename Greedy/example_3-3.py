# 내 답안
n, m = map(int, input().split())

ary = []
for i in range(n):
    ary.append(min(map(int, input().split())))
print(max(ary))

# 책 답안1(min() 함수 이용)
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)

# 책 답안2(2중 반복문 구조 사용)
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)