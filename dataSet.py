# # DataSet linha
# f = open('tratamentos-de-arquivos/arquivos/salarios.csv', "r")
# data  = f.read()
# rows = data.split('\n')
# print(rows)

# # DataSet em Colunas

# f = open('tratamentos-de-arquivos/arquivos/salarios.csv', "r")
# data = f.read()
# rows = data.split('\n')
# full_data = []

# for row in rows:
#     split_row = row.split(',')
#     full_data.append(split_row)
# print(full_data)


# Contando as linhas de um arquivo
f = open('tratamentos-de-arquivos/arquivos/salarios.csv', "r")
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
count = 0
for row in full_data:
    count += 1
print("Quantidade de linhas: " + str(count))


# Contando as Colunas de um arquivo
f = open('tratamentos-de-arquivos/arquivos/salarios.csv', "r")
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    first_row = full_data[0]
count = 0

for collumn in first_row:
    count = count + 1

print("Quantidade de Colunas : " + str(count))