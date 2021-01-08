# Automating Recording Process

fileName = input('Enter the file name: ')

fileName = fileName + ".txt"
arql = open(fileName, "w")
arql.write('Successfully created file!')
arql.close()
arql = open(fileName, 'r')
print(arql.read())
arql.close()