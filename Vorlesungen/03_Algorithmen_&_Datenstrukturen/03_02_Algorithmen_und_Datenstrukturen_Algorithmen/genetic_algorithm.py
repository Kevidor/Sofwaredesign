from functools import partial
from collections import namedtuple
from random import choices, randint, randrange, random
from typing import List, Callable, Tuple

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]

Thing = namedtuple('Thing', ['value', 'weight'])
things = []


def generate_genome(lenght: int) -> Genome:
    return choices([0, 1], k=lenght)

def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]

def fitness(genome: Genome, things: List[Thing], weight_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("genome and things must be of the same lenght")
    
    weight = 0
    value = 0

    for i, things in enumerate(things):
        if genome[i] == 1:
            weight += things.weight
            value += things.value

            if weight > weight_limit:
                return 0
    return value

def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2
    )

def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genome a and b must be of same length")
    
    length = len(a)
    if length < 2:
        return a, b

    p = randint(1, length -1)
    return a[0:p] + b[p:], b[0:p] + a[p:]

def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
    return genome

def run_evolution(
        populate_func: PopulateFunc,
        fitness_func: FitnessFunc,
        fitness_limit: int,
        selection_func: SelectionFunc = selection_pair,
        crossover_func: CrossoverFunc = single_point_crossover,
        mutation_func: MutationFunc = mutation,
        generation_limit: int = 100
    ) -> Tuple[Population, int]:
    population = populate_func()

    for i in range(generation_limit):
        population = sorted(population, key= lambda genome: fitness_func(genome), reverse= True)

        # if fitness_func(population[0]) >= fitness_limit:
            # break

        next_generation = population[0:2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]

        population = next_generation

    return [population, i]
    

max_weight = 850
weights = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0, 42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71, 3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]
values = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147, 78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28, 87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276, 312]

for i, j in zip(values, weights):
    things.append(Thing(i, j))

population, generation = run_evolution(
    populate_func=partial(
        generate_population, size= 10, genome_length= len(things)
    ),
    fitness_func=partial(
        fitness, things=things, weight_limit=max_weight
    ),
    fitness_limit=sum(weights),
    generation_limit=100
)

def genome_to_things(genome: Genome, things: List[Thing]) -> List[Thing]:
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing]
    
    return result

print(f"Numbers of Gens: {generation}")
print(f"Best Solution: {genome_to_things(population[0], things)}")
