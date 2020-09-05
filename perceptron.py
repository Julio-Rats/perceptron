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

	entrada_p = np.array(entrada)
	saida_p   = np.array(saida)
#	pesos_p   = np.array(np.random.random(entrada_p[0].shape))
	pesos_p   = np.zeros(entrada_p[0].shape)

	result_p  = []
#	bias  = np.radom.random()
	bias  = 0

	for k in range(len(saida)):
		result_p.append(f_activ(np.sum(entrada_p[0]*pesos_p)+bias))

	erro_p    = np.sum(saida_p-np.array(result_p))
	inter = 0

	while (erro_p != 0)and(inter < maxInter):

		inter = inter + 1 	
		for i in range(len(entrada_p)):
			erro_p = saida_p[i] - f_activ((np.sum(entrada_p[i]*pesos_p))+bias)
			if (erro_p != 0):
				pesos_p = pesos_p + (delta*entrada_p[i]*(erro_p))
				bias = bias + delta*erro_p
				break
	
	if (inter == maxInter):
		print("\n\n[CAUTION]: inter value is limited by maxInter\n\n")
		
	def perceptron(x):
		return f_activ(np.sum(np.array(x)*pesos_p)+bias)

	return perceptron

#============================================================================================#

