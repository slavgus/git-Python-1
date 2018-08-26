# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = 0

    def go(self):
        print ('Начинаю движение')
    def stop(self):
        print('Останавливаюсь')
    def turn(self, direction):
        print('Поворачиваю', direction)

class TownCar(Car):
    def __init__(self, name, speed, color):
        Car.__init__(self, name, speed, color)

class SportCar(Car):
    def __init__(self, name, speed, color):
        Car.__init__(self, name, speed, color)

class WorkCar(Car):
    def __init__(self, name, speed, color):
        Car.__init__(self, name, speed, color)

class PoliceCar(Car):
    def __init__(self, name, speed, color):
        Car.__init__(self, name, speed, color)
        self.is_police = 1

Car1 = TownCar('Toyota Yaris','160','red')
Car2 = SportCar('Chevrolet Corvette','300','yellow')
Car3 = WorkCar('Ford F150','140','silver')
Car4 = PoliceCar('Dodge Charger','240','black & white')

car_set = (Car1,Car2,Car3,Car4)

for item in car_set:
    print ('Характеристики автомобиля:')
    print('Название:',item.name)
    print('Скорость:', item.speed)
    print('Цвет:', item.color)
    print('Является ли полицейской:', 'Да','\n') if item.is_police == 1 else print('Является ли полицейской:', 'Нет','\n')

    print('Проверка функций:')
    Car1.go()
    Car2.stop()
    Car3.turn('направо')
    Car4.turn('налево')

    print('___________________________________\n')


