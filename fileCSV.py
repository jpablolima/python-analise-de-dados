# Manipulando arquivo CSV

import csv

with open('tratamentos-de-arquivos/arquivos/number.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((55,92,76))
    writer.writerow((62,14,86))

    with open('tratamentos-de-arquivos/arquivos/number.csv', 'r') as file:
        leitor = csv.reader(file)
        for x in leitor:
            print('número de colunas ', len(x))
            print(x)


with open('tratamentos-de-arquivos/arquivos/number.csv', 'r') as file:
    leitor = csv.reader(file)
    data = list(leitor)
    print(data)

for linha in data[1:]:
    print(linha)