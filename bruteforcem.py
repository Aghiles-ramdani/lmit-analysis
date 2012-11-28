import utils
import scipy
import numpy

def bruteforce(slot_inicial, nslots):
    
    # Inicializacao e importacao de dados
    
    mat_file = utils.read_mat("final.mat")
    
    s2 = mat_file["s2"]
    P = mat_file["P"]
    PI = mat_file["PI"]
    
    n_maquinas = mat_file["n_maquinas"]
    
    pesos = mat_file["pesos"]
    
    x_teste = mat_file["x_teste"]    
    Consumo_total = x_teste[slot_inicial:slot_inicial+nslots]
    
    [lista,combinacoes] = utils.init_markov(nslots,n_maquinas, pesos)
    
        
    while(1):
        cost = 0
        
        
                
    
    return
