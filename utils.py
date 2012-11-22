import scipy.io
import numpy
import itertools

def uns(lista):
    for n in range(numpy.shape(lista)[0]):
        if lista[n] > 0:
            lista[n] == 1
    
    return(lista)

def read_mat(filename):
    mat_file = scipy.io.loadmat(filename)
    return mat_file

def calc_comb_markov(n_maquinas, combinacoes):
    m1 = combinacoes["m1"][0].tolist()
    m2 = combinacoes["m2"][0].tolist()
    m3 = combinacoes["m3"][0].tolist()
    m4 = combinacoes["m4"][0].tolist()
    m5 = combinacoes["m5"][0].tolist()
    m6 = combinacoes["m6"][0].tolist()
    m7 = combinacoes["m7"][0].tolist()
    m8 = combinacoes["m8"][0].tolist()
    m9 = combinacoes["m9"][0].tolist()
    m10 = combinacoes["m10"][0].tolist()
    
    weights = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
    
    lista = itertools.product(*weights)
    
    l1 = range(n_maquinas[0]+1)
    l2 = range(n_maquinas[1]+1)
    l3 = range(n_maquinas[2]+1)
    l4 = range(n_maquinas[3]+1)
    l5 = range(n_maquinas[4]+1)
    l6 = range(n_maquinas[5]+1)
    l7 = range(n_maquinas[6]+1)
    l8 = range(n_maquinas[7]+1)
    l9 = range(n_maquinas[8]+1)
    l10 = range(n_maquinas[9]+1)
    
    l = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
    
    lista_maquinas = itertools.product(*l)
    
    
    return lista, lista_maquinas
    
def calc_comb(pesos):
    list = []
    
    for n in range(numpy.shape(pesos)[0]):
        if n == 0:
            list = [[0,pesos[0]]]
        else:
            list = list + [[0,pesos[n]]]
    
    lista = itertools.product(*list)
    
    return lista
    

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
