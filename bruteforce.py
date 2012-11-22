import utils
import scipy
import numpy

# Inicializacao e importacao de dados
print "initializing and loading data"

mat_file = utils.read_mat("final.mat")

# Variancia
s2 = mat_file["s2"]

# Matriz de probabilidades
matriz_probabilidades = mat_file["probab"]

# Consumo total
Consumo_total = mat_file["x_teste"]

# Vector com o numero de submaquinas de cada maquina
n_maquinas = mat_file["n_maquinas"]

# Vector com o consumo de cada submaquina
pesos = mat_file["pesos"].tolist()[0]

# Variaveis auxiliares

l = scipy.shape(pesos)[0]
t = scipy.shape(Consumo_total)[0]

# Matriz de armazenamento dos resultados de cada problema 
optimo = scipy.zeros([t,l,5])

# Geracao da lista de permutacoes
lista = utils.calc_comb(pesos)

# Minimizacao

for n in range(0,1):
    
    print "in problem %s" % n
    a = 0
    b = 0
    combinacoes = scipy.zeros(l)
    best =[float('Inf')]*5
    
    # Caso o consumo total seja zero nao e necessario optimizar
    if Consumo_total[n] == 0:
        continue
    
    # Percorre todas as permutacoes
    for c in lista:
        
        # Dada a baixa variancia so interessam combinacoes cujo consumo seja igual ao consumo total
        
        if s2 < 0.000001:
            if Consumo_total-sum(c) != 0:
                continue
        
        # Calculo da primeira parte do funcional de custo
        custo = 1/(2*s2)*(Consumo_total[n] - sum(c))**2 
        
        # Calculo do vector de combinacoes
        combinacoes = numpy.array(utils.uns(c))
        
        # Calculo da segunda parte do funcional de custo
        custo = custo - numpy.dot(combinacoes,numpy.log(matriz_probabilidades[n,:])) - numpy.dot((1-combinacoes,),numpy.log(1-matriz_probabilidades[n,:]))
        
        # Armazenamento de resultados
        for i in xrange(5):
            if custo < best[i]:
                if i == 5:
                    best[i] = custo
                    optimo[n,:,i] = combinacoes
                    break
                
                for m in range(0,4-i):
                    best[i] = custo
                    optimo[n,:,i]
                
                best[i] = custo
                optimo[n,:,i] = combinacoes
                break
        
    