from parking_lot import Car, MotorBike, Moto4

cars_info = [
    {
        "name": "Honda Jazz",
        "year": 2003,
        "fuel": "GPL",
        "kms": 250_000,
        "color": "Red",
        "state": "Good",
        "quality": "Low",
        "size": "Small",
    },
    {
        "name": "VW Beetle ",
        "year": 1962,
        "fuel": "Gas",
        "kms": 405_000,
        "color": "Orange",
        "state": "Worn",
        "quality": "Classic",
        "size": "Small",
    },
    {
        "name": "Ford F-150",
        "year": 2023,
        "fuel": "Diesel",
        "kms": 5000,
        "color": "Dark Blue",
        "state": "New",
        "quality": "Medium",
        "size": "Big",
    },
]

cars = [Car(**car) for car in cars_info]

cool_car = cars[0]

cool_car.parked_days
cool_car.get_parking_cost(indoors=False)
cool_car.park_vehicle(indoors=False)
cool_car.parked_days

if cool_car.is_parked:
    cool_car.parked_days += 1

cool_car.wash_inside()
cool_car.cleaning_cost

cool_car.drive(kms=100)

moto4_details = {
    "name": "Suzuki",
    "year": 2011,
    "kms": 2_500,
    "color": "Yellow",
    "state": "Good",
    "quality": "Low",
}

moto4_details = list(moto4_details.values())

# moto4_details = [
#    "Suzuki",
#    2011,
#    2_500,
#    "Yellow",
#    "Good",
#    "Low",
# ]


your_moto4 = Moto4(*moto4_details)
cars.append(your_moto4)

bike_details = {
    "name": "Honda CB350",
    "year": 2021,
    "kms": 5_500,
    "color": "Red",
    "state": "New",
    "quality": "Medium",
}

my_bike = MotorBike(**bike_details)
cars.append(my_bike)
