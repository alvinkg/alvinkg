from student import Student

jim = Student("Jim", "Science", 3.4, False)
print(jim.name)
print(jim.gpa)

pam = Student("Pam", "Art", 1.5, True)
print(pam.name)
print(pam.major)
print("Is Pam on probation? ")
print(pam.probation)

print("Is Pam on the honors roll?  ")
print(pam.honors())
