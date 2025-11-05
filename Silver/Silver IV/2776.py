import sys

# 테스트케이스 입력
t = int(sys.stdin.readline())

for i in range(t):
    note1_list = []
    note2_list = []
    
    # 수첩1의 정수의 개수 & 정수 입력
    note1 = int(sys.stdin.readline())
    note1_list = list(map(int, sys.stdin.readline().split()))
    
    # 수첩2의 정수의 개수 & 정수 입력
    note2 = int(sys.stdin.readline())
    note2_list = list(map(int, sys.stdin.readline().split()))
    
    # 수첩2의 내용이 수첩1에 있는지 확인
    for l in note2_list:
        if l in note1_list:
            print('1')
        else:
            print('0')