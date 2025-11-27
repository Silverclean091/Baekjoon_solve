import sys
input = sys.stdin.readline

# 행과 열을 정수로 입력받기
N, M = map(int, input().split())

for i in range(N):
    bungeobbang = input().strip()  # 줄바꿈 제거 (출력형식 오류 수정)
    print(bungeobbang[::-1])       # 인덱싱으로 뒤집어서 출력