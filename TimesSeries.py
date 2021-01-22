#  Times Series


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# range da datas com frequência de segundos
rng = pd.date_range('22/01/2021', periods = 50,  freq = "S")
ts  = pd.Series(np.random.randint(0,500,len(rng)), index = rng)
print('Segundos \n',ts)

# range da datas com frequência de meses
rng = pd.date_range('22/01/2021', periods = 5,  freq = "M")
ts  = pd.Series(np.random.randint(0,500,len(rng)), index = rng)
print('Meses \n',ts)


# Plotting

ts = pd.Series(np.random.random(500), index=pd.date_range('21/01/2021', periods = 500))
ts = ts.cumsum()
ts.plot()

df = pd.DataFrame(np.random.randn(500,4), index = ts.index, columns = ['A', 'B','C','D'])
df = df.cumsum()
plt.figure(); 
df.plot();
plt.legend(loc = 'best')