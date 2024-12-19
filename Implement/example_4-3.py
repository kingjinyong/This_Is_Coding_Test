# 내 답안
locate = list(input())
x, y = int(ord(locate[0]) - ord('a') + 1) - 1, int(locate[1]) - 1

dx = [1, -1, 1, -1, 2, -2, 2, -2]
dy = [2, 2, -2, -2, 1, 1, -1, -1]

cnt = 0
# 8가지 경우로 확인해주기
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1

print(cnt)

# 책 답안
input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 8가지 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    nr = row + step[0]
    nc = column + step[1]

    # 가능하면 result 증가
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        result += 1
print(result)