# Product Class
class Product:
    def __init__(self, product_name, price, discount, gst, quantity):
        self.product_name = product_name
        self.price = price
        self.discount = discount
        self.gst = gst
        self.quantity = quantity

    def display(self):
        print(f"Product: {self.product_name}, Price: {self.price}"
              f"Discount: {self.discount}, GST: {self.gst}, Quantity: {self.quantity}")

# Creating 5 product objects
p1 = Product("Laptop", 50000, 10, 18, 2)
p2 = Product("Mobile", 20000, 5, 12, 5)
p3 = Product("Tablet", 15000, 7, 12, 3)
p4 = Product("Headphones", 2000, 15, 18, 10)
p5 = Product("Monitor", 10000, 8, 18, 4)

# Accessing product data
print("---- Product Data ----")
p1.display()
p2.display()
p3.display()
p4.display()
p5.display()

