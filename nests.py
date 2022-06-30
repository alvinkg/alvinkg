number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0]) 
print(number_grid[2][1]) 

# nested for loops

print("Printing rows.")
for row in number_grid:
    print(row)

    print("Printing columns.")
    for column in number_grid:
        print(column)

#print("Printing rows.")
for row in number_grid:
    #print(row)

    #print("Printing columns.")
    for col in row:
        print(col)