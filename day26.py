def has_cycle(v, edges):
    graph = {i: [] for i in range(v)}
    for u, w in edges:
        if u >= v or w >= v:   # invalid edge
            return False
        graph[u].append(w)
        graph[w].append(u)

    visited = [False] * v

    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(v):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False

v, e = map(int, input("Enter V and E: ").split())
edges = [tuple(map(int, input().split())) for _ in range(e)]
print("true" if has_cycle(v, edges) else "false")