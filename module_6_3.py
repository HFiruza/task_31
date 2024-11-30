import random

class Animal: # класс описывающий животных
    # Класс обладает следующими атрибутами:
    live = True
    sound = None # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 # степень опасности существа

    # Объект этого класса обладает следующими атрибутами:
    _cords = [0, 0, 0] # координаты в пространстве
    speed = int # - скорость передвижения существа (определяется при создании объекта)
    def __init__(self, speed):
        self.speed = speed

    # И методами:
    def move(self, dx, dy, dz):
        if dz < 0:
            print(f"It's too deep, i can't dive :(")
        else:
            self._cords[0] = dx * self.speed
            self._cords[1] = dy * self.speed
            self._cords[2] = dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f"Sorry, i'm peaceful :)")
        else:
            print(f"Be careful, i'm attacking you 0_0")

    def speak(self):
        print(f'{self.sound}')

class Bird(Animal): # класс описывающий птиц. Наследуется от Animal
    # Должен обладать атрибутом:
    beak = True # наличие клюва

    # И методом:
    def lay_eggs(self):
        print("Here are(is)", str(random.randint(1, 4)), "eggs for you")

class AquaticAnimal(Animal): # класс описывающий плавающего животного. Наследуется от Animal
    # В этом классе атрибут
    _DEGREE_OF_DANGER = 3

    # Должен обладать методом:
    def dive_in(self, dz):
        self._cords[2] = abs(int(self._cords[2] / self.speed- dz // 2))

class PoisonousAnimal(Animal): # класс описывающий ядовитых животных. Наследуется от Animal
    # В этом классе атрибут
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click" # звук, который издаёт утконос

    def __init__(self, sound):
        super().__init__(sound)



db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

# print(Animal.mro())
# print(Bird.mro())
# print(AquaticAnimal.mro())
# print(PoisonousAnimal.mro())
#print(Duckbill.mro())