import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())  # 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점 번호 V
graph = [[] for _ in range(N+1)]  # 정점들의 간선 정보를 저장할 빈 2차원 인접 리스트 만들기
# 예를 들어 N이 5일 경우, graph = [ [], [], [], [], [], [] ]

# 간선 입력 (양 정점은 서로 연결되어야 하므로 각 정점의 인접 리스트에 모두 저장)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 문제의 정의에 따라 정점 번호가 작은 것부터 방문하도록 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()

# DFS (재귀)
visited = [False] * (N+1)  # 모든 노드가 방문되지 않았다는 의미로 False로 초기화 (dfs는 재귀함수이므로 바깥에 선언)
def dfs(v, visited):
    visited[v] = True  # 기존값은 모두 False로 되어있음, 방문한 값만 True로 변경
    print(v, end=' ')  # 방문함과 동시에 출력하기 (문제 형식에 맞게 띄어쓰기로 출력)
    for next_node in graph[v]:  # 정점 v를 탐색, 인접 리스트 내의 정점을 next_node로 정의
        if not visited[next_node]:  # next_node가 False라면 (아직 방문하지 않았다면)
            dfs(next_node, visited) # 해당 노드로 이동하여 재귀 dfs함수 호출

# BFS (큐)
def bfs(start):
    visited = [False] * (N+1)  # 모든 노드가 방문되지 않았다는 의미로 False로 초기화
    queue = deque([start])     # 시작 정점을 큐에 먼저 집어넣어서 큐 자료형 생성
    visited[start] = True      # 첫 정점을 방문했다는 의미로 True로 변경

    while queue:  # 큐가 비워지기(empyt) 전까지 실행
        v = queue.popleft()  # 큐의 가장 왼쪽에 있는 값을 시작 정점인 v로 변경, 값 꺼내기
        print(v, end=' ')    # v로 꺼낸 값을 출력 (문제 형식에 맞게 띄어쓰기로 출력)
        for next_node in graph[v]:  # 정점 v를 탐색, 인접 리스트 내의 정점을 next_node로 정의
            if not visited[next_node]:  # next_node가 False라면 (아직 방문하지 않았다면)
                visited[next_node] = True  # next_node의 값을 방문했다는 의미로 True로 변경
                queue.append(next_node)    # next_node를 큐에 삽입하기 (그래야 출력할 수 있음)

dfs(V, visited)
print()
bfs(V)