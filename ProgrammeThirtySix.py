#Approach One:

def divide_five_by_zero():
    try:
        print(5 / 5)
    except ArithmeticError:
        print("Cannot divide a number by zero")
    finally:
        print("Exception executed")
    return "Finished Execution"

print(divide_five_by_zero())