Class CheckParenthesis:
    def validParenthesis(s):
        stack = []
        brackets = { '(': ')',
                     "{": "}",
                     '[': ']' }

        for bracket in s:
            if bracket in brackets.keys(): stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False

                deleted = stack.pop()
                if brackets[deleted] != bracket:
                    return False

        if len(stack) != 0:
            return False

        return True

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
class UseFulOperations:
    def __init__(self):
        self.pi = 3.14
    def calculateArea(self, radius):
        return self.pi * radius ** 2

    def divide_numbers(a, b):
        return a / b
