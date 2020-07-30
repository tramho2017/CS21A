class ShoppingCart:

    def __init__(self,ShoppingList,subtotal):
        self.ShoppingList=ShoppingList
        self.subtotal=subtotal
    def addItem(self,item):
        self.ShoppingList.append(item)

    def getsubtotal(self):
        return self.shoppingQuatity*self.price
    def subtractitem(self):
        return self.inventory-self.shoppingQuatity

class Product:
    def init(self,price,shoppingQuatity,inventory,productCategory):
        self.price=price
        self.shoppingQuality=shoppingQuatity
        self.inventory=inventory
        self.productCaterory=productCategory
    def setPrice:

class Toy:
    def setageGroup(self):

class BabyToy(Toy,Product):
    def __init__(self,name, safetyinfor,agegroup):
class Food:
    def setExpirationDate

class Frozendesert(Food,Product):
    def __nit__(self,size,refrigerationTemperature):

