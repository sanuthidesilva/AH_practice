from starter.oob_1 import BankAccount

acc1 = BankAccount(name="alex", number=123, balance=0)
print(acc1)
print(type(acc1))

print(acc1.number)
print(acc1.name)
print(acc1.balance)

acc2 = BankAccount(name="mark", number=127, balance=100)
print(acc2.number)
print(acc2.name)
print(acc2.balance)

# acc1.add(20)
# print(acc1.balance)
# acc1.withdraw(10)
# print(acc1.balance)
# acc1.withdraw(10)
# print(acc1.balance)
# acc1.withdraw(10)
# print(acc1.balance)
