import tree

class Population():
    
    def __init__(self, population_size, a_range, b_range, min_depth, max_depth, pset):
        
        # create a population of tree individuals
        self.population = {}
        for i in range(0, population_size):
            self.population[i] = tree.Tree(a_range, b_range, pset, min_depth, max_depth)
     
    def get_all(self):
        return self.population   
    
    def get_individual(self, index):
        
        if index < len(self.polulation) and index >=0:
            return self.population[index]
        else:
            return None