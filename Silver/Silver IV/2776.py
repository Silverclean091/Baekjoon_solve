import sys
input = sys.stdin.readline

# 테스트 케이스 개수 입력
t = int(input())

for i in range(t):
    note1_list = []
    note2_list = []
    
    # 수첩1의 정수의 개수 & 정수 입력
    note1 = int(input())
    note1_list = list(map(int, input().split()))
    
    # 수첩2의 정수의 개수 & 정수 입력
    note2 = int(input())
    note2_list = list(map(int, input().split()))
    
    # 수첩2의 내용이 수첩1에 있는지 확인
    for l in note2_list:
        if l in note1_list:
            print('1')
        else:
            print('0')