class Product:
    product_count = 0
    
    def __init__(self, name, price,stock):
        self.name= name
        self.price = price
        self.stock = stock
        Product.product_count +=1
    def sell(self, quantity):
        if quantity <= self.stock or quantity == self.stock:
             self.stock -= quantity
             print(f"{quantity} units of {self.name} sold")
        else:
            print(f"Insufficient stock")
    def restock(self, quantity):
        self.stock = self.stock + quantity
        print (f"You restocked {self.name} with {quantity} units")
    def stock_value(self):
        return self.price * self.stock
    def __str__(self):
        return f"Product(Name: {self.name}, price: ${self.price:.2f}, stock: {self.stock})"
        
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchase_history = []
    def add_order(self, order):
        self.purchase_history.append(order)
    def total_spent(self):
        return sum(order.total_price() for order in self.purchase_history)
    def __str__(self):
        return f"Name: {self.name}[email: {self.email}, Total Spent: ${self.total_spent():.2f}]"
    
class Order:
    def __init__(self, product, quantity, customer):
        self.product = product
        self.quantity = quantity
        self.customer = customer
    def total_price(self):
        return self.product.price * self.quantity
        
    def __str__(self):
        return f"{self.customer.name} ordered {self.product.name}, {self.quantity} items. Total price is {self.total_price():.2f}"
    
class VIP(Customer):
    def __init__(self, name, email, discount_rate):
        super().__init__(name, email)
        self.discount_rate = discount_rate
        
    def total_spent(self):
        return sum(order.total_price() * (1 - self.discount_rate) for order in self.purchase_history)
        

if __name__ == "__main__":
    product1= Product("cereals", 500, 50)
    product2 = Product("legumes", 5000, 20)
    
    customer1 = Customer("Joan", "joan@gmail.com")
    customer2 = Customer("James", "james@gmail.com")
    customer3 = Customer("Alvin", "alvin@gmail.com")
    VIP_customer = VIP("Bob", "bob@gmail.com", 0.1)
    
    order1 = Order(product1, 5, customer1)
    order2 = Order(product2, 10, customer2)
    order3 = Order(product2, 10, VIP_customer)
    
    product1.sell(5)
    customer1.add_order(order1)
    
    product2.sell(20)
    customer2.add_order(order2)
    VIP_customer.add_order(order3)
    
    product2.restock(10)
    
    print("\n--- Products ---")
    print(product1)
    print(product2)

    print("\n--- Customers ---")
    print(customer1)
    print(customer2)
    print(customer3)
    print(VIP_customer)

    print("\n--- Orders ---")
    print(order1)
    print(order2)
    print(order3)