def sayhi():
    print("plain sayhi")
    print("Hello User")
sayhi()

# with parameter
def sayhi(name):
    print("sayhi with parameter")
    print("Hello User" + name)
sayhi("Alvin")

# with two parameters
def sayhi(name, age):
    print("Hi "+name + ", you are "+ age +" this year.")
sayhi("john", str(31))
def sayhi(name, age):
    print("Hi "+ name + ", you are "+str(age)+" this year.")
sayhi("Makre", 33)

