from deap import gp
from custom_operator import Operator

class Primitive():
    
    def __init__(self):
        
        # define the primitive set for the experiment
        self.pset = gp.PrimitiveSetTyped('prime_generator', [int], int)
        self.pset.renameArguments(ARG0='k')
        
        # define non-terminal primitives
        op = Operator() 
        self.pset.addPrimitive(op.add, [int, int], int)
        self.pset.addPrimitive(op.mul, [int, int], int)
        
    def get_pset(self):
        return self.pset