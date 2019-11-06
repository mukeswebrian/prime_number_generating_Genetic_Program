class Operator():
    ''' 
        This class defines the non terminal methods
        (i.e. operators) used in the generataed program trees.
    '''
    def __init__(self, n_args=2):
        self.n_args = n_args
        
    def add(self, arg1, arg2):
        return sum([arg1, arg2])
        
    def mul(self, arg1, arg2):
        return arg1*arg2
    
    def get_n_args(self):
        return self.n_args
    
