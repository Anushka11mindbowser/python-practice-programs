#Approach One: using class functions
class Calculator:
    def __init__(self):

        self.a = int(input("Enter the first number\n"))
        self.b = int(input("Enter the second number\n"))

    def add(self):
        try:
            return self.a + self.b
        except:
            return "Invalid"

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

example1 = Calculator()
print(example1.add())
print(example1.subtract())
print(example1.multiply())
print(example1.divide())


#Approach Two: Using if-else loop
def calc():
    a = int(input("Enter the first number\n"))
    b = int(input("Enter the second number\n"))
    print("Press 1 for addition\n")
    print("Press 2 for subtraction\n")
    print("Press 3 for multiplication\n")
    print("Press 4 for division\n")
    df = int(input("Enter your choice\n"))
    if df == 1:
        return a + b
    elif df == 2:
        return a - b
    elif df == 3:
        return a * b
    elif df == 4:
        return a / b
    else:
        return "Invalid Input"

print(calc())

