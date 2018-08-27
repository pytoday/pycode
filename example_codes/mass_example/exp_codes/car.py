#!/usr/bin/env python3
# coding=utf-8
# title          :car.py
# description    :practice for class
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/3 18:38
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


class Car:      # class Car():  Is ok too!
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reader = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reader) + ' miles on it.')

    def update_odometer(self, meter):
        if self.odometer_reader <= meter:
            self.odometer_reader = meter
        else:
            print("SHIT, Don't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles != 0:
            self.odometer_reader += miles
        else:
            print("SHIT, Don't roll back an odometer!")


class Battery:
    def __init__(self, battery_size=100):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-KWh battery')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #    print('This car has a ' + str(self.battery_size) + '-KWh battery')

# my_new_car = Car('audi', 'A4', 2017)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(34)
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()

# my_tesla = ElectricCar('tesla', 'model s', 2017)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
