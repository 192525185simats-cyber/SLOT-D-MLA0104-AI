EXPERIMENT1: 
##PSEUDO CODE OF BFS&DFS:

START

Create an empty graph

Input number of vertices (n)

Repeat n times
    Input vertex
    Input neighbours
    Store vertex and neighbours in graph
End Repeat

Input starting vertex

-------------------------
BFS Algorithm
-------------------------

Create empty visited list
Create queue
Insert starting vertex into queue

Print "BFS Traversal"

While queue is not empty
    Remove first element from queue → node

    If node is not visited
        Mark node as visited
        Print node

        For each neighbour of node
            Insert neighbour into queue
        End For
    End If
End While

-------------------------
DFS Algorithm
-------------------------

Create empty visited list

Function DFS(node)

    If node is not visited
        Mark node as visited
        Print node

        For each neighbour of node
            Call DFS(neighbour)
        End For
    End If

End Function

Print "DFS Traversal"

Call DFS(starting vertex)

STOP

##Uniform Cost Search (UCS) – Pseudocode
START

Read the graph
Read the start node
Read the goal node

Create a priority queue
Insert (0, start node) into the priority queue

Create an empty visited list

WHILE priority queue is not empty

    Remove the node with the minimum cost

    IF node is not visited THEN

        Mark the node as visited

        IF node is the goal node THEN
            Print "Goal Found"
            Print total cost
            STOP
        END IF

        FOR each neighbour of the current node
            Calculate new cost = current cost + edge cost
            Insert (new cost, neighbour) into the priority queue
        END FOR

    END IF

END WHILE

Print "Goal Not Found"

STOP

##A* Bearch

START

1. Create a priority queue.
2. Insert the start node with f = g + h.
3. Repeat until the queue is empty:
   a. Remove the node with the smallest f value.
   b. If it is the goal, print the path and cost.
   c. Mark the node as visited.
   d. Calculate g, h, and f for each neighbour.
   e. Insert neighbours into the priority queue.
4. If the goal is not found, print "Goal Not Found".

STOP

##GBFS

START

Read graph and heuristic values
Read start node and goal node

Create a priority queue
Insert start node

WHILE queue is not empty
    Remove node with smallest heuristic value
    Visit the node
    IF node is goal
        Print "Goal Found"
        STOP
    Add all unvisited neighbours to the priority queue
END WHILE

STOP

##Water jug problem

START

Read jug1, jug2 and target
Create a queue with initial state (0,0)

WHILE queue is not empty
    Remove a state
    IF target is found
        Print "Target Achieved"
        STOP
    Generate all possible next states:
        Fill Jug1
        Fill Jug2
        Empty Jug1
        Empty Jug2
        Pour Jug1 to Jug2
        Pour Jug2 to Jug1
    Add unvisited states to queue
END WHILE

STOP
Sum in Prolog:
pseudo code:
Algorithm: Sum of First N Natural Numbers (Using Recursion)

START

Function SUM(N)

    If N = 0 Then
        Return 0
    Else
        S1 ← SUM(N - 1)
        S ← S1 + N
        Return S
    End If

END Function

Read N
Result ← SUM(N)
Print Result

STOP
