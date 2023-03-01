# Create a single class called Account. Upon initialization, it should receive owner (str) and amount (int, optional, 0 by default). It should also have an attribute called _transactions (empty list upon initialization). Create the following methods:
# ⦁	add_transaction(amount) - if the amount is not an integer, raise ValueError with message "please use int for amount", otherwise, add the amount to the transactions
# ⦁	balance() - property that returns sum of the amount and all the transactions
# ⦁	validate_transaction(account: Account, amount_to_add)
# ⦁	If the balance becomes less than zero, raise ValueError with message "sorry cannot go in debt!" and break the transaction.
# ⦁	Otherwise, complete it and return a message "New balance: {account_balance}"
# Implement the correct magic methods, so the code in the example bellow works properly

class Account:
    def __init__(self, owner, amount = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.amount += amount_to_add
        return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return reversed(self._transactions)

    def __le__(self, other):
        return self.balance <= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        result = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        result._transactions = self._transactions + other._transactions
        return result


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
print(acc.validate_transaction(acc, 20))
print(acc.validate_transaction(acc, -200))
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
