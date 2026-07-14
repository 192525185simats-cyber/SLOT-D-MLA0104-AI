from collections import deque

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    neighbours = input("Enter neighbours (space separated): ").split()
    graph[vertex] = neighbours

start = input("Enter starting vertex: ")
visited = []
queue = deque([start])

print("BFS Traversal:", end=" ")

while queue:
    node = queue.popleft()

    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        for i in graph[node]:
            queue.append(i)
visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        for i in graph[node]:
            dfs(i)

print("\nDFS Traversal:", end=" ")
dfs(start)
