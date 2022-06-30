from animals import Animals

class Dogs(Animals):
    def __init__(self):
        super().__init__()

    def isMammal(self):
        return super().isMammal()

class Horses(Animals):
    def __init__(self):
        super().__init__()

    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail.")

Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()