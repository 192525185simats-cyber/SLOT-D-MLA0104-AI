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
