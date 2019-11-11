This is a genetic program that finds prime number generating fucntions. 
The program was implemented using Python version 3.6.5

Organization: University of Edinburgh, School of Informatics
Date: November 11, 2019
Exam Number: B145418


-----------------------------------------------------------------------------------------
Dependancies
-----------------------------------------------------------------------------------------
Before running this program, run the following commands to ensure that all the required
libraries are installed on the system

pip install deap
pip install pandas
pip install matplotlib
pip install networkx

A matlab library folder is also included for the optional use of Matlab for prime checking
Note 1: A MATLAB installation is required in order to use this option.
Note 2: set use_matlab option to TRUE in controller.py to use this option


------------------------------------------------------------------------------------------
How to run the program
------------------------------------------------------------------------------------------
1 - List the details for each experiement to run in the spreadsheet "experiment_list.xlsx"
2 - Save and close the "experiment_list.xlsx" spreadsheet
3 - Run the program as follows:
	a - on a Windows machine simply double click the batch file "1-RUN_EXPERIMENTS.bat"
	b - on a non Windows machine, ececute the command "python controller.py"

-------------------------------------------------------------------------------------------
Output
-------------------------------------------------------------------------------------------
The program generates a text file "experiment-id.txt" for each experiment specified.
Note: Ensure that each experiment is assigned a unique id