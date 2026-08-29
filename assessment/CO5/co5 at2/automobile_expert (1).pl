% PROLOG-BASED AUTOMOBILE FAULT DIAGNOSIS EXPERT SYSTEM
% Student: S. Roshni (192525185)

:- dynamic symptom/1.

% Knowledge Base
fault(cooling_system_fault) :-
    symptom(overheating),
    symptom(low_coolant).

fault(battery_starting_fault) :-
    symptom(hard_start),
    symptom(weak_battery).

fault(belt_or_bearing_fault) :-
    symptom(abnormal_noise).

fault(fuel_efficiency_fault) :-
    symptom(low_mileage).

fault(engine_management_fault) :-
    symptom(check_engine_light).

% Diagnostic Actions
action(cooling_system_fault, check_coolant_and_leaks).
action(battery_starting_fault, test_battery_and_charging_system).
action(belt_or_bearing_fault, inspect_belt_and_bearings).
action(fuel_efficiency_fault, check_tyre_pressure_and_engine_tune).
action(engine_management_fault, scan_diagnostic_trouble_codes).

% Explanations
reason(cooling_system_fault,
       'Overheating and low coolant indicate a possible cooling-system fault.').
reason(battery_starting_fault,
       'Hard starting and a weak battery indicate a possible battery/starting fault.').
reason(belt_or_bearing_fault,
       'Abnormal noise suggests inspection of belts, pulleys or bearings.').
reason(fuel_efficiency_fault,
       'Low mileage suggests checking tyre pressure and engine tuning.').
reason(engine_management_fault,
       'Warning-light activation suggests scanning diagnostic trouble codes.').

% Main Diagnosis
diagnose(Fault, Action, Explanation) :-
    fault(Fault),
    action(Fault, Action),
    reason(Fault, Explanation).

% Forward Chaining
forward_chain(Fault) :-
    fault(Fault).

% Backward Chaining
backward_chain(Fault) :-
    fault(Fault).

% Symptom Management
clear_symptoms :-
    retractall(symptom(_)).

add_symptom(Symptom) :-
    assertz(symptom(Symptom)).

show_symptoms :-
    findall(S, symptom(S), List),
    format('Current symptoms: ~w~n', [List]).

% Demonstration
demo :-
    clear_symptoms,
    add_symptom(overheating),
    add_symptom(low_coolant),
    show_symptoms,
    diagnose(Fault, Action, Explanation),
    format('~nProbable Fault : ~w~n', [Fault]),
    format('Recommended Action : ~w~n', [Action]),
    format('Reason : ~w~n', [Explanation]).

% Sample queries:
% ?- [automobile_expert].
% ?- demo.
% ?- clear_symptoms, add_symptom(hard_start), add_symptom(weak_battery),
%    backward_chain(Fault).
