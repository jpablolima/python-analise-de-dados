import os 
import numpy as np
import matplotlib.pyplot as plt
filename = os.path.join('iris.csv')

# !more iris.csv

arquivo = np.loadtxt(filename, delimiter=',', usecols=(0,1,2,3), skiprows=1)
print(arquivo)

# Gerando um plot a partir de um arquivo usando o numpy
var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(0,1), skiprows=1, unpack=True)
plt.show(plt.plot(var1,var2,'o', markersize=8, alpha=0.75))