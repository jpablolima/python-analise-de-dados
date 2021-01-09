import pandas as  pd;

file_name = 'tratamentos-de-arquivos/arquivos/binary.csv'

df = pd.read_csv(file_name)
df.head()
print(df)


file2 = 'tratamentos-de-arquivos/arquivos/salarios.csv'
df2 = pd.read_csv(file2)
print(df2)