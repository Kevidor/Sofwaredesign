import itertools as itt

def knapsack(values, weights, capacity):
    n = len(values)  # Anzahl der Objekte
    # Tabelle zur Speicherung der maximalen Werte
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Dynamische Programmierung, um die Tabelle zu füllen
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # Objekt passt in den Rucksack
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:  # Objekt passt nicht in den Rucksack
                dp[i][w] = dp[i - 1][w]
    
    # Maximaler Wert im Rucksack
    max_value = dp[n][capacity]
    
    # Objekte rekonstruieren
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Objekt wurde ausgewählt
            selected_items.append(i - 1)  # Index des Objekts
            w -= weights[i - 1]
    
    return max_value, selected_items

# Beispiel
max_weight = 15
weights =  [12, 2, 1, 4, 1]
values =  [4, 2, 1, 10, 2]

max_value, selected_items = knapsack(values, weights, max_weight)
print("Maximaler Wert:", max_value)
print("Ausgewählte Objekte:", selected_items)