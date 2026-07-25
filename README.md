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
