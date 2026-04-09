# Practical 24: Class with function overloading (using default arguments)

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

    def area(self, shape, a, b=0):
        if shape == "rectangle":
            return a * b
        elif shape == "square":
            return a * a
        elif shape == "triangle":
            return 0.5 * a * b
        else:
            return "Unknown shape"

calc = Calculator()

print("=== Function Overloading Demo ===")
print(f"add(5)        = {calc.add(5)}")
print(f"add(5, 3)     = {calc.add(5, 3)}")
print(f"add(5, 3, 2)  = {calc.add(5, 3, 2)}")
print(f"Area of Square(4)         = {calc.area('square', 4)}")
print(f"Area of Rectangle(4, 5)   = {calc.area('rectangle', 4, 5)}")
print(f"Area of Triangle(6, 8)    = {calc.area('triangle', 6, 8)}")
