"""
Battery Upgrade: Use the final version of electric car.py from this section. 
Add a method to the Battery class called upgrade_battery(). 
This method should check the battery size and set the capacity to 65 if it isn't already. 
Make an electric car with a default battery size, call get_range() once, and then call get_range()
a second time after upgrading the battery. 
You should see an increase in the car's range.
"""


class Car:
    pass


class Battery:
    def __init__(self):
        self.battery_size = 20

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

    def get_range(self):
        print(f'Battery Size: {self.battery_size}')


class ElectricCar(Car):

    def __init__(self):
        super().__init__()
        self.battery = Battery()


electric = ElectricCar()
electric.battery.get_range()

# Upgrading battery
electric.battery.upgrade_battery()
electric.battery.get_range()
