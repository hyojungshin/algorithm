### 1920
### 수 찾기

# 입력된 N개의 정수 중 X라는 정수가 존재하는지 알아내는 프로그램 
# N(1 ≤ N ≤ 100,000), M(1 ≤ M ≤ 100,000)이 주어지므로 시간에 주의
# 시간 단축을 위해 list 아닌 set 사용

n = int(input())
nSet = set(map(int, input().split(' '))) # [2,3,3,4] -> {2,3,4} 중복 제거
m = int(input())
mlist = list(map(int, input().split(' ')))
result = []

for i in mlist: # list를 넣어 원소 하나씩 꺼냄
    if i in nSet: # list, set, 튜플 모두 통째로 비교 가능
        print('1')
    else:
        print('0')
     

