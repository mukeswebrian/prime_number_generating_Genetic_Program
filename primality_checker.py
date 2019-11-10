import math
class Checker():
	'''
	a custom class for checking if a given number is in the 
	set of the first N primes
	'''
	def __init__(self, N=1000, max_iter=1000):
		
		# initalize list to contain the first N primes
		self.primes = []
		
		for i in range(2, max_iter):
		
			flag = False
			for j in range(2,i):
				if i%j == 0:
                    # flag and break if a factor is discovered
					flag = True
					break
				else:
					pass
					
			if not flag:
                # add i to list of primes if no factors are discovered
				self.primes.append(i)
            
            # Terminate after generating the first N primes			
			if len(self.primes) >= N:
				break
	
	def isprime(self, n):
		
		'''
        method to check if a number in the set of primes
        '''
        # check if n is in the set of primes
		if n in self.primes:
			return True
		else:
			return False
			