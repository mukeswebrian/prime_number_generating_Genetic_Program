import individual
import primality_checker as custom_engine
eng = custom_engine.Checker()

class Population():
    
    def __init__(self, init_population_size, a_range, min_depth, max_depth, pset):
        
        # fitness of the fittest individual in the population (intialized as 0)
        self.max_fitness = 0
        
        # create a population of tree individuals
        self.population = {}
        for i in range(0, init_population_size):
            self.population[i] = individual.Individual(a_range, pset, min_depth, max_depth)
            self.population[i].make_tree()
            self.population[i].calc_fitness(eng)
     
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
		
    def replace_individual(self, ind_id, new_ind):
        self.population[ind_id] = new_ind
    
    def describe(self):
        
        print('Fitness : indiviual')	
        for key in self.population.keys():
            print(str(self.population[key].fitness) +' : '+ self.population[key].describe())