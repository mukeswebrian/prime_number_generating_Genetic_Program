from experiment import Experiment
import pandas as pd
import time
import primality_checker as custom_engine

use_matlab = False # Only set this to true if you have a matlab installation and python-matlab library

if use_matlab:
    # optionally use matlab for primality checking
    import matlab.engine
    eng = matlab.engine.start_matlab()
else:
    # use custom primality checker by dafault
    eng = custom_engine.Checker()

if __name__=='__main__':
    
    exps = {}
    
    # initialize specified experiments
    
    el = pd.read_excel('experiment_list.xlsx')
    
    for i in range(len(el)):
        exp_id = el.experiment_id.iloc[i]
        
        a_max = int(el.a_range.iloc[i].split(',')[1])
        a_min = int(el.a_range.iloc[i].split(',')[0])
        
        exps[exp_id] = Experiment(exp_id=exp_id, 
                                max_iter=el.max_iter.iloc[i], 
                                f_threshold=el.f_threshold.iloc[i], 
                                p_size=el.p_size.iloc[i], 
                                k_max=el.k_max.iloc[i], 
                                min_depth=el.min_depth.iloc[i], 
                                max_depth=el.max_depth.iloc[i], 
                                a_range=(a_min,a_max), 
                                p_mutate=el.p_mutate.iloc[i],
								calc_eng=eng)
        
    print('Experiment initalization completed successfully!\n')
        
    # Run each experiment and report results
    for i in exps.keys():
        
        print('running experiment: '+str(i))
        strt = time.time() # start timer
		
        exps[i].run()
        exps[i].report_results()

        end = time.time() # stop timer
        print('completed in: '+str(end-strt)+' seconds \n\n')
    
	# close matlab engine if it was used for calculation
    if use_matlab:
        eng.exit()
		
    print('Done')