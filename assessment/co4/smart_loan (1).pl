% SMART LOAN APPROVAL SYSTEM
% Decision Tree Style Implementation in Prolog

% ------------------------------------------------
% LOAN DATA
% ------------------------------------------------

loan(1, 60000, 780, employed, 250000, good, approved).
loan(2, 25000, 580, unemployed, 500000, poor, rejected).
loan(3, 50000, 720, employed, 200000, good, approved).
loan(4, 35000, 650, self_employed, 300000, average, approved).
loan(5, 20000, 550, unemployed, 400000, poor, rejected).
loan(6, 75000, 800, employed, 300000, good, approved).
loan(7, 45000, 680, employed, 350000, average, approved).
loan(8, 30000, 590, self_employed, 450000, poor, rejected).
loan(9, 90000, 820, employed, 400000, good, approved).
loan(10, 28000, 600, unemployed, 250000, poor, rejected).

% ------------------------------------------------
% GINI INDEX
% ------------------------------------------------

gini(Approved, Rejected, Gini) :-
    Total is Approved + Rejected,
    Total > 0,
    PA is Approved / Total,
    PR is Rejected / Total,
    Gini is 1 - (PA * PA + PR * PR).

% ------------------------------------------------
% DECISION TREE RULES
% ------------------------------------------------

loan_decision(Income, Credit, Employment,
              Amount, Repayment, approved) :-

    Credit >= 700,
    Repayment = good,
    Income >= 40000,
    Amount =< Income * 6.

loan_decision(Income, Credit, Employment,
              Amount, Repayment, approved) :-

    Credit >= 650,
    Repayment = good,
    Employment \= unemployed,
    Income >= 35000,
    Amount =< Income * 7.

loan_decision(_, Credit, _, _, _, rejected) :-
    Credit < 650.

loan_decision(_, _, _, _, poor, rejected).

loan_decision(Income, _, _, _, _, rejected) :-
    Income < 30000.

loan_decision(Income, _, _, Amount, _, rejected) :-
    Amount > Income * 8.

% ------------------------------------------------
% PREDICTION
% ------------------------------------------------

predict_loan(Income, Credit, Employment,
             Amount, Repayment, Result) :-

    loan_decision(
        Income,
        Credit,
        Employment,
        Amount,
        Repayment,
        Result
    ).

% ------------------------------------------------
% SAMPLE TEST
% ------------------------------------------------

test :-

    predict_loan(
        60000,
        780,
        employed,
        250000,
        good,
        R1
    ),

    write('Customer 1: '),
    write(R1),
    nl,

    predict_loan(
        25000,
        580,
        unemployed,
        500000,
        poor,
        R2
    ),

    write('Customer 2: '),
    write(R2),
    nl,

    predict_loan(
        50000,
        720,
        employed,
        200000,
        good,
        R3
    ),

    write('Customer 3: '),
    write(R3),
    nl.

% ------------------------------------------------
% GINI TEST
% ------------------------------------------------

gini_example :-

    gini(6, 4, G),

    write('Gini Index = '),
    write(G),
    nl.
