% Facts

food(apple).
food(vegetables).

likes(johan, peanuts).

eats(anil, peanuts).

alive(anil).

% Rules

% Johan likes all kinds of food
likes(johan, X) :-
    food(X).

% Harry eats everything that Anil eats
eats(harry, X) :-
    eats(anil, X).

% Anything anyone eats and is not killed by is food
food(X) :-
    eats(Person, X),
    \+ kills(X, Person).

% Facts stating peanuts do not kill Anil
kills(peanuts, anil) :- fail.