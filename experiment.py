from population import Population
from primitive import Primitive as pm
import evolution
import random
import primality_checker as custom_engine
eng = custom_engine.Checker()

class Experiment():
    
    def __init__(self, 
                 exp_id, 
                 max_iter=3, 
                 f_threshold=0.75, 
                 p_size=6, 
                 k_max=20, 
                 min_depth=1, 
                 max_depth=4, 
                 a_range=(1,9), 
                 b_range=(1,9),
                 p_mutate=0.1,
                 calc_eng=None):
        
        # initalize experiment variables
        self.exp_id = exp_id # experiemnt id
        self.max_iter = max_iter # maximum number of generations allowed
        self.f_threshold = f_threshold # terminate early if the max_fitness exceeds f_threshold. (specified as a percentage of k_max)
        self.p_size = p_size # the population size to be maintained
        self.k_max = k_max # the maximum number of unique prime numbers desired
        self.min_depth = min_depth # the minimum tree depth allowed
        self.max_depth = max_depth # the maximum tree depth allowed
        self.a_range = a_range # the range(inclusive) within which to search for constants a
        self.b_range = b_range # the range(inclusive) within which to search for constants b
        self.p_mutate = p_mutate # the probabilty of mutation
        self.calc_eng = calc_eng # external computation engine to use for primality checking
        
        self.populate()
        
    def populate(self):
        
        # initialize population
        self.population = Population(init_population_size=self.p_size,
                                     a_range=self.a_range, 
                                     b_range=self.b_range, 
                                     pset=pm().get_pset(),
                                     min_depth=self.min_depth, 
                                     max_depth=self.max_depth)

        # print inital population
        self.population.describe()
        
    
    def run(self):
        # run experiment
 
        evol = evolution.Evolution()
        
        for generation in range(self.max_iter):
            #print('Computing generation: '+str(generation))
            #self.population.describe()
            #print('\n')
            
            # pair up parents
            pairs = evol.make_random_pairs(list(self.population.get_all().keys()))
        
            # create off-spring
            for pair in pairs:
            
                parent1 = self.population.get_individual(pair[0])
                parent2 = self.population.get_individual(pair[1])
            
                child1, child2 = evol.cross_over(parent1, parent2)
                
                #print('parents: '+parent1.describe()+' and '+parent2.describe())
                #print('children: '+child1.describe()+' and '+child2.describe())
                #print('\n')
            
                # decide if mutation occurs for child 1
                if random.random() < self.p_mutate:
                    evol.mutate(child1)
                
                # decide if mutation occurs for child 2    
                if random.random() < self.p_mutate:
                    evol.mutate(child2)
                
                # update child fitness
                child1.calc_fitness(eng)
                child2.calc_fitness(eng)	
				
                # add off-spring to the population
                if child1.fitness > parent1.fitness:
                    self.population.add_individual(child1)
                elif child1.fitness == parent1.fitness:
                    self.population.replace_individual(pair[0], child1)
                else:
                    pass
					
                if child2.fitness > parent2.fitness:
                    self.population.add_individual(child2)
                elif child1.fitness == parent1.fitness:
                    self.population.replace_individual(pair[1], child2) 
                else:
                    pass					
                #print('\n\n')
                
            # perform fitness based selection to maintain original population size
            evol.select(population=self.population,
                        n_selection=self.p_size, 
                        k_max=self.k_max,
                        calc_eng=self.calc_eng)
            
            # check early-termination condition
            if self.population.max_fitness > (self.f_threshold*self.k_max):
                break
    
    def report_results(self):
        
        # report the experiment results
        report = open('experiment-'+str(self.exp_id)+'.txt', 'w')
		
        # write experiment inputs
        report.write('max_iter'+', '+
                     'f_threshold'+', '+
					 'p_size'+', '+
				     'k_max'+', '+
					 'min_depth'+', '+
					 'max_depth'+', '+
					 'a_range'+', '+
					 'b_range'+', '+
					 'p_mutate'+', '+'\n')
					 
        report.write(str(self.max_iter)+', '+
                     str(self.f_threshold)+', '+
					 str(self.p_size)+', '+
				     str(self.k_max)+', '+
					 str(self.min_depth)+', '+
					 str(self.max_depth)+', '+
					 str(self.a_range)+', '+
					 str(self.b_range)+', '+
					 str(self.p_mutate)+', '+'\n\n')
        
        # write headings
        report.write('Fitness score : Individual \n')
        
        for key in self.population.get_all().keys():
            ind = self.population.get_all()[key]
            
            report.write(str(ind.fitness) +' : '+ ind.describe() + '\n')
            
        report.close()
        