class Bassist(object):
    def __init__(self):
        self.sounds = ["Twang", "Thrumb", "Bling"]

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()

class Guitarist(object):
    def __init__(self):
        self.sounds = ["Boink", "Bow", "Boom"]


    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        

david = Musician(["Twang", "Thrumb", "Bling"])
david.solo(6)