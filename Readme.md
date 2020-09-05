<style>
h1{color:#0a306c;font-weight:bold}
h2{color:#1056a5}
h3{color:#4076b5}
li{color:#5085c0}
button{display:flex;flex-direction:row;align-items:center}
button:hover{background-color: #67f4}
img{width:20px;height:20px;}
a{text-decoration:none;color:#a00e7b}
a:hover{text-decoration:none;color:#a00e7b;font-weight:bold;cursor:alias;}
</style>

# REDES NEURAIS ARTIFICIAIS, DISCIPLINA SCC5809

## Grupo 6, Autores:

- Júlio César de Melo Cândido NUSP 11926153
  <button type="button">⟶
  <a href="https://github.com/Julio-Rats" target="_blank">Github</a>
  </button>
- Junior Rodrigues Ribeiro NUSP 9725190
  <button type="button">⟶
  <a href="https://github.com/j5r" target="_blank">Github</a>
  </button>
- Luiz Henrique Romero NUSP ...
  <button type="button">⟶
  <a href="https://github.com/neoluiz" target="_blank">Github</a>
  </button>

## DESCRIÇÃO

Este exercício implementa o algoritmo **Perceptron** com 1 neurônio artificial.

- O seu objetivo é classificar figuras com a letra "A" (cujo **label** é definido como +1) e a letra "∀" (cujo **label** é definido como -1).

## REQUERIMENTOS

O programa foi escrito na linguagem Python3, e faz uso da biblioteca **numpy**, a qual pode ser facilmente instalada com `pip3 install numpy`.

## EXECUÇÃO

Para executar o programa, abra um terminal com o comando

```bash
  python3 main.py
```

## DETALHES DE IMPLEMENTAÇÃO

### ENTRADAS

Os dados estão escritos em arquivos `.txt` na pasta `./trainment`. Cada arquivo contém um valor _value_, sendo +1 ou -1, e logo abaixo se tem uma matriz de caracteres separados por espaços.

O caractere ponto "." representa o fundo da imagem (que será interpretado como -1), e qualquer caracter imprimível que seja diferente de "." é considerado um pixel da imagem (que será interpretado como +1).

Para leitura desses arquivos, é criada uma interface `Item(file_name)` no arquivo `./trainment/input.py`. Esta interface faz a leitura dos arquivos e implementa os atributos

- `value` : valor do **label** da figura
- `array` : um 1-D `numpy.array()` carregando as informações dos pixels (+1 ou -1)
- `fname` : o nome do arquivo lido.

Os métodos especiais `__repr__()` e `__str__()` foram implementados para que se possa imprimir as figuras no terminal com `print(objeto)`.

**É possível que a impressão no terminal em ambientes Windows não seja correta, nesse caso, pode-se usar** `print(objeto.__repr__())`.

## PRINCIPAIS FUNÇÕES

### ARQUIVO `./perceptron.py`

Implementa as seguintes funções

1. `limit_degrau_bin(x)`
   > Função utilizada como função de ativação (não está sendo utilizada) do perceptron, do tipo degrau, qualquer valor para 'X' menor ou igual a zero retorna 0, se maior retorna 1
2. `sigmoid(x)`
   > Função utilizada como função ativação (não está sendo utilizada) do percepctron, do tipo sigmoide (1/(1+e^(-x))).
3. `limit_degrau_neg(x)`
   > Função utilizada como função de ativação (utilizada neste projeto) do perceptron, do tipo degrau, qualquer valor para 'X' menor ou igual a zero retorna -1, se maior retorna 1
4. `training_perceptron(entrada, saida, f_activ=limit_degrau_neg, delta=5e-1, maxInter=5e4)`

   > Função para criação e treinamento do perceptron, cuja a entrada é um vetor com as entradas (exemplo: um vetor de matrizes, onde cada matriz é uma entrada para uma saida do perceptron), sendo esse vetor genérico (podendo ser um ventor de inteiros, matrizes.. etc) apatir de listas ou tipo numpy.array. A saida sendo um vetor com os valores de saida do perceptron para cada entrada. Delta como parâmetro de aprendizagem, e maxInter como número maximo de iterações, uma vez estourada o treinamento irá gerar uma mensagem de alerta, mas continuará e devolverá o perceptron com os pesos da iteração maxInter (existindo saídas diferentes da esperada).

   - `perceptron(x)`
     > Objeto que define o perceptron treinado utilizando como função de ativação a mesma durante o treinamento. Caracterizando como o produto da entrada ('X') com os pesos e bias previamente calculados (entrada unica, exemplo: apenas uma matriz que foi utilizada no processo de aprendizagem).

### ARQUIVO PRINCIPAL `./main.py`

Este arquivo começa importando `import numpy as np`, `from perceptron import *` e `from trainment.input import Item`.
Após as importações ele carrega as 'k' entradas utilizadas para aprendizagem do perceptron (Utilizada como 10). Após a leitura e armazenagem das entradas (matriz) , o perceptron é treinado, e depois as n-k entradas são lidas e usadas como avaliação do perceptron. Durante a avaliação é printado a matriz com seu valor e com o valor estipulado pelo perceptron, por último é mostrado um resumo com números de acertos e erros do perceptron.
