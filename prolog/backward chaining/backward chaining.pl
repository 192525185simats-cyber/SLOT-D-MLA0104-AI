% Backward Chaining Example

parent(john, mary).
parent(mary, sam).
parent(sam, david).

ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).