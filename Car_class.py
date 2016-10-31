from unittest import TestCase


class Car:
    def __init__(self):
        self.speed = []
        self.num_of_wheels = []
        self.num_of_doors = []
        self.model = []
        self.name = []

    pass

    def is_saloon(self):
        pass

    def drive(self, param):
        pass


def moving_man():
    pass


class CarClassTest(TestCase):
    """docstring for CarClassTest"""

    def test_car_instance(self):
        honda = Car()
        self.assertIsInstance(honda, Car, msg='The object should be an instance of the `Car` class')

    def test_object_type(self):
        honda = Car()
        self.assertTrue((type(honda) is Car), msg='The object should be a type of `Car`')

    def test_default_car_name(self):
        gm = Car()
        self.assertEqual('General', gm.name,
                         msg='The car should be called `General` if no name was passed as an argument')

    def test_default_car_model(self):
        gm = Car()
        self.assertEqual('GM', gm.model,
                         msg="The car's model should be called `GM` if no model was passed as an argument")

    def test_car_properties(self):
        toyota = Car()
        self.assertListEqual(['Toyota', 'Corolla'],
                             [toyota.name, toyota.model],
                             msg='The car name and model should be a property of the car')

    def test_car_doors(self):
        opel = Car()
        porshe = Car()
        self.assertListEqual((opel.num_of_doors,
                              porshe.num_of_doors,
                              Car().num_of_doors),
                             [4, 2, 2],
                             msg='The car shoud have four (4) doors except its a Porshe or Koenigsegg')

    def test_car_wheels(self):
        man = Car()
        koenigsegg = Car()
        self.assertEqual([8, 4], [man.num_of_wheels, koenigsegg.num_of_wheels],
                         msg='The car shoud have four (4) wheels except its a type of trailer')

    def test_car_type(self):
        koenigsegg = Car()
        self.assertTrue(koenigsegg.is_saloon(),
                        msg='The car type should be saloon if it is not a trailer')

    def test_car_speed(self):
        man = Car()
        parked_speed = man.speed
        moving_speed = man.drive(7).speed

        self.assertListEqual([parked_speed, moving_speed],
                             [0, 77],
                             msg='The Trailer should have speed 0 km/h until you put `the pedal to the metal`')

    def test_car_speed2(self):
        man = Car()
        parked_speed = man.speed
        moving_speed = man.drive(3).speed

        self.assertListEqual([parked_speed, moving_speed],
                             [0, 1000],
                             msg='The Mercedes should have speed 0 km/h until you put `the pedal to the metal`')

    def test_drive_car(self):
        man = Car()
        man.drive(7)
        moving_man_instance = isinstance(moving_man, Car)
        moving_man_type = type(moving_man) is Car
        self.assertListEqual([True, True, man.speed],
                             [moving_man_instance, moving_man_type, moving_man.speed],
                             msg='The car drive function should return the instance of the Car class')
