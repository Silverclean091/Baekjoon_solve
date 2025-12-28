import sys
input = sys.stdin.readline

N, M = map(int, input().split())   # 알고있는 노래의 개수 N, 문제의 개수 M
S = []      # 노래 제목의 길이를 저장할 리스트 S (사용X)
T = []      # 노래 제목을 저장할 리스트 T
notes = []  # 노래의 음을 저장할 리스트 notes

# 기존에 알고 있는 노래 입력받기
for i in range(N):
    tmp = input().split() # 공백을 기준으로 분할
    S.append(tmp[0])      # 첫 번쨰 분할 : 노래 제목의 길이
    T.append(tmp[1])      # 두 번째 분할 : 노래 제목
    notes.append("".join(tmp[2:]))  # 세 번째 ~ : 노래의 음 (띄어쓰기 제거)

# 전주 듣고 노래 맞히기
for i in range(M):
    jh_notes = "".join(input().split())  # 음 입력받기 (공백제거)
    cnt = 0   # 해당 음으로 시작하는 노래의 개수
    ans = ""  # 해당 음으로 시작하는 노래의 제목

    for idx, j in enumerate(notes):
        if j[:3] == jh_notes:   # notes에 있는 모든 음들의 "앞의 세 음" 비교
            cnt += 1      # 일치할 경우 cnt 값 증가
            ans = T[idx]  # ans에 해당 노래의 제목 추가
    
    if cnt == 0:    # 답이 존재하지 않을 경우
        print("!")
    elif cnt == 1:  # 답이 한 개일 경우
        print(ans)
    else:
        print("?")  # 답이 두 개 이상일 경우