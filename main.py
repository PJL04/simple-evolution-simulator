# TODO Change self.phenotype = genotype

import random

class Organism:
    def __init__(self, genotype):
        self.genotype = genotype
        # In more complex simulations, phenotype could be calculated based on the genotype through some function or mapping.
        self.phenotype = genotype # For the sake of simplicity the 'phenotype' is considered to be the same as the 'genotype'. 

POPULATION_SIZE = 50

def create_population():
    
    population = []

    for _ in range(POPULATION_SIZE):
        genotype = random.uniform(0, 1)     # Genotype is a float between 0 and 1
        organism = Organism(genotype)
        population.append(organism)
    return population

def selection(population):
    sorted_population = sorted(population, key=lambda x: x.genotype, reverse=True)
    surviving_parents = sorted_population[:POPULATION_SIZE // 2]

    # Reproduction
    children = []
    for parent in surviving_parents:
        child_genotype = parent.genotype + random.uniform(-0.1, 0.1)
        child = Organism(child_genotype)
        children.append(child)

    # Combine survivibg parents and children to create the new population
    new_population = surviving_parents + children
    return new_population

NUM_GENERATIONS = 15

def main():
    population = create_population()

    for generation in range(NUM_GENERATIONS):
        print(f"Generation {generation}")

        for organism in population:
            print(f"Genotype: {organism.genotype:.2f}, Phenotype: {organism.phenotype:.2f}")

        population = selection(population)

if __name__ == "__main__":
    main()
