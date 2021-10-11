### 1074
### z

# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N, r, c가 주어진다.

# 출력
# r행 c열을 몇 번째로 방문했는지 출력한다.

# 이 방식은 결과를 찾을 수는 있으나 시간초과 발생하여 아래 방법으로 해결해야 함
# def recursiveSq(n, r, c): # n은 지수, x는 
#     global result # 전역변수를 함수에서도 사용
#     print('result = ', result, ', n =', n)
#     # 2 * 2 형태가 되면 각 (0,0), (0,1), (1,0), (1,1)로 접근
#     # 각 위치는 1이 증가하는 형태
#     # 입력받은 R과 C를 그 안에서 찾음
#     if n == 2: 
#         if r == R and c == C:
#             print(result)
#             return
#         result += 1
#         if r == R and c + 1 == C:
#             print(result)
#             return
#         result += 1
#         if r + 1 == R and c == C:
#             print(result)
#             return
#         result += 1
#         if r + 1 == R and c + 1 == C:
#             print(result)
#             return
#         result += 1
#         return

#     # 2 * 2 형태 이전에는 호출 시마다 절반 사이즈가 되는 특징을 활용
#     recursiveSq(n / 2, r, c) # (0,0) 
#     recursiveSq(n / 2, r, c + n / 2)
#     recursiveSq(n / 2, r + n / 2, c)
#     recursiveSq(n / 2, r + n / 2, c + n / 2)


# result = 0
# N, R, C = map(int, input().split(' '))
# recursiveSq(2 ** N, 0, 0) # 최종 사각형 형태, 2*2의 형태에서 (0,0)으로 시작


result = 0

def recursiveSq(n, r, c):
    global result
    if r == R and c == C: # 자기 영역을 찾은 후 r, c 같은지 확인
        print(int(result))
        return

    if n == 1: # 자기 영역을 찾음
        result += 1
        return

    # 함수에서 r은 보다 입력받은 R이 크거나 같아야 하며, R은 전
    # 자기 영역을 찾기 전에는 영역의 셀 개수만큼 result에 더함
    if not (r <= R < r + n and c <= C < c + n):  # 첫 시도는 해당 안됨, 부등호가 연속으로 등장할 경우 첫번째 부등호 참 거짓 판별 후 참일 경우 두번째 요소로 그 다음 과정 진행
        result += n * n
        return

    # 이후 호출 시마다 절반 사이즈(2 ** n-1)가 되도록 호출하며 각 호출이 4개씩 다시 호출하는 형태
    # -> N-1(= n / 2)만큼의 횟수로 각 위치의 합을 구하다가 r과 c가 일치하는 지점의 숫자만 출력하는 방법
    # n / 2 는 N-1 효과
    # r + n / 2는 r + (n / 2)
    # print('check ======>', 'n=', n, ', r=', r, ', c=', c, ', r+n/2=', r+n/2, ', result=',result)
    recursiveSq(n / 2, r, c) # (0, 0)
    recursiveSq(n / 2, r, c + n / 2) # (0, 1)
    recursiveSq(n / 2, r + n / 2, c) # (1, 0)
    recursiveSq(n / 2, r + n / 2, c + n / 2) # (1, 1)


N, R, C = map(int, input().split(' '))
recursiveSq(2 ** N, 0, 0) # 첫 호출 시에는 최대 사이즈로 호출
