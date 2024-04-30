array = [7, 5, 9, 0, 8, 3, 6, 4, 1, 2]

for i in range(len(array)):
    min_index = i       # 가장 작은 원소 (기본 값으로는 그냥 첫번째 원소)
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j       # 가장 작은 원소가 계속 바뀌면서 가장 작은 원소를 찾게 됨
    array[i], array[min_index] = array[min_index], array[i]     # 스와핑
print(array)

