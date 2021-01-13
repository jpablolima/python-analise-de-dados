# Classes

# class Livro():
#     def __init__(self):
#         self.titulo = 'The Hobbit'
#         self.isbn = 100000
#         print('Construtor chamado para criar um objeto desta classe')
#     def imprimir(self):
#         print('Foi criado o livro %s e ISBN %d' %(self.titulo, self.isbn))

# Livro1 = Livro()
# print(Livro1.titulo)


# # Criando Classes Livro2

# class Book():
#     def __init__(self, titulo, isbn):
#         self.titulo = titulo
#         self.isbn = isbn
#         print('Construtor chamado para criar um objeto desta classe')
#     def imprimir(self, titulo, isbn):
#         print('Foi criado o livro %s e ISBN %d' %(titulo,isbn))

# Livro2 = Book('Ready Player One', 20000)
# Livro3 = Book('The Witcher', 30000)

# print(Livro2.titulo)
# print(Livro2.isbn)
# print(Livro3.titulo, Livro3.isbn)


# # Criando Classe Cachorro
# class Cachorro ():
#     def __init__(self, raca):
#         self.raca = raca
#         print('Construtor chamado para criar um objeto desta classe')

# Rex = Cachorro(raca='Labrador')
# Bob = Cachorro(raca = 'Huskie')

# print(Rex.raca, Bob.raca)




# #  Heroes

# class Heroes():
#     def __init__(self, comics, name, power, speed, intelligence, combat):
#         self.comics = comics
#         self.name = name
#         self.power = power
#         self.speed = speed
#         self.intelligence = intelligence
#         self.combat = combat
#         print('Construtor pata criação do Objeto.')
# HeroeMarvel = Heroes(comics="Mavel", power=1000, name = 'Spider Man', intelligence=100, combat=500, speed=50)
# HeroeDc = Heroes(comics="Dc", power="900", name="Batman", speed="200",intelligence=1500, combat=750)

# print('Name: ', HeroeMarvel.name)
# print('Comics: ',HeroeMarvel.comics)
# print('Power',HeroeMarvel.power)
# print('Intelligense: ',HeroeMarvel.intelligence)
# print('Speed: ',HeroeMarvel.speed)
# print('Compat: ',HeroeMarvel.combat)


# print('Name: ', HeroeDc.name)
# print('Comics: ',HeroeDc.comics)
# print('Power',HeroeDc.power)
# print('Intelligense: ',HeroeDc.intelligence)
# print('Speed: ',HeroeDc.speed)
# print('Compat: ',HeroeDc.combat)

# Ferias

class Ferias():
    def __init__(self, city):
        self.country = 'Brasil'
        self.city = city
        print('Construtor pata criação do Objeto.')

Ferias1 = Ferias(city='Brasília')
print("País: ", Ferias1.country)
print("Cidade: ", Ferias1.city)