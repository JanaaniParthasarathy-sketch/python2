class Bird:
    def sound(self):
        print("Bird Sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")

class Crow(Bird):
    def sound(self):
        print("Caw Caw")

birds = [Sparrow(), Crow()]

for b in birds:
    b.sound()
