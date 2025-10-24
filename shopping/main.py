from shoppinglist import ShoppingList, Product

list1 = ShoppingList("grocery")

print(list)
list1.show()

product1 = Product('Apple', 2)
product2 = Product('Choco', 3)
product3 = Product('Coconut', 3)
product4 = Product('Rice', 5)
product5 = Product('Milk', 5)

list1.add(product2)
list1.add(product3)
list1.add(product5)
list1.add('flour')
list1.add('Banana')

print(list1)
list1.show()
