import numpy as np
from   trainment.input import Item
from   perceptron import *

input_learning  = []
results_correct = []


data_training = list(range(1,11))
data_rating   = list(range(11,37))


print("\n\t|========================================|")
print("\t|              Treinamento               |")
print("\t|========================================|\n")


for num_file in data_training:	
	obj = Item("./trainment/{:02d}".format(num_file)+".txt")
	print("File:("+obj.fname+"). Utilizado para treinamento.")
	print(obj)
	input_learning.append(obj.array)
	results_correct.append(obj.value)

trained_perceptron = training_perceptron(np.array(input_learning), results_correct)

hit    = 0
missed = 0

print("\n\t|========================================|")
print("\t|              Avaliação                 |")
print("\t|========================================|\n")

for num_file in data_rating:	
	obj = Item("./trainment/{:02d}".format(num_file)+".txt")
	estimado = trained_perceptron(obj.array)
	print("File:("+obj.fname+"). Valor Estimado: ", estimado)
	print(obj)
	if estimado == obj.value:
		hit = hit + 1
	else: 
		missed = missed + 1

print("\nLog de pontuações\n")		
print("\tAcertos: ", hit)	
print("\tErros:   ", missed)
print("\n\n")

	
