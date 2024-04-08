n = int(input())

work = list(map(str, input().split()))

travler = [1, 1]

print(travler, work)

for i in work:
    if i == 'L' and (travler[1] - 1 >= 1):
        travler[1] -= 1
    if i == 'R' and (travler[1] + 1 <= 5):
        travler[1] += 1
    if i == 'U' and (travler[0] - 1 >= 1):
        travler[0] -= 1
    if i == 'D' and (travler[0] + 1 <= 5):
        travler[0] += 1

print(travler[0], travler[1])