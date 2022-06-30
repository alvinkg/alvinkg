# create a class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email= email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and my age is {self.age}'

    def add_to_age(self):
        self.age += 1

# Extend class User
class Customer(User):
    def __init__(self, name, email, age):
        super().__init__(name, email, age)
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        #pass
        return f'My name is {self.name} and my age is {self.age} while my balance is {self.balance}'

brad = User('Brad', 'brad@gmail.com', 37)
print(type(brad))
print(brad.name)
print(brad.email)
print(brad.age)
print(brad.greeting())
brad.add_to_age()
print(brad.greeting())


janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)
print(type(janet))
print(janet.name)
print(janet.email)
print(janet.age)

print(janet.greeting())
janet.add_to_age()
janet.set_balance(500)
print(janet.greeting())