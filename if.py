isMale = True
isTall =  True

if isMale:
    print("You are male.")
else:
    print("You are not male.")

if isTall:
    print("You are tall.")
else:
    print("You are not tall.")

if isMale or isTall:
    print("You are male or tall.")
else:
    print("You are neither male nor tall.")

if isMale and isTall:
    print("You are both male and tall.")
else:
    print("You are either not male or not tall.")

if isMale and isTall:
    print("You are both male and tall.")  
elif isMale and not(isTall):
    print("You are a short male.")
elif not(isMale) and isTall:
    print("You are a tall non-Male.")
else:
    print("You are neither male nor tall.")