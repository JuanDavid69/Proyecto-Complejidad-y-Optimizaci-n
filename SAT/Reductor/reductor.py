import sys

def reduce(x,sat_instance, sat_instance_reduced):
    for instance in instances:
        problem_reduced = []
        num_vars = sat_instance.vars
        num_clauses= instance[0][3]
        for clause in instance:
            if clause[0] == 'p':
                problem_reduced.append(clause)
                continue
            if int(x) == len(clause):
                problem_reduced.append(clause)
                continue
            if int(x) > int(len(clause)) and (int(x) - int(len(clause))) == 1:
                num_new_vars = int(x) - int(len(clause))
                num_new_clauses = pow(2, num_new_vars)
                
                is_new_var_added = False
                
                num_vars = str(int(num_vars)+1)
                negative_num_vars = "-" + num_vars
                
                for i in range(num_new_clauses):
                    new_clause = clause[:]
                    
                    negative_new_clause = new_clause[:]
                    
                    for j in range(num_new_vars): 
                        negative_new_clause.append(negative_num_vars)
                        new_clause.append(num_vars)

                    if is_new_var_added:
                        problem_reduced.append(negative_new_clause)
                    else:
                        problem_reduced.append(new_clause)
                        is_new_var_added = True
            if int(x) < int(len(clause))
            
            instance[0][2] = num_vars
            instance[0][3] = str(len(problem_reduced) - 1)

        #print(instance[0])
        return sat_instance_reduced

def increase(x,sat_instance, sat_instance_reduced):
    
    num_vars = sat_instance.nv
    new_clause_size = int(x)

    for clause in sat_instance:
        clause_size = len(clause)

        if new_clause_size == clause_size:
            problem_reduced.append(clause)
        else:
            

def read_cnf_and_reduce(x):
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
            
            sat_instance_reduced = reduce(x, sat_instance, sat_instance_reduced)
            
            sat_instance_reduced.to_file(join(X_SAT_directory, SAT_instance[:-4] + '_reduced.cnf'))
            print(sat_instance.clauses)
            print(sat_instance_reduced.clauses)
    
    print("INSTANCIAS REDUCIDAS A %s-SAT." % x)
    
read_cnf_and_reduce()

x = str(sys.argv[1])

read_cnf_and_reduce(x)