# A program that showcases a shopping list

# object for every product
class Product:
    def __init__(self,
                 title,
                 quantity):
        self.title = title
        self.quantity = quantity
# product details

    def __str__(self,
                title,
                quantity):
        return f"Product name: {self.title}, Product quantity: {self.quantity}"

# new product quantity
    def change_Quantity(self,
                        quantity,
                        new_quantity):
        self.quantity = new_quantity


class ShoppingList:
    # create the list
    def __init__(self,
                 title):
        self.title = title
        self.Items = []

    def __str__(self):
        return f"SHOPPING LIST: {self.title}"

# define an object for the actual products
    def add(self, new_item):
        # but we have to make sure that the user doesn't just add ANY product but of the given inputs,
        # in order to do so, we have to make sure the new_Item is an Object of Product Class
        # Essentially, checking if its an instance of the class
        if isinstance(new_item, Product):
            self.Items.append(new_item)
            print("Item added")
        else:
            print("item doesn't exist")

# define an objetc to add products to the list
    def show(self):
        for item in self.Items:
            print(f"{item.title} {item.quantity}")
# define an objetc to print products list

# define an objetc to print products list
