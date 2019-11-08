import random
import individual
import copy
import pandas as pd

class Evolution():
    '''
    A class that implements evolution mechanisms
    '''
    
    def __init__(self):
        pass
    
    def mutate(self, ind1):
        
        '''
        Mutation involves selecting a node uniformly at random
     
        if the selected node is a non-terminal node, the oparator of 
        the node is replaced by a different operator that is also selected at random
     
        if the selected node is a terminal node, the node is randomly increamented or 
        decremented by 1 with equal probability
     
        The mutation is performed in place
     
        '''
        # select node to mutate
        node_index = random.randint(0, len(ind1.get_tree())-1)
        node = ind1.get_tree()[node_index]
               
        if ind1.is_terminal(node):
             # if node is terminal
            
            if type(node.value) is int:
                # mutate if int
                ind1.tree[node_index].value = node.value + random.choice([1,-1])
                
            else:
                # check if node is a k do nothing
                pass
            
        else:
             # if node is non-terminal
            non_terminals = ['add', 'mul', 'sub']
            non_terminals.remove(node.name)
            
            new_node_name = random.choice(non_terminals)
            
            for n in ind1.get_pset().primitives[int]:
                if new_node_name == n.name:
                    ind1.tree[node_index] = n     
        
    
    def cross_over(self, ind1, ind2):
        '''
        cross-over involves simply swapping a two nodes between two individuals
        A node is selected at random from each indivdual and is exchanged with
        a randomly selected node of the same type in the other individual.
        
        cross-over results in two newly created individuals
        
        '''
        # create new individuals
        new_ind1 = individual.Individual(ind1.a_range, ind1.b_range, ind1.pset, ind1.min_depth, ind1.max_depth)
        new_ind1.tree = copy.deepcopy(ind1.get_tree())
        
        new_ind2 = individual.Individual(ind2.a_range, ind2.b_range, ind2.pset, ind2.min_depth, ind2.max_depth)
        new_ind2.tree = copy.deepcopy(ind2.get_tree())
        
        
        # select nodes to cross over
        n1 = random.choice([i for i in range(len(ind1.get_tree()))])
        
        if ind1.is_terminal(ind1.get_tree()[n1]):
            
            n2 = random.choice(ind2.get_terminal_indicies())
            
            # swap terminal nodes
            n1_value = ind1.get_tree()[n1].value
            n2_value = ind2.get_tree()[n2].value
            
            for n in ind1.get_pset().terminals[int]:
                if n1_value == n.value:
                    new_ind2.tree[n2] = n
                
                if n2_value == n.value:
                    new_ind1.tree[n1] = n
            
            #print('swapped terminals')
            #print('swapped item in ind1: '+str(n1_value))
            #print('with')
            #print('swapped item in ind2: '+str(n2_value))
         
        
        else:
            n2 = random.choice(ind2.get_non_terminal_indicies())
            
            # swap non-terminal nodes
            n1_name = ind1.get_tree()[n1].name
            n2_name = ind2.get_tree()[n2].name
            
            for n in ind1.get_pset().primitives[int]:
                if n1_name == n.name:
                    new_ind2.tree[n2] = n
                
                if n2_name == n.name:
                    new_ind1.tree[n1] = n
                    
            #print('swapped non-terminals')
            #print('swapped item in ind1: '+n1_name)
            #print('with')
            #print('swapped item in ind2: '+n2_name)    
     
        return new_ind1, new_ind2
    
    def make_random_pairs(self, ids):
        '''
        A method for randomly pairing up individuals in a population for the
        purposes of cross over
        '''
        pairs = []
        if len(ids)%2 == 0:
            r = random.sample(ids, len(ids))
        
            for j in range(len(ids)-1):
                if j%2 == 0:
                    pairs.append(r[j:j+2])
            
        return pairs
    
    def select(self, population, n_selection, calc_eng, k_max=20):
        '''
        selects a specified number of individuals from a population.
        
        selection is done by dropping the least fit members from the population
        and keeping only the fittest n_selection members.
        '''
        
        if n_selection >= population.get_size():
            return population
        
        elif n_selection < population.get_size():
            n_drop = population.get_size() - n_selection
            
            # get fitness scores
            individuals = population.get_all()
            scores = {}
            
            for key in individuals.keys():
                scores[key] = individuals[key].calc_fitness(calc_engine=calc_eng, k_max=k_max)
                
            #print(scores)
            
            # identify individuals to be dropped
            scores = pd.Series(scores).sort_values()
            to_drop = scores.index[:n_drop]
            
            # drop unfit individuals
            for i in to_drop:
                population.get_all().pop(i)
                
            # update maximum fitness
            population.max_fitness = scores.max()
            
            # reset individual ids
            #j = 0
            #for key in population.get_all().keys():
                #population.get_all()[j] = population.get_all()pop(key)
                #j += 1
            
                
            
    