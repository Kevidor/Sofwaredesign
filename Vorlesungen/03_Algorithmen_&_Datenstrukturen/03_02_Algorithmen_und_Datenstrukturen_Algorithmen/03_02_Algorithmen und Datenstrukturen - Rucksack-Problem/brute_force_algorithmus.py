from itertools import combinations

class Objekt():
    _idx_counter = 0
    def __init__(self, weight, value) -> None:
        self.weight = weight
        self.value = value
        self.idx = Objekt._idx_counter
        Objekt._idx_counter += 1

    def __str__(self) -> str:
        return f"Objekt mit Index: {self.idx}, Weight: {self.weight} und Value: {self.value}"
    
    def __repr__(self) -> str:
        return f"Objekt_{self.idx}(Weight: {self.weight}, Value: {self.value})"
    
def brute_force(objects: list[Objekt]) -> tuple[int, list[Objekt]]:
    best_value = 0
    best_combo = []
    for i in range(1, len(objekte)):
        for comb in combinations(objekte, i):
            test_weight = 0
            test_value = 0
            for obj in comb:
                if test_weight + obj.weight <= max_weight:
                    test_weight += obj.weight
                    test_value += obj.value
                    
            if test_value > best_value:
                best_value = test_value
                best_combo = comb
    return (best_value, best_combo)

max_weight = 15
weights =  [12, 2, 1, 4, 1]
values =  [4, 2, 1, 10, 2]

objekte = [Objekt(wei, val) for wei, val in zip(weights, values)]
best_value, best_combo = brute_force(objekte)

print(f"Value: {best_value} mit der Combo {best_combo}")

        