# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущую скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущую скорость автомобиля {self.speed} км/ч')
        if self.speed > 60:
            print(f'Превышении скорости! Ограничение 60 км/ч')


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущую скорость автомобиля {self.speed} км/ч')
        if self.speed > 40:
            print('Превышении скорости! Ограничение 40 км/ч')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car = TownCar(80, 'красная', 'BMW', False)
print(town_car.name, town_car.color)
town_car.go()
town_car.show_speed()
town_car.turn('на право')
town_car.stop()