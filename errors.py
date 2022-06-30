try:
    print(int(input("Enter an integer. ")))
except ValueError as err:
    print(err)
