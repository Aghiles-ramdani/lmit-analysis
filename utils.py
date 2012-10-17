import scipy.io

def read_mat(filename):
    mat_file = scipy.io.loadmat(filename)
    return mat_file

def prox(n_maquinas, maquina, permut):
    a = 0
    
    if maquina == 0:
        pos = 0
    else:
        pos = sum(n_maquinas[0:maquina])
        
    for n in xrange(pos, pos+n_maquinas[maquina]):
        
        if n == pos+n_maquinas[maquina]:
            
            if permut[n] == 1:
                
                if maquina == scipy.shape(n_maquinas)[0]-1:
                    permut[n] = 0
                    a = 1
                    return permut, a
                
                permut[n] = 0
                [permut, a] = prox(n_maquinas, maquina+1, permut)
                return permut, a
            
        if permut[n] == 1:
            
            permut[n] = 0
            permut[n+1] = 1
            return permut, a
    
    permut[pos] = 1
    
    return permut, a
