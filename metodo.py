class Circulo():
    pi = 3.14
    def __init__(self, raio = 8):
        self.raio = raio
    def are(self):
        return (self.raio * self.raio) * Circulo.pi
    def setRaio(self, novo_raio):
        self.raio = novo_raio
    def getRaio(self):
        return self.raio

circ = Circulo()    
circ.getRaio()

print('Raio: ', circ.getRaio())
print('Área: ', circ.are())