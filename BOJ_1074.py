### 1074
### z

# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N, r, c가 주어진다.

# 출력
# r행 c열을 몇 번째로 방문했는지 출력한다.


# 2 * 2의 형태를 각 (0,0), (0,1), (1,0), (1,1)로 접근
# 각 위치는 1이 증가하는 형태
# 입력받은 R과 C를 그 안에서 찾음
def recursiveSq(n, r, c): # n은 지수, x는 
    global result # 전역변수를 함수에서도 사용
    if n == 2: 
        if r == R and c == C:
            print(result)
            return
        result += 1
        if r == R and c + 1 == C:
            print(result)
            return
        result += 1
        if r + 1 == R and c == C:
            print(result)
            return
        result += 1
        if r + 1 == R and c + 1 == C:
            print(result)
            return
        result += 1
        return

    # 호촐 시마다 절반 사이즈가 됨
    recursiveSq(n / 2, r, c) # 1/2의 (0,0) 
    recursiveSq(n / 2, r, c + n / 2)
    recursiveSq(n / 2, r + n / 2, c)
    recursiveSq(n / 2, r + n / 2, c + n / 2)


result = 0
N, R, C = map(int, input().split(' '))
recursiveSq(2 ** N, 0, 0) # 최종 사각형 형태, 2*2의 형태에서 (0,0)으로 시작