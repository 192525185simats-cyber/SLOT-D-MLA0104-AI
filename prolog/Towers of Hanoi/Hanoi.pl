% Tower of Hanoi Program

move(1, Source, Destination, _) :-
    write('Move Disk 1 from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl.

move(N, Source, Destination, Auxiliary) :-
    N > 1,
    N1 is N - 1,
    move(N1, Source, Auxiliary, Destination),
    move(1, Source, Destination, _),
    move(N1, Auxiliary, Destination, Source).