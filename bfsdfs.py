from collections import deque

graph={}

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

for i in range(1,n+1):
	graph[i]=[]
	
print(f"Enter {e} edges (e.g. 1 2):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting node: "))

def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

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

print("Graph:", graph)

print("\nDFS Traversal:")
dfs(start,set())

print("\n\nBFS Traversal:")
visited = {start}
bfs(deque([start]),visited)
