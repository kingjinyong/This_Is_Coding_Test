from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 방향
dx = [-1, 1,0 , 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #괴물 만나면 무시
            if graph[nx][ny] == 0:
                continue
            #안 만나면 최소 거리 증가하고 큐에 추가
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))