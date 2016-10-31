class Car(object):
    num_of_wheels = 4
    speed = 0
    num_of_doors = 4

    def __init__(self, name="General", model="GM", car_type=None):
        self.name = name
        self.model = model
        self.car_type = car_type

        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.car_type == "trailer":
            self.num_of_wheels = 8

    def drive(self):
        if self.speed == 3:
            self.speed = 1000
            return self
        elif self.speed == 7:
            self.speed = 77
            return self

    def is_saloon(self):
        return self.car_type != "trailer"
