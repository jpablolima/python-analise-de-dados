# Classes

class Livro():
    def __init__(self):
        self.titulo = 'The Hobbit'
        self.isbn = 100000
        print('Construtor chamado para criar um objeto desta classe')
    def imprimir(self):
        print('Foi criado o livro %s e ISBN %d' %(self.titulo, self.isbn))

Livro1 = Livro()

print(Livro1.titulo)


# Criando Classes Livro2

class Book():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print('Construtor chamado para criar um objeto desta classe')
    def imprimit(self, titulo, isbn):
        print('Foi criado o livro %s e ISBN %d' %(titulo,isbn))

Livro2 = Book('Ready Player One', 20000)

print(Livro2.titulo)
print(Livro2.isbn)


# Criando Classe Cachorro
class Cachorro ():
    def __init__(self, raca):
        self.raca = raca
        print('Construtor chamado para criar um objeto desta classe')

Rex = Cachorro(raca='Labrador')
Bob = Cachorro(raca = 'Huskie')

print(Rex.raca, Bob.raca)

