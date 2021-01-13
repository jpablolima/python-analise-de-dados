# Super-Classe

class Animal():
    def __init__(self):
        print("Animal criado!")
    
    def Identif(self):
        print("Animal")
    
    def comer(self):
        print('Comendo')

# Sub-Classe

class Cachorro():
    def __init__(self):
        Animal.__init__(self)
        print('Objeto cachorro criado')
    def Identif(self):
        print('Cachorro')
    def latir(self):
        print('Au, Au')

bob = Cachorro()
bob.Identif()
bob.latir()
