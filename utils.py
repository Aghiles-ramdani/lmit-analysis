import scipy.io
import numpy
import itertools

def read_mat(filename):
    mat_file = scipy.io.loadmat(filename)
    return mat_file

def calc_comb():
    mat = read_mat("combinacoes.mat")
    n_maquinas = read_mat("final.mat")["n_maquinas"]
    
    m1 = mat["m1"].tolist()[0]
    m2 = mat["m2"].tolist()[0]
    m3 = mat["m3"].tolist()[0]
    m4 = mat["m4"].tolist()[0]
    m5 = mat["m5"].tolist()[0]
    m6 = mat["m6"].tolist()[0]
    m7 = mat["m7"].tolist()[0]
    m8 = mat["m8"].tolist()[0]
    m9 = mat["m9"].tolist()[0]
    m10 = mat["m10"].tolist()[0]
    l1 = range(n_maquinas[0][0])
    l2 = range(n_maquinas[0][1])
    l3 = range(n_maquinas[0][2])
    l4 = range(n_maquinas[0][3])
    l5 = range(n_maquinas[0][4])
    l6 = range(n_maquinas[0][5])
    l7 = range(n_maquinas[0][6])
    l8 = range(n_maquinas[0][7])
    l9 = range(n_maquinas[0][8])
    l10 = range(n_maquinas[0][9])
    
    comb = itertools.product(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10)
    
    lista = itertools.product(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10)
    
    return comb, lista
    

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
