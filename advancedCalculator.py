# advancedCalculator.py
# Author: Tinli Yarrington
# Date created: 3/21/15
# Dates edited: 3/23/15
# Purpose: to create a program that when user inputs certain function, program will calculate answer
# Notes:
#       - add more shapes to calculate areas and volumes (maybe even be able to solve using integrals)
#       - add more things that users can select to solve for (log, e, ln, exponents, differential equations)

import math

def selectChoice(choice):
    if choice == "a":
        solveArea()
    elif choice == "b":
        solveVolume()
    elif choice == "c":
        createLine()
    elif choice == "d":
        quadraticFormula()
    elif choice == "e":
        anglesInRight()
    else:
        print("That was not one of the choices.")
        print()
        main()

def solveArea():
    print("Which shape would you like to calculate?")
    print("{0:>5}".format("a) Circle"))
    print("{0:>5}".format("b) Triangle"))
    print("{0:>5}".format("c) Square"))
    print("{0:>5}".format("d) Rectangle"))
    print("{0:>5}".format("e) Trapezoid"))
    choice = input("(please type the letter associated with the chocie you would like)   ")
    print()

    getArea(choice)


def getArea(choice):
    if choice == "a":
        radius = eval(input("What is the radius of your circle?   "))
        area = math.pow(radius,2)*math.pi
        print("The area of your circle is:", area)
    elif choice == "b":
        base = eval(input("What is the base of your triangle?   "))
        height = eval(input("What is the height of your triangle?   "))
        area = (0.5)*base*height
        print("The area of your triangle is:", area)
    elif choice == "c":
        side = eval(input("What is the side of your square?   "))
        area = math.pow(side,2)
        print("The area of your square is:", area)
    elif choice == "d":
        length = eval(input("What is the length of your rectangle?   "))
        width = eval(input("What is the width of your rectangle?   "))
        area = length*width
        print("The area of your rectangle is:", area)
    elif choice == "e":
        base1 = eval(input("What is one of the bases of your trapezoid?   "))
        base2 = eval(input("What is the other base of your trapezoid?   "))
        height = eval(input("What is the height of your trapezoid?   "))
        area = (height/2)*(base1+base2)
        print("The area of your trapezoid is:", area)
    else:
        print("That was not one of the choices.")
        solveArea()

def solveVolume():
    print("Which shape would you like to calculate?")
    print("{0:>5}".format("a) Sphere"))
    print("{0:>5}".format("b) Triangular Prism"))
    print("{0:>5}".format("c) Cube"))
    print("{0:>5}".format("d) Rectangular Prism"))
    print("{0:>5}".format("e) Cone"))
    print("{0:>5}".format("f) Cylinder"))
    choice = input("(please type the letter associated with the chocie you would like)   ")

    getVolume(choice)

def getVolume(choice):
    if choice == "a":
        radius = eval(input("What is the radius of your sphere?   "))
        volume = math.pow(radius,3)*math.pi*(4./3.)
        print("The volume of your sphere is:", volume)
    elif choice == "b":
        base = eval(input("What is the base of your trianglar prism?   "))
        height = eval(input("What is the height of your trianglar prism?   "))
        length = eval(input("What is the length of your triangular prism?   "))
        volume = (0.5)*base*height*length
        print("The volume of your trianglar prism is:", volume)
    elif choice == "c":
        side = eval(input("What is the side of your cube?   "))
        volume = math.pow(side,3)
        print("The volume of your cube is:", volume)
    elif choice == "d":
        length = eval(input("What is the length of your rectanglar prism?   "))
        width = eval(input("What is the width of your rectanglar prism?   "))
        height = eval(input("What is the height of your rectangular prism?   "))
        volume = length*width*height
        print("The volume of your rectanglar prism is:", volume)
    elif choice == "e":
        radius = eval(input("What is the radius of your cone?   "))
        height = eval(input("What is the height of your cone?   "))
        volume = math.pow(radius,2)*math.pi*(height/3.)
        print("The volume of your sphere is:", volume)
    elif choice == "f":
        radius = eval(input("What is the radius of your cylinder?   "))
        height = eval(input("What is the height of your cylinder?   "))
        volume = math.pow(radius,2)*math.pi*height
        print("The volume of your cylinder is:", volume)
    else:
        print("That was not one of the choices.")
        solveVolume()

def createLine():
    xPoint1 = eval(input("What is the x-coordinate of one of the points?   "))
    yPoint1 = eval(input("What is the y-coordinate of one of the points?   "))
    xPoint2 = eval(input("What is the x-coordinate of the other point?   "))
    yPoint2 = eval(input("What is the y-coordinate of the other point?   "))

    slope = float(yPoint2 - yPoint1)/(xPoint2 - xPoint1)

    print("The slope of the line for these two points is: y -", yPoint1, "=", slope, "(x -", xPoint1, ")")

def quadraticFormula():
    print("Your equation is in the format: ax^2 + bx + c...")
    a = eval(input("What is the value of the a?   "))
    b = eval(input("What is the value of the b?   "))
    c = eval(input("What is the value of the c?   "))

    x1 = -b + math.sqrt(math.pow(b,2) - 4*a*c)/(2*a)
    x2 = -b - math.sqrt(math.pow(b,2) - 4*a*c)/(2*a)

    print("The solutions to this quadratic equation are:", x1, "and", x2)

def anglesInRight():
    side1 = eval(input("What is one of the sides of the right triangle?   "))
    side2 = eval(input("What is another side of the right triangle?   "))
    hypotenuse = eval(input("What is the length of the hypotenuse?   "))

    angle1 = math.degrees(math.asin(side1/hypotenuse))
    angle2 = math.degrees(math.asin(side2/hypotenuse))
    angle3 = 90
    sumAngles = angle1 + angle2 + angle3

    print("The angles in the triangle are:{0:6.2f},{1:6.2f},{2:3}".format(angle1, angle2, angle3))
    print("The sum of the angles is:", sumAngles)
    if sumAngles != 180:
        print("These sides do NOT form a right triangle.")
    else:
        print("These sides correctly form a right triangle.")
    
def main():
    bar = "+" + ("-"*48) + "+"
    print(bar)
    print("|{0:^48}|".format("CALCULATOR"))
    print(bar)
    print()
    print("What would you like to solve for?")
    print("{0:>5}".format("a) Area of a shape"))
    print("{0:>5}".format("b) Volume of a shape"))
    print("{0:>5}".format("c) Equation of a line"))
    print("{0:>5}".format("d) Solution to quadratic equation"))
    print("{0:>5}".format("e) Angles in a right triangle"))
    choice = input("(please type the letter associated with the choice you would like)   ")
    print()

    selectChoice(choice)
    print()

    option = ""
    while option != "YES" and option != "NO":
        print("Would you like to solve for something else?")
        option = input("(type yes or no as answers)   ").upper()
        if option == "YES":
            main()
        elif option == "NO":
            print("Hope your problem was solved!")

main()
