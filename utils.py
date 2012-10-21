import scipy.io
import numpy

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
        if n == pos+n_maquinas[maquina]-1:
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

def init_markov(permut, n_maquinas, linha):
    c = numpy.shape(permut)[1]
    
    b = numpy.shape(n_maquinas)[0]
    
    permut[linha,:] = numpy.zeros([1,c])
    
    for m in range(b):
        pos = numpy.sum(n_maquinas[0:m])
        permut [linha,pos] = 1
    return permut
    

def proxm(n_maquinas, permut, slot, nslots):
    
    [permut[slot,:],b] = prox(n_maquinas,0, permut[slot,:])
    a = 0
    
    if b == 1:
        if slot == nslots:
            a = 1
            return permut,a
        
        permut = init_markov(permut, n_maquinas, slot)
        [permut,a] = proxm(n_maquinas, permut, slot+1, nslots)
        return permut,a
    
    return permut,a
