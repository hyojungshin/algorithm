### 2750
### 수 정렬하기

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

num = int(input())
numbers = []
result = []

for i in range(num):
    numbers.append(int(input()))

## 1) sort
#numbers.sort()
#print('\n'.join(map(str, numbers)))


## 2) remove
# for n in range(num):
#     result.append(min(numbers))
#     numbers.remove(min(numbers))
#print('\n'.join(map(str, result)))


## 3) 선택적 정렬(오름차순이므로 가장 작은 수를 찾음)
for i in range(num):
    min_index = i
    for j in range(i+1, num): # 다음 인덱스
        if numbers[min_index] > numbers[j]: # 다음 인덱스가 작으면 스와프
            numbers[i], numbers[j] = numbers[j], numbers[i] # a, b = b, a 

print('\n'.join(map(str, numbers)))