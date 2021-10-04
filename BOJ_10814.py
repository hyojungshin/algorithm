### 10814
### 나이순 정렬

# 1. 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

## 입력
#. 첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
#. 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

## 출력
#. 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

caseN = int(input())
users = list()

# 출력은 되나 시간초과 발생
# ages = set()
# for _ in range(caseN):
#     data = input()
#     users.append(data)    
#     ages.add(int(data.split(' ')[0]))

# for i in range(len(ages)):
#     age = ages.pop()
#     for j in range(len(users)):
#         if age == int(users[j].split(' ')[0]):
#             print(users[j])     

for _ in range(caseN):
    data = input().split(' ')
    users.append((int(data[0]), data[1])) # 리스트에 튜플 형태로 추가, 나이는 int로 변경필요

users = sorted(users, key=lambda x:x[0]) # 첫번째 요소로 정렬, 즉 나이순

for i in users:
    #print(i) # 튜플 형태로 나오므로 각각 출력해야 함
    print(i[0], i[1])