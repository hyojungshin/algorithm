### 5397
### 키로거

#. 비밀번호를 알기 위한 키보드 로그 프로그램

# 1. 첫째 줄에 테스트 케이스 개수 입력
# 2. 백스페이스 : - (앞에 글자 있으면 지움)
#     화살표 : < , > (앞뒤로 이동 가능할 시 1만큼씩 이동)
#     그 외 비밀번호

# key point
# 키보드 입력 시 커서의 위치에서 작동해야 하므로 커서 계산이 까다로움
# stack 커서 stack 의 구조로 커서 위치를 알아내는 것이 효율적
# # list에 append(), pop()를 사용하면 실제로는 list 타입이나 stack처럼 사용하게 되어 스택 연결 시 reversed를 해줘야 함

n = int(input())

for _ in range (n):
    left_stack = []
    righ_stack = []
    
    data = input()

    for i in data:
        # pop() 사용 시 빈 리스트 아닐 때만 가능
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack: 
                righ_stack.append(left_stack.pop())
        elif i == '>':
            if righ_stack: 
                left_stack.append(righ_stack.pop())
        else:
            left_stack.append(i)
    
    left_stack.extend(reversed(righ_stack)) # stack으로 작동하므로 righ_stack에서 역순으로 정렬해서 마지막 원소(원래는 처음)부터 pop()해서 연결하는 형태
    print(''.join(left_stack))



### 참고
# list 자체를 reversed 할 때는 예상한 대로 역순으로 정렬됨

# a = ['C']
# b = ['A', 'B']
# c = ['C']
# d = ['A', 'B']

# a.extend(b)
# print(a) -> ['C', 'A', 'B']

# c.extend(reversed(d))
# print(c) -> ['C', 'B', 'A'] 