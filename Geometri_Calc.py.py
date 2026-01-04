''' Program that calculates the area of one of the following shapes
1. Square
2. Rectangle
3. Triangle
4. Circle '''

import math 
print("Select a shape to calculate area:")
print("1. Square\n" \
"2. Rectangle\n" \
"3. Triangle\n" \
"4. Circle")

# You must get the 'option' from the user first
option = int(input("Enter option (1-4): "))


if option==1:
    side = float(input("Enter side: "))
    Square = side**2
    print("Area of square is" + str(Square))
elif option == 2:
    length= float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    Rectangle = length * width
    print("Area of rectangle is" + str(Rectangle))
elif option == 3:
    height= float(input("Enter height: "))
    base = float(input("Enter base: "))
    Triangle = (height * base)/2
    print("Area of triangle is" + str(Triangle))
elif option == 4:
    radius= float(input("Enter Radius: "))
    pi=3.14
    Circle = pi * (radius**2)
    print("Area of circle is" + str(Circle))
