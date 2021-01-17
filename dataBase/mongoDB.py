# MongoDB

# instalação pymongo
# !pip install pymongo


# importando MongoClient para conectar aplicação ao MongoDB
from pymongo import MongoClient

# Estabelecendo conexão com Banco de Dados 

conn = MongoClient('localhost', 27017)
# type(conn)

# criação do banco de dados 
db = conn.cadastrodb

# criando coleção 
collection = db.cadastrodb

import datetime

post = {"codigo": "ID = 1000",
        "prod_name": "Carro",
        "marcas": ["ferrari","bmw","lamborghini"],
        "data_cadastro": datetime.datetime.utcnow()}


collection = db.posts

post_id = collection.insert_one(post)
post_id.inserted_id
post_id


# navegar pelos dados
for post in collection.find():
    print(post)

db.name
db.collection_names()