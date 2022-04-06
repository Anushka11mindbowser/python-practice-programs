def polygon_angle():
    try:
        n = int(input("Enter the number of sides: \n"))
        ans =  (n-2) * 180
        statement = "The sum of interior angles of a polygon is : " + str(ans) + "\n"
        return statement
    except:
        return "Invalid Input"
print(polygon_angle())