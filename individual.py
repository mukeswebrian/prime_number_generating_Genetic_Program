from deap import gp
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import matlab.engine
import random

class Individual():
    '''
    This class generates a random tree using a specified
    set of operators
    '''
    def __init__(self, a_range, b_range, pset, min_depth, max_depth):
        
        self.a_range = a_range
        self.b_range = b_range
        self.min_depth = min_depth
        self.max_depth = max_depth
        self.pset = pset
        
        # initalize fitness as 0 (all newly created trees are initalized with minimum fitness)
        self.fitness = 0
        
        # initalize with empty tree
        self.tree = None
        
    def make_tree(self):
        
        # spefify the maximum and minimum values of the random constants a and b
        self.a = random.randint(self.a_range[0], self.a_range[1])
        self.b = random.randint(self.b_range[0], self.b_range[1])
        
        # add terminal primitives the tree's primitive set specific
        self.pset.addTerminal(self.a, int)
        self.pset.addTerminal(self.b, int)
        
        expression = gp.genGrow(self.pset, min_=self.min_depth, max_=self.max_depth)
        self.tree = gp.PrimitiveTree(expression)
        
    
    def plot(self, fig_name):
        
        '''
        A method for visualizing a tree and saving the figure in a file
        
        Refernce: used plotting code from https://deap.readthedocs.io/en/1.0.x/tutorials/advanced/gp.html
                  as a template
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
        
    def calc_fitness(self, calc_engine, k_max=20):
        '''
        Fitness method where fitness is calculated as the number of values k in 
        the range 0 to k_max for which the function generates unique prime numbers
        primality check is delegated to MATLAB is prime function
        '''
        # calulate the fitness of the tree
        func = gp.compile(self.tree, self.pset)
        
        # get a list of all the unique integers generated
        calc = map(func, [i for i in range(0, k_max)])
        unique_nums_generated = list( pd.Series([j for j in calc]).unique() )
        
        # use matlab engine to count the number of unique prime integers generated
        
        check_prime = map(calc_engine.isprime, [int(i) for i in unique_nums_generated])
        self.fitness = [i for i  in check_prime].count(True)
        
        
        return self.fitness
        
    def get_tree(self):
        return self.tree
    
    def get_pset(self):
        return self.pset
    
    def describe(self):
        return self.tree.__str__()
    
    def get_terminal_indicies(self):
        
        indicies = []
        
        for i in range(0, len(self.tree)):
            if self.is_terminal(self.tree[i]):
                indicies.append(i)
                
        return indicies
    
    def get_non_terminal_indicies(self):
        
        indicies = []
        
        for i in range(0, len(self.tree)):
            if not self.is_terminal(self.tree[i]):
                indicies.append(i)
                
        return indicies
    
    def get_int_terminal_indicies(self):
        
        indicies = []
        
        for i in range(0, len(self.tree)):
            if self.is_terminal(self.tree[i]):
                if type(self.tree[i].value) is int:
                    indicies.append(i)
                
        return indicies        
    
    def is_terminal(self, node):
        '''
        A method to check whether a specified node is a terminal node
        '''
        if type(node)==type(self.pset.terminals[int][0]):
            return True
        else:
            return False
        
        
        
        
        
        
    
        
                
        
        