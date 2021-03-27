import numpy as np

""" Para calcular el valor de pi, lo primero es definir cuantos puntos vamos a lanzar """
DOTS_TO_THROW = 100000000

""" Despues generamos puntos aleatorios en el eje Y y el eje X, y esas coordenadas las elevamos al cuadrado """

x_coordinates_square = np.power(np.random.rand(DOTS_TO_THROW), 2)
y_coordinates_square = np.power(np.random.rand(DOTS_TO_THROW), 2)

""" Sumamos los cuadrados de las coordenadas """
square_sum = np.add(x_coordinates_square, y_coordinates_square)

""" Verificamos qué par de coordenadas cayó dentro del circulo """
dots_inside_circle = np.count_nonzero(np.sqrt(square_sum) < 1)

""" Estimamos pi con la formula dada """
pi_estimated = 4 * (dots_inside_circle / DOTS_TO_THROW)
print(pi_estimated)