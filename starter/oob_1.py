class BankAccount:
    def __init__(self, name, balance, number):
        print("new Bankaccount created!")
        self.number = number
        self.name = name
        self.balance = balance

# make another object to add money
    def add(self, amount):
        self.balance += amount

# make another object to withdraw money
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

        else:
            print("not enough money..")

# print account details requires you to use dundersdrrunder (idk if thats what its called)
# to do that you must friend def the __str__
    def __str__(self):
        return f"Bank Account: {self.number, self.name, self.balance}"
