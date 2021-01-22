import pandas as pd
import numpy as np
import sys


print(pd.__version__)

# método read_csv
df = pd.read_csv('salarios.csv')
# print(df)

# método read_table
df = pd.read_table('salarios.csv', sep = ',')
# print(df)

#alterando título da coluna

df = pd.read_csv('salarios.csv', names = ['A', 'B', 'C', 'D'])
# print('Alteração do título da coluna \n',df)

# gerar arquivo csv depois das manipulações
# data = pd.read_csv('salarios.csv')
# data.to_csv(sys.stdout, sep = '|')
# print(data)


# criando DataFrame
dates = pd.date_range('20200122', periods = 10)
df = pd.DataFrame(np.random.randn(10,4), index = dates, columns = list("ABCD"))
print('DataFrame \n',df)

print("Primeira linhas \n",df.head())
print('Describe \n',df.describe())
print('Mean \n', df.mean())