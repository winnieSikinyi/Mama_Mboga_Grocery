class Customer:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
        self.cart=Cart()
        
    def add_to_cart(self, product,quantity):
           self.cart.add_item(product,quantity)
    
    def remove_from_cart(self,product):
        self.cart.remove_item(product)
    
    def place_order(self):
        order=Order(self.cart.items)
        self.cart.empty_cart()
        return order