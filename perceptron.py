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

#
#	Exemplo AND e OR
#

#entrada_and_or = [[0,0],[0,1],[1,0],[1,1]]
#saida_or       = [0,1,1,1]
#saida_and      = [0,0,0,1]

#p_or  = training_perceptron(entrada_and_or,  saida_or, limit_degrau_bin, 5e-1)
#p_and = training_perceptron(entrada_and_or, saida_and, limit_degrau_bin, 5e-1)

#print("\nPorta Logica OR:\n")
#print("\t0 V 0 =",p_or([0,0]))
#print("\t0 V 1 =",p_or([0,1]))
#print("\t1 V 0 =",p_or([1,0]))
#print("\t1 V 1 =",p_or([1,1]))

#print("\nPorta Logica AND:\n")
#print("\t0 A 0 =",p_and([0,0]))
#print("\t0 A 1 =",p_and([0,1]))
#print("\t1 A 0 =",p_and([1,0]))
#print("\t1 A 1 =",p_and([1,1]))

#============================================================================================#


#
#	MATRIZ A E A INVERSO
#

#matrizes_A = [
#		 [ [-1,-1, 1,-1,-1],
#		   [-1, 1,-1, 1,-1],
#		   [-1, 1, 1, 1,-1],
#		   [1 ,-1,-1,-1, 1],
#		   [1 ,-1,-1,-1, 1]
#	 	 ],
#		 [ [ 1,-1,-1,-1, 1],
#		   [ 1,-1,-1,-1, 1],
#		   [-1, 1, 1, 1,-1],
#		   [-1, 1,-1, 1,-1],
#		   [-1,-1, 1,-1,-1]
#	 	 ]
#	 ]

#matrizes_ruidos =[
#		 [ [-1, 1, 1,-1,-1],
#		   [-1, 1,-1, 1,-1],
#		   [-1, 1,-1, 1,-1],
#		   [ 1,-1,-1,-1, 1],
#		   [ 1, 1,-1,-1, 1]
#	 	 ],
#		 [ [ 1,-1,-1,-1,-1],
#		   [ 1,-1,-1, 1, 1],
#		   [-1, 1, 1, 1,-1],
#		   [-1, 1, 1, 1,-1],
#		   [-1,-1, 1,-1,-1]
#	 	 ]
#
#	]

#saida_matrizes = [1,-1]
#p_mat_a = training_perceptron(matrizes_A, saida_matrizes, limit_degrau_neg, 5e-1)


#print("\n\nMatrizes:\n")
#print("\tMatriz A(1) com ruidos = "         ,p_mat_a(matrizes_ruidos[0]))
#print("\tMatriz A inverso(-1) com ruidos = ",p_mat_a(matrizes_ruidos[1]))
