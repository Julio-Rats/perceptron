import numpy as np

#============================================================================================#

def limit_degrau_bin(x):
	if x <= 0:
		return 0.0
	return 1.0

def sigmoid(x):
	return 1.0/(1.0+np.exp(-x))

def limit_degrau_neg(x):
	if x <= 0:
		return -1.0
	return 1.0

#============================================================================================#

def training_perceptron(entrada, saida, f_activ=limit_degrau_neg, delta=5e-1, maxInter = 5e4):


	if (len(entrada) != len(saida)):
		print("\n\n[ERRO]: Erro a quantidade de entrada é diferente da quantidade de saidas\n\n")
		exit(-1)

	n_entradas = len(saida)
	entrada_p  = np.array(entrada)
	saida_p    = np.array(saida)
	pesos_p    = np.zeros(entrada_p[0].shape)
	bias       = 0.0
	erro_p     = 0.0
	inter      = 0.0
	
	for i_entrada in range(n_entradas):
		erro_p = erro_p + saida_p[i_entrada] - f_activ(np.sum(entrada_p[i_entrada]*pesos_p)+bias)
		 
	while (erro_p != 0.0)and(inter < maxInter):
		inter = inter + 1 	
		for i_entrada in range(n_entradas):
			erro_p = saida_p[i_entrada] - f_activ((np.sum(entrada_p[i_entrada]*pesos_p))+bias)
			if (erro_p != 0.0):
				pesos_p = pesos_p + (delta*entrada_p[i_entrada]*(erro_p))
				bias = bias + delta*erro_p
				break
	
	if (inter == maxInter):
		print("\n\n[CAUTION]: inter value is limited by maxInter\n\n")
		
	def perceptron(x):
		return f_activ(np.sum(np.array(x)*pesos_p)+bias)
	
	return perceptron

#============================================================================================#

