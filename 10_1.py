""" Написать класс Car Конструктор класса принимает атрибуты:
color: str (цвет)
count_passenger_seats: int (количество пассажирских мест)
is_baby_seat: bool (наличие десткого кресла)
is_busy: bool (определяется внутри конструктора со значением False, не принимается на вход)
1.1 Написать магический метод __str__ выводящий форматированную строку с информацией об автомобиле
"""
from typing import Type


class Car(object):

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool) -> None:
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat: bool = False

    def __str__(self, is_baby_seat=False) -> str:
        return f'Car: {self.color=}, {self.count_passenger_seats=}, {self.is_baby_seat=}'


""" Написать класс Taxi Конструктор класса принимает атрибуты:
cars: list[Car] (список экземпляров класса Car)
2.1 Реализовать метод find_car
На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров, наличие ребенка, 
примечание: количество пассажиров с учетом ребенка если он есть)
На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и свободный (is_busy = False), 
у автомобиля сменить атрибут is_busy на значение True, если подходящего автомобиля нет, метод должен возвращать None
"""


class Taxi(object):

    def __init__(self, cars: list[Car]) -> None:
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool) -> Car | None:
        for car in self.cars:
            if not is_baby and car.count_passenger_seats >= count_passengers:
                if is_baby and car.is_baby_seat:
                    is_baby = True
                    return car
                elif is_baby:
                    return None
                else:
                    is_baby = True
                    return car

car1 = Car('red', 6, False)
car2 = Car('red', 5, True)
cars1 = [car1, car2]
taxi = Taxi(cars=cars1)
print(taxi.find_car(2, False))  # проверка
