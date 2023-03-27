# add your contents here
class PowerCalculator:
    def get_square(self, number):
        return number ** 2

    def get_cubes(self, numbers):
        cubes = []
        for number in numbers:
            cubes.append(number ** 3)
        return cubes

instance = PowerCalculator()
my_numbers = [1, 2, 3, 4, 5]
squares = []
for number in my_numbers:
    squares.append(instance.get_square(number))

cubes = instance.get_cubes(my_numbers)