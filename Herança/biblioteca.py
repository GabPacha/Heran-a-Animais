class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer.")
    def emitirSom(self):
        print(f"O {self.nome}  urrou")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def comer(self):
        print(f"O {self.nome} foi comer.")
    def emitirSom(self):
        print(f"O {self.nome} miou")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def comer(self):
        print(f"O {self.nome} foi comer.")
    def emitirSom(self):
        print((f"O {self.nome} latiu"))

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def comer(self):
        print(f"O {self.nome} foi comer.")

    def emitirSom(self):
        print((f"O {self.nome} chiou"))

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def comer(self):
        print(f"A {self.nome} foi comer.")

    def emitirSom(self):
        print((f"A {self.nome} mugiu"))