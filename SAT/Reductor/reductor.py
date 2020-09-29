from os import system, getcwd, walk
from os.path import join, sep
import sys
from pysat.formula import CNF

def increse_one_by_one(clause, num_vars, sat_instance_reduced,new_clause_size):

    sat_instance_reduced_copy = sat_instance_reduced.copy() # Creamos una copia de la instancia reducida para el llamado recursivo

    pos_new_clause = clause [:] # Creamos la nueva clausula
    neg_new_clause = clause [:] # Creamos la nueva clausula

    num_vars = num_vars + 1 # Creamos la nueva variable positiva 
    neg_num_vars = num_vars * -1 # Creamos la nueva variable negativa

    pos_new_clause.append(num_vars) # Agremamos la variable positiva a la clausula
    neg_new_clause.append(neg_num_vars) # Agregamos la variable negativa a la clausula
                    
    # Agregamos las nuevas clausulas a la instancia SAT reducida
    sat_instance_reduced.append(pos_new_clause)
    sat_instance_reduced.append(neg_new_clause)

    clause_size = int(len(pos_new_clause)) # Calculamos el tamaño de las nuevas clausulas calculadas

    if new_clause_size > clause_size: # Verificamos si la clausula calculada ya se encuentra en X-SAT

        # Llamados recursivos para nuestras clausulas positivas y negativas que aun no se encuentran en X-SAT
        sat_instance_reduced = increse_one_by_one(pos_new_clause, num_vars, sat_instance_reduced_copy, new_clause_size)
        sat_instance_reduced = increse_one_by_one(neg_new_clause, num_vars, sat_instance_reduced, new_clause_size)
    
    return sat_instance_reduced 

def reduce(x,sat_instance):
    
    sat_instance_reduced = CNF() # Creamos una instancia de la clase CNF donde se almacenaran las clausulas reducidas
    num_vars = sat_instance.nv # Obtenemos el numero de variables de la instancia a reducir
    new_clause_size = int(x) # Obtenemos el X del X-SAT que deseamos reducir
    #print(sat_instance.clauses)
    
    for clause in sat_instance:
        
        clause_size = int(len(clause)) # Obtenemos el tamaño de la clausula en cada iteracion
         
        if new_clause_size == clause_size: # Si el tamaño de la clausula es igual al X-SAT que buscamos resumir entonces agregamos la misma clausula sin modificarla
            
            sat_instance_reduced.append(clause)
        else:
            if new_clause_size > clause_size: # Si el tamaño de X-SAT es mayor que el tamaño de la clausula actual, incrementamos
                
                sat_instance_reduced = increse_one_by_one(clause, num_vars, sat_instance_reduced, new_clause_size) # Reductor
                
                num_vars = sat_instance_reduced.nv
            
            elif new_clause_size < clause_size: # Si el tamaño de X-SAT es menor que el tamaño de la clausula actual, reducimos

                num_new_vars = clause_size - new_clause_size # Obtenemos el numero de nuevas variables que vamos a crear
    
    return sat_instance_reduced


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
            sat_instance = CNF(from_fp=fp) # Leemos el archivo .cnf para obtener el problema en un formato manejable
            sat_instance_reduced = CNF() # Creamos una instancia de la clase CNF donde se almacenaran las clausulas reducidas

            sat_instance_reduced = reduce(x, sat_instance) # Llamamos a la funcion "reduce", la cual reduce la instancia que le pasemos
            
            sat_instance_reduced.to_file(join(X_SAT_directory, SAT_instance[:-4] + '_reduced.cnf')) # Escribimos un nuevo archivo .cnf con la instancia reducida
    
    print("INSTANCIAS REDUCIDAS A %s-SAT." % x)

x = str(sys.argv[1])

read_cnf_and_reduce(x)