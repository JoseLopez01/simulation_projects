from numpy import double
from numpy.random import f


seed =  '12'
CONSTANT = '32'

numbers_to_generatee = 4
sw = False

for i in range(0, numbers_to_generatee):
  if len(seed) == len(CONSTANT) or sw:
    # Obtenemos el tamaño para n
    N = len(seed)
    # Multiplicamos la semilla por la constante
    result = str(float(seed) * float(CONSTANT))
    print(result)
    # Obtenemos el indice en el que debemos empezar a separar la nueva cadena
    start_index = int(len(result) / 2)
    print(start_index)
    # Obtenemos la nueva semilla
    seed = result[start_index:len(seed) + 1]
    sw = True
    print(seed)