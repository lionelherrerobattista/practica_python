from car import Car #importo el archivo
from car import ElectricCar

# ~ my_used_car = Car('audi', 'a4', 2016)
# ~ print(my_used_car.get_descriptive_name())

# ~ my_new_car.odometer_reading = 23 # modifico atributo directamente
# ~ my_used_car.update_odometer(23500)
# ~ my_used_car.read_odometer()

# ~ my_used_car.increment_odometer(100)
# ~ my_used_car.read_odometer()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
