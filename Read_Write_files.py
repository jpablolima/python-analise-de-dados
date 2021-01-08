# Abrindo arquivos para leitura
arql = open('tratamentos-de-arquivos/arquivos/arquivo1.txt', "r")

# leitura do arquivo
print(arql.read())

#  Contar a quantidade de caracteres 
print(arql.tell())

# Retornar para  o início do arquivo
print(arql.seek(0,0))
arql2 = open('tratamentos-de-arquivos/arquivos/arquivo1.txt', "w")

# Gravando arquivo
arql2.write('Python e JavaScript')

arql2.close()

arql2 = open('tratamentos-de-arquivos/arquivos/arquivo1.txt', "r")

print(arql2.read())

# Acrencentando conteúdo 
arql2 = open('tratamentos-de-arquivos/arquivos/arquivo1.txt', "a")


arql2.write('NodeJs, HTML, CSS, Java')

arql2.close()
print(arql.read())
