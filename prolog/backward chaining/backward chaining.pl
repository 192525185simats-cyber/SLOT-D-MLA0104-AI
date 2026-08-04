% Facts

man(marcus).
pompeian(marcus).
ruler(caesar).

% Rules

roman(X) :-
    pompeian(X).

person(X) :-
    man(X).

loyal(X, caesar) :-
    roman(X).

hates(X, caesar) :-
    roman(X),
    \+ loyal(X, caesar).

assassinate(X, Y) :-
    person(X),
    ruler(Y),
    hates(X, Y).