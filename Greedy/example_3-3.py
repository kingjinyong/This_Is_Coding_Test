n, m = map(int, input().split())
min_v = 10001
mins = []                                   # 각 행에서 가장 작은 수를 저장 할 리스트
for i in range(n):
    ary = list(map(int, input().split()))
    mins.append(min(ary))                   # 리스트에서 가장 작은 수 리스트에 추가
print(max(mins))                            # 작은 수들을 모아놓은 리스트에서 가장 큰 수 출력