# BFS and DFS - Undirected Graph
# Using Adjacency List and Recursive approach

from collections import deque

# ──Graph ───────────────────────────────────────────
graph={}

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

for i in range(1,n+1):
	graph[i]=[]
	
print(f"Enter {e} edges (e.g. 1 2):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)   # undirected

start = int(input("Enter starting node: "))


# ── DFS (Recursive) ───────────────────────────────────────
def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

# ── BFS (Recursive) ───────────────────────────────────────
def bfs(queue, visited):
    if not queue:
        return
    node = queue.popleft()
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    bfs(queue, visited)

# ── Run ───────────────────────────────────────────────────
print("Graph:", graph)

print("\nDFS Traversal (starting from node 1):")
dfs(start,set())

print("\n\nBFS Traversal (starting from node 1):")
visited = {start}
bfs(deque([start]),visited)
