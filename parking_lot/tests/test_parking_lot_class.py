from parking_lot import ParkingLot, Car, MotorBike, Moto4


def test_basic_parking_lot_obj():
    pl = ParkingLot(total_slots=20, indoors=True, cleaning_services=True, vehicles=None)

    assert pl.vehicles == []

    car = Car(
        "Honda Jazz",
        year=2003,
        kms=250_000,
        fuel="GPL",
        color="Red",
        state="Good",
        quality="Low",
        size="Small",
    )
    pl.add_vehicle(car)
    assert len(pl) == 1
