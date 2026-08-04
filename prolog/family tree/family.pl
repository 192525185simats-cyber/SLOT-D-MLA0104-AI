% Gender Facts

male(tom).
male(bob).
male(jim).

female(pam).
female(liz).
female(ann).
female(pat).

% Parent Facts

parent(pam,bob).
parent(tom,bob).

parent(bob,ann).
parent(liz,ann).

parent(ann,jim).
parent(pat,jim).

% Rules

father(X,Y) :-
    male(X),
    parent(X,Y).

mother(X,Y) :-
    female(X),
    parent(X,Y).

grandfather(X,Y) :-
    male(X),
    parent(X,Z),
    parent(Z,Y).

grandmother(X,Y) :-
    female(X),
    parent(X,Z),
    parent(Z,Y).

brother(X,Y) :-
    male(X),
    parent(P,X),
    parent(P,Y),
    X \= Y.

sister(X,Y) :-
    female(X),
    parent(P,X),
    parent(P,Y),
    X \= Y.