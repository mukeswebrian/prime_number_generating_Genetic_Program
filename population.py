import individual

class Population():
    
    def __init__(self, init_population_size, a_range, b_range, min_depth, max_depth, pset):
        
        # fitness of the fittest individual in the population (intialized as 0)
        self.max_fitness = 0
        
        # create a population of tree individuals
        self.population = {}
        for i in range(0, init_population_size):
            self.population[i] = individual.Individual(a_range, b_range, pset, min_depth, max_depth)
            self.population[i].make_tree()
     
    def get_all(self):
        return self.population   
    
    def get_individual(self, index):
        return self.population[index]
        
        
    def add_individual(self, ind1):
        
        next_id = max(self.population.keys()) + 1
        self.population[next_id] = ind1
        
    def remove_individual(self, ind_id):
        self.population.pop(ind_id)
        
    def get_size(self):
        return len(self.population)
    
    def describe(self):
        for key in self.population.keys():
            print(str(key) +' : '+ self.population[key].describe())