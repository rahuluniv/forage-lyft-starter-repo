import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Engine(Serviceable):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 30000

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 60000

class Battery(Serviceable):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class BatteryBase(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

class SpindlerBattery(BatteryBase):
    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= 730

class NubbinBattery(BatteryBase):
    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= 1460

class Car:
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)


class TestCar(unittest.TestCase):
    def test_calliope_needs_service(self):
        current_date = date(2023, 5, 24)
        last_service_date = date(2020, 5, 24)
        current_mileage = 40000
        last_service_mileage = 20000

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade_needs_service(self):
        current_date = date(2023, 5, 24)
        last_service_date = date(2022, 5, 24)
        current_mileage = 80000
        last_service_mileage = 50000

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_palindrome_needs_service(self):
        current_date = date(2023, 5, 24)
        last_service_date = date(2020, 5, 24)
        warning_light_on = True

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service())

    def test_rorschach_needs_service(self):
        current_date = date(2023, 5, 24)
        last_service_date = date(2022, 5, 24)
        current_mileage = 80000
        last_service_mileage = 50000

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_thovex_needs_service(self):
        current_date = date(2023, 5, 24)
        last_service_date = date(2020, 5, 24)
        current_mileage = 40000
        last_service_mileage = 20000

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()
