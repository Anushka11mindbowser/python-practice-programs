def polygon_angle():
    n = int(input("Enter the number of sides: \n"))
    ans =  (n-2) * 180
    statement = "The sum of interior angles of a polygon is : " + str(ans) + "\n"
    return statement
print(polygon_angle())