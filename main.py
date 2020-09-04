import numpy as np
from   trainment.input import Item
from   perceptron import *

input_learning  = []
results_correct = []

for i in range(1,10):	
	obj = Item("./trainment/{:02d}".format(i)+".txt")
	print(obj)
	input_learning.append(obj.array)
	results_correct.append(obj.value)

trained_perceptron = training_perceptron(np.array(input_learning), results_correct)

hit    = 0
missed = 0

for i in range(11,37):	
	obj = Item("./trainment/{:02d}".format(i)+".txt")	
	estimado = trained_perceptron(obj.array)
	print("File:("+obj.fname+"). Valor Estimado: ", estimado)
	print(obj)
	if estimado == obj.value:
		hit = hit +1
	else: 
		missed = missed + 1

print("\nLog de pontuações\n")		
print("\tAcertos: ", hit)	
print("\tErros: ", missed)
print("\n\n")

	
