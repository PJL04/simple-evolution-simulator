import random
import matplotlib.pyplot as plt

class Organism:
    def __init__(self, genotype):
        self.genotype = genotype
        self.weight, self.height = self.calculate_phenotype(genotype)
        self.fitness = self.calculate_fitness()

    def calculate_phenotype(self, genotype):
        # Quadratic mapping: 
        #   weight = 2 * genotype^2 +1
        #   height = 3 * genotype^2 +2
        weight = 2 * genotype ** 2 + 1
        height = 3 * genotype ** 2 + 2
        return weight, height

    def calculate_fitness(self):
        # Simple way: Fitness = weight + height
        fitness = self.weight + self.height
        return fitness

POPULATION_SIZE = 50

def create_population():
    
    population = []

    for _ in range(POPULATION_SIZE):
        genotype = random.uniform(0, 1)     # Genotype is a float between 0 and 1
        organism = Organism(genotype)
        population.append(organism)
    return population

def selection(population):
    sorted_population = sorted(population, key=lambda x: x.fitness, reverse=True)
    surviving_parents = sorted_population[:POPULATION_SIZE // 2]

    # Reproduction
    children = []
    for _ in range(POPULATION_SIZE // 2):
        parent1 = random.choice(surviving_parents)
        parent2 = random.choice(surviving_parents)

        # Crossover
        child_genotype = (parent1.genotype + parent2.genotype) / 2

        # Mutation
        mutation_rate = 0.1
        if random.random() < mutation_rate:
            child_genotype += random.uniform(-0.1, 0.1)

        child = Organism(child_genotype)
        children.append(child)

    # Combine surviving parents and children to create the new population
    new_population = surviving_parents + children
    return new_population

NUM_GENERATIONS = 15

def main():
    population = create_population()

    generations = [0]
    weights_by_generation = [[organism.weight for organism in population]]
    heights_by_generation = [[organism.height for organism in population]]
    genotypes_by_generation = [[organism.genotype for organism in population]]
    fitness_by_generation = [sum(organism.fitness for organism in population) / len(population)]  # Store average fitness

    for generation in range(1, NUM_GENERATIONS + 1):
        for organism in population:
            print(f"Generation: {generation}, Genotype: {organism.genotype:.2f}, Weight: {organism.weight:.2f}, Height: {organism.height:.2f}")

        population = selection(population)

        # Append values for the current generation
        generations.append(generation)
        genotypes_by_generation.append([organism.genotype for organism in population])
        weights_by_generation.append([organism.weight for organism in population])
        heights_by_generation.append([organism.height for organism in population])
        fitness_by_generation.append(sum(organism.fitness for organism in population) / len(population))  # Store average fitness

    # Visualization: Line plot of average values over generations
    plt.figure(figsize=(10, 6))
    plt.plot(generations, [sum(genotypes) / len(genotypes) for genotypes in genotypes_by_generation], label="Average Genotype")
    plt.plot(generations, [sum(weights) / len(weights) for weights in weights_by_generation], label="Average Weight")
    plt.plot(generations, [sum(heights) / len(heights) for heights in heights_by_generation], label="Average Height")
    plt.plot(generations, fitness_by_generation, label="Average Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Average Value")
    plt.title("Evolution Simulator - Average Genotype, Weight, Height, and Fitness over Generations")
    plt.legend()
    plt.savefig("evolution.png")

if __name__ == "__main__":
    main()
