from random import choices, randint, randrange, random
from typing import List

class Objekt:
    """Represents an object with weight, value, and an auto-incrementing index."""
    _idx_counter = 0

    def __init__(self, weight: int, value: int) -> None:
        """Initialize an Objekt with weight, value, and a unique index.

        Args:
            weight (int): The weight of the object.
            value (int): The value of the object.
        """
        self.weight = weight
        self.value = value
        self.idx = Objekt._idx_counter
        Objekt._idx_counter += 1

    def __str__(self) -> str:
        """String representation of the object."""
        return f"Objekt mit Index: {self.idx}, Weight: {self.weight} und Value: {self.value}"
    
    def __repr__(self) -> str:
        """Detailed representation of the object."""
        return f"Objekt_{self.idx}(Weight: {self.weight}, Value: {self.value})"

def generate_genome(length: int) -> List[int]:
    """Generate a random genome (list of 0s and 1s).

    Args:
        length (int): Length of the genome.

    Returns:
        list[int]: Genome as a list of 1s and 0s.
    """
    return choices([0, 1], k=length)

def generate_population(size: int, genome_length: int) -> List[List[int]]:
    """Generate an initial population of genomes.

    Args:
        size (int): Number of genomes in the population.
        genome_length (int): Length of each genome.

    Returns:
        list[list[int]]: A population represented as a list of genomes.
    """
    return [generate_genome(genome_length) for _ in range(size)]

def fitness(genome: List[int]) -> int:
    """Calculate the fitness of a genome based on selected objects.

    Args:
        genome (list[int]): The genome representing selected objects.

    Returns:
        int: Total value of selected objects if weight constraint is satisfied; otherwise, 0.
    """
    total_weight = sum(obj.weight for i, obj in enumerate(objects) if genome[i] == 1)
    total_value = sum(obj.value for i, obj in enumerate(objects) if genome[i] == 1)
    return total_value if total_weight <= max_weight else 0

def select_parents(population: List[List[int]]) -> List[List[int]]:
    """Select two parents from the population based on their fitness.

    Args:
        population (list[list[int]]): The current population.

    Returns:
        list[list[int]]: Two genomes selected as parents.
    """
    fitness_scores = [fitness(genome) for genome in population]
    return choices(population, weights=fitness_scores, k=2)

def crossover(parent1: List[int], parent2: List[int]) -> List[List[int]]:
    """Perform single-point crossover on two parent genomes.

    Args:
        parent1 (list[int]): The first parent genome.
        parent2 (list[int]): The second parent genome.

    Returns:
        list[list[int]]: Two child genomes resulting from the crossover.
    """
    if len(parent1) < 2:
        return parent1, parent2
    point = randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def mutate(genome: List[int], probability: float = 0.1) -> List[int]:
    """Mutate a genome by flipping bits with a certain probability.

    Args:
        genome (list[int]): The genome to mutate.
        probability (float): The probability of mutation for each bit.

    Returns:
        list[int]: The mutated genome.
    """
    for i in range(len(genome)):
        if random() < probability:
            genome[i] = 1 - genome[i]  # Flip 0 to 1 or 1 to 0
    return genome

def genetic_algorithm(pop_size: int, genome_length: int, generations: int) -> List[int]:
    """Run the genetic algorithm to find the optimal solution.

    Args:
        pop_size (int): Size of the population.
        genome_length (int): Length of each genome.
        generations (int): Number of generations to run.

    Returns:
        list[int]: The best genome found by the algorithm.
    """
    population = generate_population(pop_size, genome_length)
    for generation in range(generations):
        # Sort population by fitness
        population = sorted(population, key=fitness, reverse=True)
        # Keep the best individuals
        next_gen = population[:2]
        # Generate the next generation
        for _ in range(len(population) // 2 - 1):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            next_gen += [mutate(child1), mutate(child2)]
        population = next_gen
    return population[0]  # Return the best genome

# Create a list of Objekt instances
weights = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0, 42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71, 3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]
values = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147, 78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28, 87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276, 312]
objects = [Objekt(weight, value) for weight, value in zip(weights, values)]

# Parameters
max_weight = 850  # Maximum weight the knapsack can carry

# Run the algorithm
best_genome = genetic_algorithm(10, len(objects), 100)

# Decode the best genome into selected objects
selected_objects = [obj for i, obj in enumerate(objects) if best_genome[i] == 1]

print("Best solution:")
for obj in selected_objects:
    print(obj)
print("Total value:", sum(obj.value for obj in selected_objects))
print("Total weight:", sum(obj.weight for obj in selected_objects))
