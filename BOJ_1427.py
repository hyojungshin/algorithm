### 1427
### 소트인사이드

# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
# 첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다. -> 0~9의 숫자가 등장한만큼 정렬되어 출력되어야 함

data = list(map(int, input()))
# numbers = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
result = ''

## 각 자리수가 몇번 등장했는지 dict 형태에 결과를 모아서 다시 그만큼 출력하는 형태
# for i in range(len(data)):
#     n = data[i]
#     numbers[n] = numbers[n] + 1

# for j in range(9, -1, -1):
#     result += str(j) * int(numbers[j])

# print(result)



## 문제에서는 단순히 숫자 출력을 원했으므로 이 방법으로 간단하게 표시할 수 있음
for i in range(9, -1, -1):
    for j in data:
        if int(j) == i:
            print(i, end='')
            #result += str(i)

#print(result)