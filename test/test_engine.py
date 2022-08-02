import unittest
from datetime import date
from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery

from engine.Capulet_engine import CapuletEngine
from engine.Sternman_engine import SternmanEngine
from engine.Willoughby_engine import WilloughbyEngine
import Car

class TestBattery(unittest.TestCase):
     def test_nubbin_battery_should_be_serviced(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

     def test_splinder_battery_should_be_serviced(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 2)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())


class TestEngine(unittest.TestCase):
    def test_calliope_instance(self):
        current_date = date.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        self.assertIsInstance(car,Car)



