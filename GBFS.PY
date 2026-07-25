import heapq

graph = {}
heuristic = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    heuristic[vertex] = int(input("Enter heuristic value: "))

    m = int(input("Enter number of neighbours: "))
    neighbours = []

    for j in range(m):
        neighbour = input("Neighbour: ")
        neighbours.append(neighbour)

    graph[vertex] = neighbours

start = input("Enter start node: ")
goal = input("Enter goal node: ")

queue = [(heuristic[start], start)]
visited = []

print("Greedy Best First Search Traversal:", end=" ")

while queue:
    h, node = heapq.heappop(queue)

    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            break

        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(queue, (heuristic[neighbour], neighbour))
