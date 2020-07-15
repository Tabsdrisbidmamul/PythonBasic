def make_car(manufacturer, model, **car_info):
    """store every bit of information about a car"""
    store_car = {}
    store_car['manufacter'] = manufacturer
    store_car['model'] = model
    for key, value in car_info.items():
        store_car[key] = value
    return store_car


build_car_0 = make_car('volkswagen', 'polo', color='black', doors=5, )
build_car_1 = make_car('audi', 'a6', color='silver', doors=5, )
build_car_2 = make_car('volkswagen', 'passat', color='grey', doors=5, )

print(build_car_0)
print(build_car_1)
print(build_car_2)
