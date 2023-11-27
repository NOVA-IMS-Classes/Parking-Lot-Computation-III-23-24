from parking_lot.vehicles import Car


class ParkingLot:
    """
    TODO: Add docstring
    """

    def __init__(self, total_slots, indoors, cleaning_services, vehicles=None):
        self.total_slots = total_slots
        self.indoors = indoors
        self.cleaning_services = cleaning_services
        self.vehicles = vehicles if vehicles is not None else []

    def add_vehicle(self, vehicle):

        if self.total_slots <= 0:
            raise ValueError("There is no more space in the parking lot!")

        if type(vehicle) == Car:
            self.total_slots -= 2
        else:
            self.total_slots -= 1

        self.vehicles.append(vehicle)

        return self

    def __len__(self):
        return len(self.vehicles)
