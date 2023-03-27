class CheckParenthesis:
    # define a function to check valid parentesis
    def validParenthesis(s):
        stack = []
        brackets = { '(': ')',
                     "{": "}",
                     '[': ']' }

        for bracket in s:
            # keys are open brackets
            if bracket in brackets.keys(): 
                stack.append(bracket)
            else:
                # close bracket is coming wihout openning bracket 
                # we will return
                if len(stack) == 0:
                    return False
                # remove the openning
                deleted = stack.pop()
                # if they are not matched we will return False
                if brackets[deleted] != bracket:
                    return False
        # to be valid it should match
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

    def divide_numbers(self, a, b):
        # remove division by zero.
        assert b != 0
        return a / b

operations = UseFulOperations()
print(operations.divide_numbers(4,2))