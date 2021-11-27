# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
import time


class TrafficLight:
    __color = {'red': ['\r\033[31m', 7], 'yellow': ['\r\033[33m', 2], 'green': ['\r\033[32m', 3]}

    def running(self):
        for color, param in self.__color.items():
            print(f'\r{param[0]} {color}', end='')
            time.sleep(param[1])


t_light = TrafficLight()
t_light.running()