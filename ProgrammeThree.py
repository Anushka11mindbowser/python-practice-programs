#Approach One

def next_num(n):
    return n + 1;

print(next_num(5))

#Approach Two

num = 17;
print("The next number is: " + str(num + 1))

#Approach Three
def next_number():
    a = int(input("Enter a number:\n"))
    number = a + 1
    statement = "The next number is: \n" + str(number);
    return statement

print(next_number())