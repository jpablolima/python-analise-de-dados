import numpy as np
import matplotlib.pyplot as plt


# criando array

# vector1  = np.array([0,1,2,3,4,5,6,7,8,9])
# print(vector1)

# # método do array numpy
# print(vector1[5])

# vector1[0] = 1000

# print(vector1[0])


# Funções Numpy

vector2  = np.arange(0., 4.5, .5)
# print(vector2)

x = np.arange(1,10,0.25)
# print(x)

# retorna 1 nas posições em diagonal  e 0 no restante
z = np.eye(3)
# print(z)

# os valores pasados como parâmetro, formam a diagonal

d = np.diag(np.array([1,2,3,4,6,7,8,9]))
# print(d)

# valores igualmente distribuidos no intervalo especificado

values = np.linspace(0,10)
# print(values)


# Random() Numpy

# %matplotlib inline
print(np.random.rand(10))
plt.show((plt.hist(np.random.rand(1000))))
print(np.random.rand(5,5))
plt.show((plt.hist(np.random.rand(1000))))