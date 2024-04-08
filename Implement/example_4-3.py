knite = input()

row = int(knite[1])
column = ord(knite[0])

ways = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

possible_count = 0
# ord 사용하기

for i in ways:
    x, y = 0, 0
    x = row + i[1]
    y = column + i[0]

    if x < 1 or x > 8 or y < ord('a') or y > ord('h'):
        continue
    possible_count += 1
print(possible_count)

