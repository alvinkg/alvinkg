file = open("employees.txt", "a")
newEmployee = str(input("Please enter a new employee. "))
print(newEmployee)
file.write(newEmployee + '\n')
file.close()

# d = "abc"
# with open('employees.txt', 'a') as f:
#     f.write(d + '\n')