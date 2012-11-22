import utils
import scipy
import numpy
import unfold

# Inicializacao e importacao de dados
print "initializing and loading data"


mat_file = utils.read_mat("final.mat")

s2 = mat_file["s2"]
print "variance %s" % s2

probab = mat_file["probab"]
print "probabilidade: %s" % probab

x_teste = mat_file["x_teste"]
print "consumo total: %s" % x_teste
n_maquinas = mat_file["n_maquinas"]
print "submaquinas per maquina: %s " % n_maquinas
pesos = mat_file["pesos"].tolist()[0]
print "pesos per maquina: %s " % pesos

l = scipy.shape(pesos)[0]
print "l: %s " % l
t = scipy.shape(x_teste)[0]
print "t: %s " % t
optimo = scipy.zeros([t,l,5])
print "optimo: %s " % optimo
list = utils.calc_comb(pesos)

# Minimizacao
for n in range(0,1):
    print "in problem %s" % n
    a = 0
    b = 0
    permut = scipy.zeros(l)
    best =[float('Inf')]*5
    
    if x_teste[n] == 0:
        continue
    
    for idx, c in enumerate(list):
        if idx % 100000 == 0: 
            print "in index: %s" % idx
        if x_teste[n]-sum(c) != 0:
            continue
        
        custo = 1/(2*s2)*(x_teste[n] - sum(c))**2 
        
        
        permut = numpy.array(utils.uns(c))
                
        custo = custo - numpy.dot(permut,numpy.log(probab[n,:])) - numpy.dot((1-permut,),numpy.log(1-probab[n,:]))
        
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
        
    