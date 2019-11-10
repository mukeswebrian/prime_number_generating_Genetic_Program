from deap import gp
from custom_operator import Operator

class Primitive():
    
    def __init__(self):
        
        # define the primitive set for the experiment
        self.pset = gp.PrimitiveSetTyped('prime_generator', [int,int], int)
        self.pset.renameArguments(ARG0='k1')
        self.pset.renameArguments(ARG1='k2')
        
        # define non-terminal primitives
        op = Operator() 
        self.pset.addPrimitive(op.add, [int, int], int)
        self.pset.addPrimitive(op.mul1, [int, int], int)
        self.pset.addPrimitive(op.sqr, [int, int], int)
        #self.pset.addPrimitive(op.sub, [int, int], int)
        
    def get_pset(self):
        return self.pset