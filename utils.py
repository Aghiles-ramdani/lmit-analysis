import scipy.io
import numpy
import itertools

def uns(lista, comb, maquinas):
    
    tamanho = numpy.shape(comb)[0]
    combinacoes = numpy.zeros(sum(maquinas))
    consumos = numpy.zeros(tamanho)
    pos = 0
    
    for n in range(tamanho):
        consumos[n] = lista[n][comb[n]]
        if comb[n] == 0:
            pos = sum(maquinas[0:n+1])
            continue
        combinacoes[pos+comb[n]-1] = 1
        pos = sum(maquinas[0:n+1])
    
    return (combinacoes, consumos)

def read_mat(filename):
    mat_file = scipy.io.loadmat(filename)
    return mat_file

    
def calc_comb(n_maquinas, pesos):
    lista = []
    for n in range(numpy.shape(n_maquinas)[0]):
        prov = range(n_maquinas[n]+1)
        lista.append(prov)
        
    
    comb = itertools.product(*lista)
    pos = 0
    
    for i in range(numpy.shape(n_maquinas)[0]):
        for m in range(n_maquinas[i]+1):
            if lista[i][m] == 0:
                continue
            lista[i][m] = pesos[pos]
            pos += 1
    
    return(lista, comb)
    

def init_markov(nslots, n_maquinas, pesos):
    combinacoes = []
    for n in range(nslots):
        [lista, comb] = calc_comb(n_maquinas, pesos)
        combinacoes.append(*comb)
    
    return(lista,combinacoes)
