class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if amount > self.balance:
            return f"{amount} exceeds your Account Balance"
        self.balance -= amount
        return self.balance

    
my_bank = BankAccount("tejas",3400)

print(my_bank.deposit(400))
print(my_bank.withdraw(4000))


print(my_bank.balance)