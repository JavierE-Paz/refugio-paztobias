import cowsay

class Animal:

    def __init__(self, nombre: str, especie: str, edad: int):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.energia = 50

    def presentarse(self):
        cowsay.cow(f"Hola soy {self.nombre}. {self.especie}. Edad: {self.edad}.")

    def ajuste_energia(self):
        if self.energia >= 100:
            self.energia = 100
        elif self.energia <= 0:
            self.energia = 0

    def comer(self, gramos: int):
        self.energia = self.energia + (gramos // 10 )
        self.ajuste_energia()
        
        
    def jugar(self):
        self.energia = self.energia - 20
        self.ajuste_energia()
       
        

    def dormir(self):
        self.energia = self.energia + 30
        self.ajuste_energia()
        
        





