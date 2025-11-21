import sys
input = sys.stdin.readline

# a보다 큰 시작점 탐색을 위한 이진탐색 함수
def find_start(points, a, N):
    start_num = 0
    end_num = N-1
    while start_num <= end_num:
        mid_num = (start_num + end_num) // 2
        if points[mid_num] < a:
            start_num = mid_num + 1
        else:
            end_num = mid_num-1
    return start_num

# b보다 작거나 같은 끝점 탐색을 위한 이진탐색 함수
def find_end(points, b, N):
    start_num = 0
    end_num = N-1
    while start_num <= end_num:
        mid_num = (start_num + end_num) // 2
        if points[mid_num] <= b:
            start_num = mid_num + 1
        else:
            end_num = mid_num-1
    return start_num

# 점의 개수 N과 선분의 개수 M 입력
N, M = map(int, input().split())
# 점의 좌표 입력받기 
points = list(map(int, input().split()))
points.sort() # 이진 탐색을 위한 정렬

# 선분의 좌표 입력받기
for i in range(M):
    a, b = map(int, input().split())
    
    # 이진탐색
    start_idx = find_start(points, a, N)
    end_idx = find_end(points, b, N)
    
    # 선분 위의 점의 개수(인덱스 개수) 구하기
    count_points = end_idx - start_idx
    print(count_points)