import pytest
from parking_lot import Car

car_details = {
    "name": "Honda Jazz",
    "year": 2003,
    "fuel": "GPL",
    "kms": 250_000,
    "color": "Red",
    "state": "Good",
    "quality": "Low",
    "size": "Small",
}


def test_car():
    example_car = Car(**car_details)

    assert example_car.parked_days == 0

    # This must raise an error
    with pytest.raises(TypeError):
        example_car.park_vehicle(indoors=True)

    assert example_car.kms == 250_000

    example_car.park_vehicle(indoors=False)
    assert example_car.is_parked
    assert example_car.parked_days == 1

    more_kms = 100
    example_car.drive(kms=more_kms)
    assert example_car.kms == 250_000 + more_kms + 0.1
