n, m = map(int, input().split())
x, y, d = map(int, input().split())

maps = []
visited = []
for i in range(n):
    maps.append(list(map(int, input().split())))
    visited.append(list([0] * m))
# print(maps)
# print(visited)
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


# 처음 있는 곳 방문 처리
visited[x][y] = 1

cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    # 회전 했을 때 가보지 않은 칸이 있다면 전진, 아니면 회전만 하고 가만히 있기.
    if maps[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 다 둘러봤을 경우.....
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        # 뒤로 갈 수 있으면 이동 ㄱ
        if maps[nx][ny] == 0:
            x, y = nx, ny
        else:
            print("멈춤!")
            break
        turn_time = 0
print(cnt)

