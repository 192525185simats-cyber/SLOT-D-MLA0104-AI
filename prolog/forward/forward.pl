% Forward Chaining Example

human(socrates).
human(roshni).
human(rahul).

mortal(X) :-
    human(X).