<style>
h1{color:#0a306c;font-weight:bold}
h2{color:#1056a5}
h3{color:#4076b5}
li{color:#5085c0}
</style>

# REDES NEURAIS ARTIFICIAIS, DISCIPLINA SCC5809

## Grupo 6, Autores:

- Júlio... NUSP ...
- Junior Rodrigues Ribeiro NUSP 9725190
- Luiz Henrique Romero NUSP ...

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
   > Esta função faz ...
2. `sigmoid(x)`
   > Esta função faz ...
3. `limit_degrau_neg(x)`
   > Esta função faz ...
4. `training_perceptron(entrada, saida, f_activ=limit_degrau_neg, delta=5e-1, maxInter=5e4)`

   > esta função faz ...

   - `perceptron(x)`
     - esta função faz ...

### ARQUIVO PRINCIPAL `./main.py`

Este arquivo começa importando `import numpy as np`, `from perceptron import *` e `from trainment.input import Item`.
