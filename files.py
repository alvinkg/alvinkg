myFile = open('myfile.txt', 'w')
print('Name:', myFile.name)
print('Is Closed:', myFile.closed)
print('Open Mode:', myFile.mode)

# write to file myFile
myFile.write("I love python")
myFile.close()
myFile = open('myfile.txt', 'a')
myFile.write(" and I also like js")
myFile.close()

# read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)