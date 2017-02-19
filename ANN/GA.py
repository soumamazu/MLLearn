"""This module contains the basic functional units of the Genetic Algorithm."""

from numpy import random
from Utils import random_clamped

class SGenome:
    """This class is a Single Genome."""
    def __init__(self, fitness=None, weights=None):
        if fitness is None:
            self.fitness = 0
        else:
            self.fitness = fitness
        if weights is None:
            self.weights = []
        else:
            self.weights = weights

class CGenAlg:
    """This class is the Genetic Algorithm."""
    def __init__(self, popSize, mutationRate, crossoverRate, numWeights):
        self.pop_size = popSize
        self.mutation_rate = mutationRate
        self.crossover_rate = crossoverRate
        self.chromo_length = numWeights
        self.total_fitness = 0
        self.generation_num = 0
        self.fittest_genome = 0
        self.best_fitness = 0
        self.worst_fitness = 99999999
        self.avergae_fitness = 0
        self.population = [SGenome(weights=random_clamped(self.chromo_length)) for count in range(self.pop_size)]

    def mutate(self, chromo):
        """This method mutates the chromosome randomly."""
        chromo[:] = [i if random.random() > self.mutation_rate else (i + random_clamped() * 0.3) for i in chromo]

    def get_chromo_roulette(self):
        """This method returns a chromo based on roulette wheel sampling."""
        fitness_so_far = 0
        for i in range(self.pop_size):
            fitness_so_far += self.population[i].fitness
            if fitness_so_far >= random.random() * self.total_fitness:
                return self.population[i]

    def crossover(self, mum, dad, son, daughter):
        """This method performs crossover according to the GAs crossover rate."""
        if random.random() > self.crossover_rate or mum == dad:
            son[:] = mum
            daughter[:] = dad
            return
        crossover_point = random.randint(0, self.chromo_length)
        son[:crossover_point] = mum[:crossover_point]
        daughter[:crossover_point] = dad[:crossover_point]
        son[crossover_point:] = dad[crossover_point:]
        daughter[crossover_point:] = mum[crossover_point:]

    def epoch(self):
        """This method returns a new population of chromosones."""
        #self.population = old_pop
        self.reset()
        self.population.sort(key=lambda x: x.fitness)
        self.calc_stats()
        new_pop = []
        if (4 * 1) % 2 == 0:
            self.grab_nbest(4, 1, new_pop)
        while len(new_pop) < self.pop_size:
            mum = self.get_chromo_roulette()
            dad = self.get_chromo_roulette()
            son = daughter = []
            self.crossover(mum.weights, dad.weights, son, daughter)
            self.mutate(son)
            self.mutate(daughter)
            new_pop.append(son)
            new_pop.append(daughter)
        self.population = new_pop
        return self.population

    def grab_nbest(self, nbest, ncopies, pop):
        """This method inserts copies of the NBest most fittest genomes into a population vector."""
        pop.append(self.population[(self.pop_size - 1) - nbest] for count in range(nbest * ncopies))

    def calc_stats(self):
        """This method calculates stats for the current generation."""
        self.total_fitness = 0
        highest_so_far = 0
        lowest_so_far = 9999999
        for i in range(self.pop_size):
            if self.population[i].fitness > highest_so_far:
                highest_so_far = self.population[i].fitness
                self.fittest_genome = i
                self.best_fitness = highest_so_far
            if self.population[i].fitness < lowest_so_far:
                lowest_so_far = self.population[i].fitness
                self.worst_fitness = lowest_so_far
            self.total_fitness += self.population[i].fitness
        self.avergae_fitness = self.total_fitness / self.pop_size

    def reset(self):
        """This method resets all the relevant variables ready for a new generation."""
        self.total_fitness = 0
        self.best_fitness = 0
        self.worst_fitness = 9999999
        self.avergae_fitness = 0
