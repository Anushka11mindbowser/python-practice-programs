#Approach One: Using inbuilt-function
x = int(input("Enter the base\n"))
y = int(input("Enter the exponent\n"))
result =  pow(x,y)
print(result)

#Approach Two: Using operators/Using functions
def power_calculator(base,exponent):
    answer = base ** exponent;
    return answer
print(power_calculator(7,5))

