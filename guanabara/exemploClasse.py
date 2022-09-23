class Gato:

    def __init__(self,nome, i):
        self.nomecompleto = nome
        self.idade = i

    def miau(self):
        print("Minhauuu")

class Cachorro:

    def __init__(self,nome, idade,peso):
        self.nomecompleto = nome
        self.idade = idade
        self.peso = peso

    def latir(self):
        print("AUAUAUAUA")


gato1 = Gato("Saci", "3")

gato2 = Gato("Katakuri", "5")

gato3 = Gato("Nete", "12")

cao1 = Cachorro("Sabo","15",50)

cao2 = Cachorro(idade="20", peso=65, nome="Robin")

print(type(gato1))
print(cao1.nomecompleto, cao1.peso, cao1.idade)

print(cao1.latir())

print(gato2.nomecompleto)

print(cao2.nomecompleto)