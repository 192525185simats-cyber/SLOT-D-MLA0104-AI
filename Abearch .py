import heapq

graph = {}
heuristic = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    h = int(input("Enter heuristic value: "))
    heuristic[vertex] = h

    m = int(input("Enter number of neighbours: "))
    neighbours = []

    for j in range(m):
        node = input("Neighbour: ")
        cost = int(input("Cost: "))
        neighbours.append((node, cost))

    graph[vertex] = neighbours

start = input("Enter start node: ")
goal = input("Enter goal node: ")

queue = [(heuristic[start], 0, start, [start])]
visited = []

while queue:
    f, g, node, path = heapq.heappop(queue)

    if node in visited:
        continue

    visited.append(node)

    if node == goal:
        print("Path:", " -> ".join(path))
        print("Total Cost:", g)
        break

    for neighbour, cost in graph[node]:
        if neighbour not in visited:
            new_g = g + cost
            new_f = new_g + heuristic[neighbour]
            heapq.heappush(queue, (new_f, new_g, neighbour, path + [neighbour]))
