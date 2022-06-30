# start
try:
    employee_file = open("employees.txt", "r")
    records = employee_file.readlines()
    for i in records:
        r = employee_file.readline()
        print(i, r)

finally:
    employee_file.close()

if not employee_file.closed:
    print("close the file")

# Check if file is readable
##print(employee_file.readable())
# each read cmd index the start point 
#print(employee_file.readline())
#print(employee_file.readline())
#xprint(employee_file.readline()) # Now the start is on index = 0
# danger of exceeding list index range
#x records = employee_file.readlines()
#x l = len(records)
#x print(l)
#x print(records)
#print(employee_file.readlines()[1])
 