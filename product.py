class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Order:
    def __init__(self, items):
        self.items = items
        self.total_price = sum([item['product'].price * item['quantity'] for item in items])
        

class Cart:
    def __init__(self):
        self.items=[]

    def add_Item(self,product,quantity):
        for item in self.items:
            if item['product']==product:
                item['quantity']+=quantity
                return
        self.items.append({'product':product,'quantity':quantity})
    def remove_item(self,product):
        for item in self.items:
            if item['product']==product:
                self.items.remove(item)

    def empty_cart(self):
        self.items=[]