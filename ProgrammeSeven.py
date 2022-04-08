#Approach One: Using inbuilt-function
x = (input("Enter the base\n"))
y = (input("Enter the exponent\n"))
#verifying if the input values is numeric
if x.isdigit() and y.isdigit():
    #using pow to find the answer
    result = pow(int(x),int(y))
    print(result)
else:
    print("Invalid Input")

#Approach Two: Using operators/Using functions
def power_calculator(base,exponent):
    #Using ** operator
    answer = base ** exponent;
    return answer
print(power_calculator(7,5))

