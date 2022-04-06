#Approach One
class Demo:
    def __init__(self):
        self.strng = input("Enter a String\n")

    def getString(self):
         return self.strng

    def printString(self):
        if self.strng.isdigit():
            return "You entered a numeric value"
        else:
            updated_string = self.strng.upper()
            return updated_string





example = Demo()
print(example.getString())
print(example.printString())



