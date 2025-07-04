class Animal: 
    def comer(self):
        print('Comendo')

    def andar(self):
        print('Andando')

class Felino(Animal):
    def lamber(self):
        print('Felino lambendo o pelo')

#    def comer(): # Isso quebra o princípio pois o comportamento não é mais o mesmo
#       print('O felino come sachê')

class Pessoa():
    def observa(self, animal: Animal):
        animal.comer()

animal = Animal()
felino = Felino()
pessoa = Pessoa()


animal.comer()
felino.comer()

pessoa.observa(animal)
pessoa.observa(felino)

# note que, como a classe foi herdada, e não teve seu funcionamento alterado
# eu pude simplesmente chamr o mesmo método porém de duas classes diferentes 