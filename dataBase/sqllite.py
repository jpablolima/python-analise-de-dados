#  Criando Banco de Dados e inserindo Dados - sqlite3

# Remove o arquivo com o banco de dados SQLite (caso exista)

import os

os.remove('dsa.db') if os.path.exists('dsa.db') else None

import sqlite3

# Criando uma conexão

conn = sqlite3.connect('dsa.db')

# criando um cursor

c = conn.cursor()


# Função para criar uma tabela 

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
      'prod_name TEXT, valor REAL )')

# Função para inserir uma linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES(10, '2020-01-16', 'Teclado', 90)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_insert()