from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.__number_of_doors = number_of_doors

    def get_number_of_doors(self):
        return self.__number_of_doors

    def set_number_of_doors(self, number_of_doors):
        self.__number_of_doors = number_of_doors
