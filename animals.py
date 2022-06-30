class Animals:
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True
    
    def isMammal(self):
        if self.mammals:
            print("It is a mammal.")
    
    def isDomestic(self):
        if self.domestic == True:
            print("It is a domesticated anial.")
    
