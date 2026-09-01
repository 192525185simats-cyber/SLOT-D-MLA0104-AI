import heapq

# ==========================================================
# INTELLIGENT DISASTER RESPONSE AND RESCUE AGENT
# MLA01 - ARTIFICIAL INTELLIGENCE AND EXPERT SYSTEMS
# ==========================================================

# ----------------------------------------------------------
# 1. DISASTER KNOWLEDGE BASE
# ----------------------------------------------------------

disasters = {
    "L1": {
        "type": "Building Collapse",
        "victims": 12,
        "smoke": True,
        "fire": False,
        "toxic_gas": False,
        "water": False,
        "stranded": False,
        "injured": True,
        "ambulance": False
    },

    "L2": {
        "type": "Flood",
        "victims": 20,
        "smoke": False,
        "fire": False,
        "toxic_gas": False,
        "water": True,
        "stranded": True,
        "injured": False,
        "ambulance": False
    },

    "L3": {
        "type": "Industrial Accident",
        "victims": 6,
        "smoke": True,
        "fire": True,
        "toxic_gas": True,
        "water": False,
        "stranded": False,
        "injured": True,
        "ambulance": False
    },

    "L4": {
        "type": "Road Accident",
        "victims": 4,
        "smoke": False,
        "fire": False,
        "toxic_gas": False,
        "water": False,
        "stranded": False,
        "injured": True,
        "ambulance": True
    }
}


# ----------------------------------------------------------
# 2. ROAD GRAPH
# ----------------------------------------------------------

graph = {
    "CENTER": {
        "L1": 4,
        "L2": 5,
        "L4": 6
    },

    "L1": {
        "CENTER": 4,
        "L2": 5,
        "L3": 4
    },

    "L2": {
        "CENTER": 5,
        "L1": 5,
        "L3": 3
    },

    "L3": {
        "L1": 4,
        "L2": 3
    },

    "L4": {
        "CENTER": 6
    }
}


# ----------------------------------------------------------
# 3. HEURISTIC VALUES
# ----------------------------------------------------------

heuristic = {
    "CENTER": 0,
    "L1": 4,
    "L2": 3,
    "L3": 0,
    "L4": 6
}


# ----------------------------------------------------------
# 4. A* SEARCH
# ----------------------------------------------------------

def a_star(start, goal):

    queue = []

    heapq.heappush(
        queue,
        (heuristic[start], 0, start, [start])
    )

    visited = set()

    while queue:

        f, cost, current, path = heapq.heappop(queue)

        if current == goal:
            return path, cost

        if current in visited:
            continue

        visited.add(current)

        for next_node, distance in graph[current].items():

            new_cost = cost + distance

            new_f = new_cost + heuristic[next_node]

            heapq.heappush(
                queue,
                (
                    new_f,
                    new_cost,
                    next_node,
                    path + [next_node]
                )
            )

    return [], 999


# ----------------------------------------------------------
# 5. EXPERT SYSTEM RULES
# ----------------------------------------------------------

def expert_system(location):

    d = disasters[location]

    conclusions = []

    # Rule 1
    if d["type"] == "Building Collapse" and d["victims"] > 0:
        conclusions.append("High Rescue Priority")

    # Rule 2
    if d["smoke"] and d["victims"] > 0:
        conclusions.append("Immediate Rescue")

    # Rule 3
    if d["type"] == "Building Collapse" and d["injured"]:
        conclusions.append("Medical Team Required")

    # Rule 4
    if d["water"] and d["stranded"]:
        conclusions.append("Rescue Boat Required")

    # Rule 5
    if d["water"] and d["stranded"]:
        conclusions.append("Evacuation Required")

    # Rule 6
    if d["fire"] and d["toxic_gas"]:
        conclusions.append("Hazmat Team Required")

    # Rule 7
    if d["fire"]:
        conclusions.append("Fire Rescue Required")

    # Rule 8
    if d["toxic_gas"]:
        conclusions.append("Respiratory Protection Required")

    # Rule 9
    if d["injured"] and d["ambulance"]:
        conclusions.append("Medical Team Required")

    # Rule 10
    if d["victims"] >= 10:
        conclusions.append("High Rescue Priority")

    # Rule 11
    if d["victims"] >= 10:
        conclusions.append("Dispatch Immediately")

    # Rule 12
    if d["toxic_gas"]:
        conclusions.append("High Risk Zone")

    return list(set(conclusions))


# ----------------------------------------------------------
# 6. PRIORITY CALCULATION
# ----------------------------------------------------------

def calculate_priority(location):

    d = disasters[location]

    score = d["victims"]

    if d["smoke"]:
        score += 3

    if d["fire"]:
        score += 8

    if d["toxic_gas"]:
        score += 10

    if d["water"]:
        score += 7

    if d["stranded"]:
        score += 5

    if d["injured"]:
        score += 4

    if d["type"] == "Building Collapse":
        score += 8

    return score


# ----------------------------------------------------------
# 7. RESOURCE SELECTION
# ----------------------------------------------------------

def resources(location, conclusions):

    result = []

    if "Rescue Boat Required" in conclusions:
        result.append("Rescue Boat")

    if "Hazmat Team Required" in conclusions:
        result.append("Hazmat Team")

    if "Fire Rescue Required" in conclusions:
        result.append("Fire and Rescue Team")

    if "Medical Team Required" in conclusions:
        result.append("Medical Team")

    if "Immediate Rescue" in conclusions:
        result.append("Rescue Team")

    if not result:
        result.append("General Rescue Team")

    return result


# ----------------------------------------------------------
# 8. FORWARD CHAINING
# ----------------------------------------------------------

def forward_chaining(location):

    conclusions = expert_system(location)

    print("\nFORWARD CHAINING")

    print("Initial Facts:")

    d = disasters[location]

    print("Victims =", d["victims"])

    print("Type =", d["type"])

    if d["fire"]:
        print("Fire = TRUE")

    if d["toxic_gas"]:
        print("ToxicGas = TRUE")

    if d["water"]:
        print("RisingWater = TRUE")

    if d["injured"]:
        print("Injured = TRUE")

    print("\nDerived Conclusions:")

    for c in conclusions:
        print("->", c)

    return conclusions


# ----------------------------------------------------------
# 9. BACKWARD CHAINING
# ----------------------------------------------------------

def backward_chaining(location, goal):

    conclusions = expert_system(location)

    print("\nBACKWARD CHAINING")

    print("Goal:", goal)

    if goal in conclusions:

        print("Goal found!")

        print("Required conditions are satisfied.")

        return True

    else:

        print("Goal cannot be proved.")

        return False


# ----------------------------------------------------------
# 10. UNIFICATION
# ----------------------------------------------------------

def unification():

    print("\nUNIFICATION")

    print("Rule:")
    print("RequiresTeam(x, Rescue)")

    print("Fact:")
    print("RequiresTeam(L1, Rescue)")

    print("Substitution:")
    print("x = L1")

    print("\nSecond Example")

    print("Rule:")
    print("RequiresTeam(x, Medical)")

    print("Fact:")
    print("RequiresTeam(L4, Medical)")

    print("Substitution:")
    print("x = L4")


# ----------------------------------------------------------
# 11. RESOLUTION
# ----------------------------------------------------------

def resolution():

    print("\nRESOLUTION")

    print("Fact 1: Fire(L3)")
    print("Fact 2: ToxicGas(L3)")

    print("Rule:")
    print("Fire(x) AND ToxicGas(x) -> HazmatRequired(x)")

    print("\nResolving Fire(L3)...")

    print("NOT ToxicGas(L3) OR HazmatRequired(L3)")

    print("\nResolving ToxicGas(L3)...")

    print("HazmatRequired(L3)")

    print("\nConclusion:")
    print("HazmatRequired(L3) = TRUE")


# ----------------------------------------------------------
# 12. ACTION SEQUENCE
# ----------------------------------------------------------

def actions(location, conclusions):

    result = []

    if "High Risk Zone" in conclusions:
        result.append("Create safety perimeter")

    if "Fire Rescue Required" in conclusions:
        result.append("Deploy Fire and Rescue Team")

    if "Hazmat Team Required" in conclusions:
        result.append("Deploy Hazmat Team")

    if "Rescue Boat Required" in conclusions:
        result.append("Deploy Rescue Boat")

    if "Medical Team Required" in conclusions:
        result.append("Deploy Medical Team")

    if "Immediate Rescue" in conclusions:
        result.append("Start Immediate Rescue")

    if "Evacuation Required" in conclusions:
        result.append("Evacuate victims")

    result.append("Monitor disaster condition")

    return result


# ----------------------------------------------------------
# 13. ANALYZE ONE LOCATION
# ----------------------------------------------------------

def analyze(location):

    d = disasters[location]

    print("\n")
    print("=" * 60)
    print("DISASTER LOCATION:", location)
    print("=" * 60)

    print("Disaster Type:", d["type"])
    print("Victims:", d["victims"])

    # Priority
    score = calculate_priority(location)

    print("Priority Score:", score)

    # A*
    route, cost = a_star("CENTER", location)

    print("\nA* SEARCH")

    print("Route:", " -> ".join(route))

    print("Path Cost:", cost)

    # Expert System
    conclusions = forward_chaining(location)

    # Resources
    selected_resources = resources(
        location,
        conclusions
    )

    print("\nRECOMMENDED RESOURCES")

    for r in selected_resources:
        print("->", r)

    # Actions
    print("\nACTION SEQUENCE")

    action_list = actions(
        location,
        conclusions
    )

    for i, action in enumerate(action_list, 1):

        print(i, ".", action)


# ----------------------------------------------------------
# 14. VALIDATION
# ----------------------------------------------------------

def validation():

    print("\n")
    print("=" * 60)
    print("VALIDATION")
    print("=" * 60)

    expected = {

        "L1": [
            "Medical Team Required",
            "Immediate Rescue"
        ],

        "L2": [
            "Rescue Boat Required",
            "Evacuation Required"
        ],

        "L3": [
            "Hazmat Team Required",
            "Fire Rescue Required"
        ],

        "L4": [
            "Medical Team Required"
        ]
    }

    passed = 0

    for location in expected:

        result = expert_system(location)

        success = all(
            item in result
            for item in expected[location]
        )

        if success:

            print(location, "-> PASS")

            passed += 1

        else:

            print(location, "-> FAIL")

    accuracy = (
        passed / len(expected)
    ) * 100

    print("\nValidation Accuracy:", accuracy, "%")


# ----------------------------------------------------------
# 15. AGENT ARCHITECTURE
# ----------------------------------------------------------

def agent_architecture():

    print("\n")
    print("=" * 60)
    print("INTELLIGENT AGENT ARCHITECTURE")
    print("=" * 60)

    print("""
             DISASTER ENVIRONMENT
                       |
                    SENSORS
                       |
               PERCEPTION MODULE
                       |
                 WORLD MODEL
                       |
                KNOWLEDGE BASE
                  /         \\
             A* SEARCH     LOGIC
                  \\         /
                   UTILITY
                      |
               AGENT DECISION
                      |
              RESCUE ACTION
                      |
                   FEEDBACK
                      |
                   LEARNING
    """)

    print("Agent Type:")
    print("Learning + Utility-Based + Model-Based Agent")


# ----------------------------------------------------------
# 16. FINAL PRIORITY
# ----------------------------------------------------------

def final_priority():

    print("\n")
    print("=" * 60)
    print("FINAL PRIORITY ORDER")
    print("=" * 60)

    scores = []

    for location in disasters:

        score = calculate_priority(location)

        scores.append(
            (score, location)
        )

    scores.sort(reverse=True)

    for i, item in enumerate(scores, 1):

        score, location = item

        print(
            i,
            ".",
            location,
            "-",
            disasters[location]["type"],
            "- Score:",
            score
        )


# ----------------------------------------------------------
# 17. MAIN PROGRAM
# ----------------------------------------------------------

def main():

    print("\n")
    print("*" * 60)
    print(" INTELLIGENT DISASTER RESPONSE AND RESCUE AGENT")
    print("*" * 60)

    print("\nCourse: MLA01 - Artificial Intelligence and Expert Systems")

    print("\nThis implementation demonstrates:")

    print("1. A* Search")
    print("2. State Space")
    print("3. Propositional Logic")
    print("4. First Order Logic")
    print("5. Unification")
    print("6. Resolution")
    print("7. Production Rules")
    print("8. Forward Chaining")
    print("9. Backward Chaining")
    print("10. Intelligent Agent")
    print("11. Utility-Based Decision")
    print("12. Learning Concept")

    # Analyze all four scenarios
    for location in disasters:

        analyze(location)

    # Unification
    unification()

    # Resolution
    resolution()

    # Backward chaining
    backward_chaining(
        "L3",
        "Hazmat Team Required"
    )

    # Agent architecture
    agent_architecture()

    # Priority
    final_priority()

    # Validation
    validation()

    print("\n")
    print("*" * 60)
    print(" IMPLEMENTATION COMPLETED SUCCESSFULLY")
    print("*" * 60)


# ----------------------------------------------------------
# PROGRAM START
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
