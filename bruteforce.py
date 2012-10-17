import utils
import scipy

# Inicializacao e importacao de dados

mat_file = utils.read_mat("final.mat")
s2 = mat_file["s2"][0,0]
probab = mat_file["probab"]
Teste = mat_file["Teste"]
maquinas = mat_file["maquinas"]
x_teste = mat_file["x_teste"][:,0]
n_maquinas = mat_file["n_maquinas"][0]
pesos = mat_file["pesos"][0]

l = scipy.shape(n_maquinas)[0]
t = scipy.shape(x_teste)[0]
optimo = scipy.zeros([t,l,5])

# Minimizacao
for n in range(0,t-1):
    
    a = 0
    permut = scipy.zeros([t])
    best =[float('Inf')]*5
    print n
    
    if x_teste[n] == 0:
        continue
    
    while(True):
        
        
        
