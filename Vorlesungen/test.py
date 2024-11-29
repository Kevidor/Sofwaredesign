import itertools as itt

max_weight = 15
weights =  [12, 2, 1, 4, 1]
values =  [4, 2, 1, 10, 2]

valid_combinations = []
for r in range(1, len(weights) + 1):  # r gibt die Länge der Kombinationen an
    for combo in itt.combinations(weights, r):
        if sum(combo) <= max_weight:
            valid_combinations.append(combo)

print(valid_combinations)