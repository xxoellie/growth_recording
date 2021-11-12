"""BFS(너비 우선 탐색) : 너비를 우선해서그래프를 탐색하는 기법, 시작점인 루트 노드와 같은 거리 있는 노드를 우선으로 방문
큐의 자료 구조를 사용하는 것이 핵심, 노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보만 큐에 넣어 먼저 큐에 들어있떤 노드부터 방문"""

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
# 다음과 같이 방향이 있는 유향그래프를 BFS로 탐색한다면

def bfs(graph, start_node):
    visit = list() # 방문했던 노드 목록을 차례대로 저장할 리스트와
    queue = list() #방문할 노드의 목록을 차례대로 저장할 리스트를 만듬

    queue.append(start_node) # 시작 노드를 큐에 넣어준다

    while queue : # 큐의 목록이 바닥 날때까지 loop를 돌려준다
        node = queue.pop(0) #큐의 맨 앞에 있는 노드를 꺼내온다
        if node not in visit : # 해당 노드가 아직 방문 리스트에 없다면
            visit.append(node) # 방문리스트에 추가해주고
            queue.extend(graph[node]) # 해당노드의 자식노드들을 큐에 추가해준다다

    return visit


"""DFS(깊이 우선 탐색)
한 방향으로 갈 수 있을만큼 깊게 탐색한다
코드 기준으로 봤을때 DFS는 BFS와 거의 똑같고 queue 대신 stack을 사용한다는 점만 다름"""
def dfs(graph, start_node) :
    visit = []
    stack = []

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit :
            visit.append(node)
            stack.extend(graph[node])
    return visit
# queue의 변수명이 stack으로 바꾸었고 8번 라인에서 pop(0)을 하던 부분이 pop()으로 바뀌었다.
# 리스트에서 pop()을 하게되면 맨 마지막에 넣었던 아이템을 가져오게 되므로 stack과 동일하게 동작한다.
# 반대로 pop(0)을 하게되면 맨 앞에있는 요소를 가져오므로 queue와 동일하게 동작한다.


from sys import stdin
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(1, dic)
print(len(visited)-1)
