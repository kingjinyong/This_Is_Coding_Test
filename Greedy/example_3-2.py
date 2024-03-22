# ------------- 단순하게 푸는 답안 ----------------
# N, M, K = map(int, input().split())
# ary = list(map(int, input().split()))
# ary.sort(reverse=True)
# count = 0
# answer = 0
#
# while True:                     # 무한 반복
#     for i in range(K):          # 가장 큰 수 K번 더해주기
#         if M == 0:              # 총 주어진 횟수 M이 0이 된다면 반복문 종료.
#             break
#         answer += ary[0]        # 가장 큰 수 더해주기
#         M -= 1                  # 더해줬으니 횟수 차감
#     if M == 0:                  # 주어진 횟수가 0이 된다면 반복문 종료
#         break
#     answer += ary[1]            # 두번째로 큰 수 더해주기
#     M -= 1                      # 더해줬으니 횟수 차감
# print(answer)

# ---------- 수학적 아이디어로 풀 수 있다고 함... -----------
n, m, k = map(int, input().split())
ary = list(map(int, input().split()))
ary.sort()
first = ary[n - 1]                  # 가장 큰 수
second = ary[n - 2]                # 두번째로 큰 수

count = m//(k+1) * k + m % (k + 1)

result = 0
result += (count) * first            # 가장 큰 수 더하기
result += (m - count) * second      # 두 번째 큰 수 더하기

print(result)                       # 최종 답안 출력