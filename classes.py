class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age =age
    
    def display_name(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Punit", 65)
person1.display_name()



#Q1

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    

#Q2
    
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    
    def display_account_details(self):
        return f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: {self.balance}" 

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y