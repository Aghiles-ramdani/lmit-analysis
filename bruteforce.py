import utils
import scipy
import numpy

# Inicializacao e importacao de dados

mat_file = utils.read_mat("final.mat")
s2 = mat_file["s2"]
probab = mat_file["probab"]
Teste = mat_file["Teste"]
maquinas = mat_file["maquinas"]
x_teste = mat_file["x_teste"]
n_maquinas = mat_file["n_maquinas"]
pesos = mat_file["pesos"]

l = scipy.shape(pesos)[1]
t = scipy.shape(x_teste)[0]
optimo = scipy.zeros([t,l,5])

# Minimizacao
for n in range(0,1):
    
    a = 0
    b = 0
    permut = scipy.zeros(l)
    best =[float('Inf')]*5
    
    if x_teste[n] == 0:
        continue
    
    while(True):
        if x_teste[n]-numpy.dot(pesos,permut) != 0:
            [permut,a]=utils.prox(n_maquinas[0],0,permut)
            continue
        
        custo = 1/(2*s2)*(x_teste[n] - numpy.dot(pesos, permut))**2 - numpy.dot(permut,numpy.log(probab[n,:])) - numpy.dot((1-permut,),numpy.log(1-probab[n,:]))
        
        for i in xrange(5):
            if custo < best[i]:
                if i == 5:
                    best[i] = custo
                    optimo[n,:,i] = permut
                    break
                
                for m in range(0,4-i):
                    best[i] = custo
                    optimo[n,:,i]
                
                best[i] = custo
                optimo[n,:,i] = permut
                break
        
        [permut, a] = utils.prox(n_maquinas[0], 0, permut)
        
        if a == 1:
            break
    