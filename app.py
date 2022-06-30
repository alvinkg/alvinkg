from math import *

name = "john"
age = "36"

print("Hello World")
print("    /|")
print("   / |")
print("  /  |")
print(" /___|")
print("The man's name was " + name + " and he was already ")
print(age +" years old.")
print("Giraffe \n Academy") 
print("Giraffe\"s Academy") 
print("Giraffe's Academy")
phrase = "Giraffe Academy"
print(phrase + " is cool.")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
# index fn
print(phrase.index("a"))
# replace fn
print(phrase.replace("Giraffe", "Elephant"))

# working with numbers
print(2)
print(2.0987)
print(3+4.5)
print(2*(4+4))
my_num = 5
print(my_num)
print(str(my_num) +" is my favorite number.")

# abs fn
print(abs(-5.453))
my_num = -4.577
print(abs(my_num))

# pow fn
print(pow(3,2))

# max fn
print(max(my_num, 10))
print(max(4,6))
print(str(my_num) + " is the best.")
print(round(3.222))
print(round(3.722))

# math fn
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

# input fn
your_name = input("Enter your name: ")
your_age = input("Enter your age. ")
year = 2022 - int(your_age)
print(year)
print("Hello " + your_name + ". Great to meet you.")
print("You were born in " + str(year) + ".")

# Add numbers
num1 = input("Enter a number.")
num2 = input("Enter a number.")
result = num1 + num2
print(result)
result2 = int(num1)+int(num2)
print(result2)