def build_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about the car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    
    for key, value in car_info.items():
        car[key] = value
        
    return car
    
car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
    
