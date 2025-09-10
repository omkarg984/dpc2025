from collections import deque

def shortest_path(V, edges, start, end):
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * V
    distance = [0] * V

    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        if node == end:
            return distance[node]
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    return -1

V = int(input())
E = int(input())
edges = []
for _ in range(E):
    u, v = map(int, input().split())
    edges.append([u, v])
start = int(input())
end = int(input())
result = shortest_path(V, edges, start, end)
print(result)