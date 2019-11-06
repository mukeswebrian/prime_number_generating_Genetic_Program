from deap import gp
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import matlab.engine
import random

class Tree():
    '''
    This class generates a random tree using a specified
    set of operators
    '''
    def __init__(self, a_range, b_range, pset, min_depth, max_depth):
        
        # initalize fitness as 0 (all newly created trees are initalized with minimum fitness)
        self.fitness = 0
        
        # spefify the maximum and minimum values of the random constants a and b
        self.a = random.randint(a_range[0], a_range[1])
        self.b = random.randint(b_range[0], b_range[1])
        
        # add terminal primitives the tree's primitive set specific
        self.pset = pset
        self.pset.addTerminal(self.a, int)
        self.pset.addTerminal(self.b, int)
        
        expression = gp.genGrow(pset, min_=min_depth, max_=max_depth)
        self.tree = gp.PrimitiveTree(expression)
        
    
    def plot(self, fig_name):
        
        '''
        A method for visualizing a tree and sving the figure in a file
        '''
        nodes, edges, labels = gp.graph(self.tree)
        
        g = nx.Graph()
        g.add_nodes_from(nodes)
        g.add_edges_from(edges)
        pos = nx.drawing.layout.spring_layout(g)

        nx.draw_networkx_nodes(g, pos)
        nx.draw_networkx_edges(g, pos)
        nx.draw_networkx_labels(g, pos, labels)
        plt.savefig(fig_name)
        
    def calc_fitness(self, k_max=20):
        '''
        Fitness is calculated as the number of values k in the range 0 to k_max for
        which the function generates unique prime numbers
        '''
        # calulate the fitness of the tree
        func = gp.compile(self.tree, self.pset)
        
        # get a list of all the unique integers generated
        calc = map(func, [i for i in range(0, k_max)])
        unique_nums_generated = list( pd.Series([j for j in calc]).unique() )
        
        # use matlab engine to count the number of unique prime integers generated
        eng = matlab.engine.start_matlab()
        check_prime = map(eng.isprime, [int(i) for i in unique_nums_generated])
        self.fitness = [i for i  in check_prime].count(True)
        eng.exit()
        
        return self.fitness
        
    def get_tree(self):
        return self.tree
    
    def describe(self):
        return self.tree.__str__()
        
        
        
        
        
        
        
    
        
                
        
        