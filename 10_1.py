""" Написать класс Car Конструктор класса принимает атрибуты:
color: str (цвет)
count_passenger_seats: int (количество пассажирских мест)
is_baby_seat: bool (наличие десткого кресла)
is_busy: bool (определяется внутри конструктора со значением False, не принимается на вход)
1.1 Написать магический метод __str__ выводящий форматированную строку с информацией об автомобиле
"""
from typing import Type


class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool) -> None:
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat

    def __str__(self, is_busy=False) -> str:
        return f'Car: {self.color}, {self.count_passenger_seats}, {self.is_baby_seat}'


""" Написать класс Taxi Конструктор класса принимает атрибуты:
cars: list[Car] (список экземпляров класса Car)
2.1 Реализовать метод find_car
На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров, наличие ребенка, 
примечание: количество пассажиров с учетом ребенка если он есть)
На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и свободный (is_busy = False), 
у автомобиля сменить атрибут is_busy на значение True, если подходящего автомобиля нет, метод должен возвращать None
"""


class Taxi(Car):

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        super().__init__(color, count_passenger_seats, is_baby_seat)
        self.cars = list[Car]

    def find_car(self, count_passengers: int, is_busy: bool) -> Type[list[Car]] | None:

        if is_busy is False and count_passengers <= self.count_passenger_seats:
            return self.cars
        else:
            return None


print(Taxi('red', 5, False).find_car(4, False))  # проверка
