import random

class Product:

    def __init__(self):
        self.price = 5
        self.revenue = 8
        self.terms = random.randint(1,3)
        self.risk = round(random.random(), 2)

        self.owner = None
        self.roundsRemain = self.terms

    def update(self):

        rand = random.random()
        if rand < self.risk:
            print('BOOM![{:.2f}] {} missed {}! (balance:{})'.format( \
            rand, self.owner.name, self.revenue, self.owner.money))
            self.roundsRemain = -1

        self.roundsRemain -= 1
        if self.roundsRemain == 0:
            self.owner.money += self.revenue
            self.owner.myProduct
            print('{} +{}! (balance:{})'.format(self.owner.name, self.revenue, self.owner.money))

    def display(self):
        print('({},{},{},{})'.format(self.price, self.revenue, self.terms, self.risk))

class Player:

    def __init__(self, name):
        self.name = name
        self.money = 10
        self.myProduct = []


myPlayer = Player('Me')
roundCount = 0

while True:

    roundCount += 1
    print('Round #' + str(roundCount))

    for product in myPlayer.myProduct:
        product.update()
    myPlayer.myProduct = [product for product in myPlayer.myProduct if product.roundsRemain > 0]

    if myPlayer.money <= 0:
        print('Lose!')
        break
    if myPlayer.money >=20:
        print('Win!')
        break

    if len(myPlayer.myProduct) < 1:
        newProduct = Product()
        newProduct.display()

        myInput = input('Buy? (y/n): ')

        if myInput == 'y':
            myPlayer.myProduct.append(newProduct)
            newProduct.owner = myPlayer
            myPlayer.money -= newProduct.price
            print('{} -{}! (balance:{})'.format(myPlayer.name, newProduct.price, myPlayer.money))
