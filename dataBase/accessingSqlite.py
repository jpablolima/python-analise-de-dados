# Acessando Banco de Dados sqlite3


import os
os.remove('escola.db') if os.path.exists('ecola.db') else None

import sqlite3

connection = sqlite3.connect('escola.db')
type(connection)
print(connection)

# Criação do cursor para percorrer os registros em  um conjunto de dados 

cur = connection.cursor()

 # criação da tabela 

sql_create = 'Create table cursos ' \
     '(id integer primary key,' \
     'titulo varchar(100), ' \
     'categoria varchar(1400))'

#  instrução sql
cur.execute(sql_create)

#   criando sentença SQL para inserir registros

sql_insert = 'insert into cursos values(?, ?, ?)'

 # dados
recset = [(1000, 'Python', 'Ciência de Dados'), 
           (1001, 'JavaScript', 'Front-end'), 
           (1002, 'Java', 'Back-end')]

 # Inserindo os registros 

for rec in recset:
     cur.execute(sql_insert, rec)

 # Gravando transação

connection.commit()

#  Selecionar registros 
sql_select = 'select * from cursos'


#  selecionar todos os registros
cur.execute(sql_select)
dados = cur.fetchall()

#  mostrar os registros

for linha in dados:
    print('Cursos Id: %d, Titulo: %s, Categoria: %s \n' %linha)


