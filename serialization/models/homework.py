

import random
import uuid
from operator import attrgetter
from . constants import CARS_PRODUCER, CARS_TYPES, TOWNS


class Car:

    def __init__(self, mileage: float, price: float):
        self.producer = random.choice(CARS_PRODUCER)
        self.type = random.choice(CARS_TYPES)
        self.mileage = mileage
        self.price = price
        self.change_number()

    def __repr__(self):
        return "Car - type: {}, producer: {}, number: {}, mileage: {}, price: {}".format(
            self.type,
            self.producer,
            self.number,
            self.mileage,
            self.price)

    def __eq__(self, other):
        """
        comparing objects by price attribute
        :param other: Car class object
        :return: bool
        """
        return self.price == other.price

    def __lt__(self, other):
        """
        comparing objects by price attribute
        :param other: Car class object
        :return: bool
        """
        return self.price < other.price

    def __gt__(self, other):
        """
        comparing objects by price attribute
        :param other: Car class object
        :return: bool
        """
        return self.price > other.price

    def change_number(self):
        """
        Randomly change car number
        :return:
        """
        self.number = str(uuid.uuid4())


class Garage:

    def __init__(self, places: int, owner=None):
        self.cars = []
        self.places = 0
        self.town = random.choice(TOWNS)
        self.places = places
        if owner:
            self.set_owner(owner.register_id)
        else:
            self.owner = None

    def __repr__(self):
        return "Garage - owner: {}, town: {}, places: {}, cars count: {}".format(
            self.owner,
            self.town,
            self.places,
            self.cars_count()
        )

    def _car_numbers(self):
        return [x.number for x in self.cars]

    def set_owner(self, owner_id: str):
        """
        uses to set garage owner
        :param owner_id: str(uuid.uuid4)
        :return:
        """
        self.owner = owner_id

    def cars_count(self):
        """
        uses to calculate total cars count
        :return: float
        """
        return len(self.cars)

    def add_car(self, car):
        """
        Uses to add any Car to garage
        :param car: Car Object
        :return:
        """
        if car.number not in self._car_numbers():
            self.cars.append(car)
            self.places -= 1
            print("{} added to {}".format(car, self))
        else:
            print("{} already in {}".format(car, self))


    def remove_car(self, car):
        """
        Uses to remove car from garage, if car exists in garage
        :param car: any Car instatnce
        :return:
        """
        if car.number in self._car_numbers():
            self.cars = [c for c in self.cars if not c.number == car.number]
            self.places += 1
            print("{} removed from {}".format(car, self))
        else:
            print("{} not in {}".format(car, self))

    def hit_hat(self):
        """
        uses to calculate garage's cars total cost
        :return: float
        """
        return sum([x.price for x in self.cars])


class Cesar:

    def __init__(self, name: str):
        self.name = name
        self.garages = []
        self.register_id = str(uuid.uuid4())

    def __repr__(self):
        return "{}, id: {}, garages: {}".format(self.name, self.register_id, self.garages_count())

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def _have_free_place(self):
        """
        uses to get garage with max free spaces
        :return: Garage
        """
        if len(self.garages):
            return max([x for x in self.garages if x.places > 0], key=attrgetter("places"))
        else:
            print("{} do not have enough free places in garages!".format(self))
            return None

    def _all_cars(self):
        """
        uses to get all cars from all owner's garages
        :return: Cars List
        """
        all_cars = []
        for garage in self.garages:
            all_cars += garage.cars
        return all_cars

    def add_garage(self, garage: Garage):
        """
        uses to add garage to owner
        :param garage: Garage
        :return:
        """
        if garage:
            garage.set_owner(self.register_id)
            self.garages.append(garage)


    def hit_hat(self):
        """
        uses to calculate sum of owners's cars cost
        :return: float
        """
        return sum([x.price for x in self._all_cars()])

    def garages_count(self):
        """
        uses to calculate garages count
        :return: float
        """
        return len(self.garages)

    def cars_count(self):
        """
        uses for calculate cars count for all garages
        :return: float
        """
        return len(self._all_cars())

    def add_car(self, car: Car):
        """
        uses to add car to owner's garage
        :param car: Car
        :return:
        """
        garage = self._have_free_place()
        if garage:
            garage.add_car(car)

