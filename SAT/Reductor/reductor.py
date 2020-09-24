import sys
import reader

def reduce(x):
    print("REDUCIENDO INSTANCIAS A %s-SAT . . ." % x)
    instances = reader.read_file()
    for instance in instances:
        problem_reduced = []
        num_vars = instance[0][2]
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
            
            instance[0][2] = num_vars
            instance[0][3] = str(len(problem_reduced) - 1)

        #print(instance[0])
        for inst in problem_reduced:
            print(str(inst) + "\n")
    print("INSTANCIAS REDUCIDAS A %s-SAT." % x)

x = str(sys.argv[1])

reduce(x)