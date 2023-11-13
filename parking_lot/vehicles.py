class BaseVehicle:
    """
    This is a base class to create a general definition of a vehicle.
    
    Arguments
    ---------
    name : str, default="vehicle"
        Name of the vehicle being defined.
        
    year : int, default=2023
        Year the vehicle was built.
    
    kms : [int, float], default=0
        Number of kms this vehicle has driven for.
        
    fuel : str, default="gas"
        Type of fuel used in the vehicle.
    
    (...)
    
    Attributes
    ----------
    wheel_count : NoneType
        Number of wheels in the vehicle
    
    can_park_indoors (...)
    (...)
    """
    
    wheel_count = None
    parked_days = 0
    is_parked = False
    cleaning_cost = 0
    
    def __init__(self, name, year, kms, fuel, color, state, quality, size):  
        self.name = name 
        self.year = year 
        self.kms = kms 
        self.fuel = fuel 
        self.color = color 
        self.state = state 
        self.quality = quality 
        self.size = size
        
        self.can_park_indoors = self.fuel != "GPL"
        
    def drive(self, kms):
        """
        Increment kms to the vehicle.
        
        Parameters
        ----------
        kms : [int, float]
            Number of kms to increment.
            
        Returns
        -------
        self
        """
        # The two lines below amount to the same result
        # self.kms += kms
        # self.kms = self.kms + kms
        self.kms += kms
        return self
    
    def get_parking_cost(self, indoors=True):
        """
        (...)
        """

        # Daily parking cost according to different specifications
        cost_quality = {"low": 2, "medium": 3, "high": 4}
        cost_size = {"small": 2, "large": 4}
        cost_maintenance = 2 if indoors else 0
        
        # Compute total cost using the criteria defined above
        total_cost = (
            cost_size[self.size.lower().strip()]
            + cost_quality[self.quality.lower().strip()]
            + cost_maintenance
        ) * self.parked_days + self.cleaning_cost
        
        return total_cost
    
    def park_vehicle(self, indoors=True):
        
        if indoors and (not self.can_park_indoors):
            print("The car cannot park indoors!")
            return self
        
        if not self.is_parked:
            self.drive(.1)
            self.parked_days += 1
            self.is_parked = True
        else:
            print("The car is already parked!")
        
        return self
    
    def return_vehicle(self):
        self.is_parked = False
        return self
    
    
    def __repr__(self):
        representation = (
            f"{self.__class__.__name__}("
            f"{self.color} {self.name} from {self.year}, "
            f"with {self.kms} Kms, {self.quality} quality"
            ")"
        )
        return representation


class Car(BaseVehicle):
    """
    Creates a Car object with 4 wheels.
    
    Arguments
    ---------
    name : str, default="vehicle"
        Name of the vehicle being defined.
        
    year : int, default=2023
        Year the vehicle was built.
    
    kms : [int, float], default=0
        Number of kms this vehicle has driven for.
        
    fuel : str, default="gas"
        Type of fuel used in the vehicle.
    
    (...)
    
    Attributes
    ----------
    wheel_count : NoneType
        Number of wheels in the vehicle
    
    can_park_indoors (...)
    (...)
    """
    wheel_count = 4

    def wash_inside(self):
        cost_size = {"small": 4, "large": 8}
        self.cleaning_cost += cost_size[self.size.lower().strip()]
        return self
    
    def wash_outside(self):
        cost_state = {"new": 3, "good": 5, "worn": 7}
        self.cleaning_cost += cost_state[self.state.lower().strip()]
        return self
    
    def clean_windshield(self):
        self.cleaning_cost += 2
        return self

class MotorBike(BaseVehicle):
    
    wheel_count = 2

    def __init__(self, name, year, kms, color, state, quality):
        # We are excluding size and fuel from the parameters
        super().__init__(
            name, year, kms, "gas", color, state, quality, "small"
        )

    # This would override __repr__
    # def __repr__(self):
    #     representation = (
    #         "MotorBike("
    #         f"{self.color} {self.name} from {self.year}, "
    #         f"with {self.kms} Kms, {self.quality} quality"
    #         ")"
    #     )
    #     return representation

class Moto4(MotorBike):
    wheel_count = 4
    def __init__(self, name, year, kms, color, state, quality):
        # We are excluding size and fuel from the parameters
        super().__init__(
            name, year, kms, color, state, quality
        )
        self.size = "medium"
