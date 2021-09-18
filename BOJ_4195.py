### 4195
### 친구 네트워크

# 친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램
# 친구 네트워크란 친구 관계만으로 이동할 수 있는 사이
# 첫째 줄에 테스트 케이스
# 테스트 케이스 첫째 줄 친구 관계 수 F, 100,000 넘지 않음
# 둘째 줄은 두 사용자 이름

# HINT
# union-find 합집합으로 해결
# find : 연결 관계의 부모(첫번째 연결)를 찾음 
# union : 집합을 합침, 각 집합의 개수를 더하면 연결관계의 수

# find : 재귀형태로 원소의 부모 찾아 반환 
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

# union : 집합의 부모로 연결, 합집합 시 y에 x를 붙이는 형태(x가 기준), 연결관계 수도 합침
def union(x, y):
    x = find(x)
    y = find(y)

    if x !=y:
        parent[y] = x
        number[x] += number[y]



test_case = int(input())
result = []

for _ in range(test_case):
    parent = dict() # 부모 정보를 갖도록 key, value 형태인 dict 사용
    number = dict()

    f = int(input())

    for _ in range(f): # 한 줄씩 처리 
        x, y = input().split(' ') 

        # parent에 처음 입력 시에는 연결관계 수 1
        if x not in parent:
            parent[x] = x
            number[x] = 1

        if y not in parent:
            parent[y] = y
            number[y] = 1


        union(x, y) # x, y의 부모를 찾아 x로 연결, 연결관계 수도 합침
        result.append(number[find(x)]) # 최종 부모의 연결관계 수

print('\n'.join(list(map(str, result))))
# print(parent) 
# {'Fred': 'Fred', 'Barney': 'Fred', 'Betty': 'Fred', 'Wilma': 'Betty'} 


# 2
# 3
# Fred Barney
# Barney Betty
# Betty Wilma

# 1
# 4
# Fred Barney
# Betty Wilma
# Betty2 Wilma
# Barney Betty


# 2
# 2
# 3
# 5