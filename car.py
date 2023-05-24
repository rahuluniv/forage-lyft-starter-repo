from abc import ABC, abstractmethod

class Serviceable:
    def needs_service(self) -> bool:
        raise NotImplementedError()


class Engine(Serviceable):
    def needs_service(self) -> bool:
        # Implementation for Engine service check
        pass


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        # Custom implementation for CapuletEngine service check
        pass


class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        # Custom implementation for SternmanEngine service check
        pass


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        # Custom implementation for WilloughbyEngine service check
        pass


class Battery(Serviceable):
    def needs_service(self) -> bool:
        # Implementation for Battery service check
        pass


class BatteryBase(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date


class SpindlerBattery(BatteryBase):
    def needs_service(self) -> bool:
        # Custom implementation for SpindlerBattery service check
        pass


class NubbinBattery(BatteryBase):
    def needs_service(self) -> bool:
        # Custom implementation for NubbinBattery service check
        pass

class Car:
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        # Implementation for creating a Calliope car
        # You can customize the initialization and additional parameters as needed
        return Car(current_date, last_service_date)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        # Implementation for creating a Glissade car
        # You can customize the initialization and additional parameters as needed
        return Car(current_date, last_service_date)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        # Implementation for creating a Palindrome car
        # You can customize the initialization and additional parameters as needed
        return Car(current_date, last_service_date)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        # Implementation for creating a Rorschach car
        # You can customize the initialization and additional parameters as needed
        return Car(current_date, last_service_date)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        # Implementation for creating a Thovex car
        # You can customize the initialization and additional parameters as needed
        return Car(current_date, last_service_date)