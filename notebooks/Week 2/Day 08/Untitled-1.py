class BankAccount:
    bank = "HBL" #works for both
    def __init__(self, owner, balance=0):     # runs when an account is created works indiidually for each
        self.owner = owner                    # store data ON this object
        self.balance = balance

# Instantiation: build objects from the blueprint. BankAccount(...) calls __init__.
ali = BankAccount("Ali", 5000)
zara = BankAccount("Zara")                     # balance defaults to 0

print(ali.owner, ali.balance)  
print (ali.bank)                # read attributes with a dot
print(zara.owner, zara.balance)

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for mark in self.marks:
            sum = sum + mark
            avg = sum/len(self.marks)
        return avg

    def grades(self):
        avg = self.average()
        if (avg >= 80):
            return "A+"
        elif (avg >= 70):
            return "B"
        elif (avg >= 60):
            return "B"
        else:
            return "F"

New = student("Fatima" , [85,92,78])

print (New.name)
print (New.marks)
print (New.average())
print (New.grades())

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._bank = "HBL"
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False

    def balance(self):
        return self.__balance

    def transfer(self, other, amount):
        if self.withdraw(amount):
            other.deposit(amount)
            return True
        return False


acc1 = Account("Ali", 5000)
acc2 = Account("Ahmed", 3000)

acc1.deposit(2000)

print(acc1.owner)
print(acc1._bank)
print(acc1.balance())

acc1.transfer(acc2, 3000)

print("Ali balance:", acc1.balance())
print("Ahmed balance:", acc2.balance())