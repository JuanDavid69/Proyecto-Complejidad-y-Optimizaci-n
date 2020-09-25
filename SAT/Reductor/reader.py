from os import system, getcwd, walk
from os.path import join, sep
import sys
from pysat.formula import CNF

def read_file():
    ALL_PROBLEMS = [] # Store all the SAT problems in format Problems->[Problem->[Clause->[variables]]]
    ACTUAL_DIRECTORY = getcwd() # Get the current directory path (../SAT/Reductor)
    PARENT_DIRECTORY = sep.join(ACTUAL_DIRECTORY.split(sep)[1:-1]) # Get the parent directory (../SAT)
    PARENT_DIRECTORY = join(sep, PARENT_DIRECTORY) # Apeend SO separator to access the folder
    SAT_instances_directory = join(PARENT_DIRECTORY, "TEST") # Joins the parent directory with InstanciasSAT to get into (../SAT/instanciasSAT)
    _, _, SAT_instances = next(walk(SAT_instances_directory))
    for SAT_instance in SAT_instances:
        SAT_file = open(join(SAT_instances_directory, SAT_instance), 'r')
        problem = []
        for line in SAT_file:
            if line[0] == "c":
                continue
            if line[0] == "p" and not problem:
                ALL_PROBLEMS.append(problem)
                problem.append(line[:-1].split(" "))
                continue
            if line[0] == "p":
                ALL_PROBLEMS.append(problem)
                problem = []
                problem.append(line[:-1].split(" "))
                continue
            if problem:
                problem.append(line[:-3].split(" "))

        break    
    #print(ALL_PROBLEMS)
    return ALL_PROBLEMS

def read_cnf_and_reduce():
    ACTUAL_DIRECTORY = getcwd() # Get the current directory path (../SAT/Reductor)
    PARENT_DIRECTORY = sep.join(ACTUAL_DIRECTORY.split(sep)[1:-1]) # Get the parent directory (../SAT)
    PARENT_DIRECTORY = join(sep, PARENT_DIRECTORY) # Apeend SO separator to access the folder
    SAT_instances_directory = join(PARENT_DIRECTORY, "TEST") # Joins the parent directory with InstanciasSAT to get into (../SAT/instanciasSAT)
    X_SAT_directory = join(PARENT_DIRECTORY, "X-SAT") # Joins the parent directory with InstanciasSAT to get into (../SAT/X-SAT)
    _, _, SAT_instances = next(walk(SAT_instances_directory))
    print("REDUCIENDO INSTANCIAS A %s-SAT . . ." % x)
    for SAT_instance in SAT_instances:
        with open(join(SAT_instances_directory, SAT_instance), 'r') as fp:
            sat_instance = CNF(from_fp=fp)
            sat_instance_reduced = CNF()
            
            reduce(x, sat_instance, sat_instance_reduced)
            for clause in sat_instance:
                if int(x)
            sat_instance_reduced.append([-1,2])
            sat_instance_reduced.append([1,-3])
            sat_instance_reduced.append([5,-4])
            sat_instance_reduced.to_file(join(X_SAT_directory, SAT_instance[:-4] + '_reduced.cnf'))
            print(sat_instance.clauses)
            print(sat_instance_reduced.clauses)
    print("INSTANCIAS REDUCIDAS A %s-SAT." % x)
    
read_cnf_and_reduce()