#Class Modeling in Python- Vehicles
class Vehicle:

    """Vehicle"""

    def __init__(self, model, brand, licensePlate):
        self._model = model
        self._brand = brand
        self._licensePlate = licensePlate
        self._year = None
    
    #Get

    @property
    def model(self):
        return self._model
    
    @property
    def brand(self):
        return self._brand

    @property
    def licensePlate(self):
        return self._licensePlate

    @property
    def year(self):
        return self._year

    #set

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    @licensePlate.setter
    def licensePlate(self, new_licensePlate):
        self._licensePlate = new_licensePlate
    
    @year.setter
    def year(self, new_year):
        self._year = new_year

    #function

    def accelerating(self):
        print('Vroom')

    def decelerating():
        print('Urch')
    
    def doorOpening():
        print('after you, madaam')

    def winshieldWiping():
        print('Woosh')

    
