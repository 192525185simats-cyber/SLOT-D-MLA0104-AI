% Facts

man(marcus).
pompeian(marcus).
roman(marcus).

ruler(caesar).

tried_to_assassinate(marcus, caesar).

% Rules

% All Pompeians are Romans
roman(X) :-
    pompeian(X).

% All men are people
person(X) :-
    man(X).

% All Romans are either loyal to Caesar or hate Caesar
loyal_to(X, caesar) :-
    roman(X),
    \+ hates(X, caesar).

hates(X, caesar) :-
    roman(X),
    \+ loyal_to(X, caesar).

% Everyone is loyal to someone
loyal_to(X, someone) :-
    person(X).

% People only try to assassinate rulers they are not loyal to
not_loyal_to(X, Y) :-
    tried_to_assassinate(X, Y).

not_loyal_to(X, Y) :-
    \+ loyal_to(X, Y).

assassin(X, Y) :-
    person(X),
    ruler(Y),
    tried_to_assassinate(X, Y),
    not_loyal_to(X, Y).