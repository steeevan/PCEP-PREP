import math
import sys
def intro():
    print("Project 2\nMulti Functional Calculator: Arithmetic Operations and Area Calculation.\nThe Multi Functional Calculator is a powerful tool designed to assist users in\nperforming arithmetic calculations and finding the areas of different geometric\nshapes. It combines the convenience of a standard calculator with the added\nfunctionality of shape-specific area calculations.")
    '''
    Name: intro

    Description: This is a function used to explain what the overall program does

    Input: N/A

    Output: This function will print out the paragraph explaining the program

    Variables:
    N/A
    '''
def add(num1=0,num2=0):
    '''
    Name: add

    Description: This is a function used to add two numbers, taken from the user

    Input: 2 numbers

    Output: This will print out the equation, followed by the answer

    Variables:
    num1 - the first number
    num2 - the second number
    equation - the tuple holding the two numbers which will be added together
    N/A
    '''
    equation = (num1, num2)
    print(num1,"+",num2,"=",sum(equation))
    main()
def subtract(num1=0,num2=0):
    '''
    Name: subtract

    Description: This is a function used to subtract two numbers, taken from the user

    Input: 2 numbers

    Output: This will print out the equation, followed by the answer

    Variables:
    num1 - the first number
    num2 - the second number
    difference - the result of the equation
    N/A
    '''
    difference = num1 - num2
    print(num1,"-",num2,"=",difference)
    main()
def multiply(num1=1,num2=1):
    '''
    Name: multiply

    Description: This is a function used to multiplt two numbers, taken from the user

    Input: 2 numbers

    Output: This will print out the equation, followed by the answer

    Variables:
    num1 - the first number
    num2 - the second number
    product - the result of the equation
    N/A
    '''
    product = num1*num2
    print(num1,"*",num2,"=",product)
    main()
    
def divide(num1=0,num2=1):
    '''
    Name: divide

    Description: This is a function used to divide two numbers, taken from the user

    Input: 2 numbers

    Output: This will print out the equation, followed by the answer

    Variables:
    num1 - the first number
    num2 - the second number
    quotient - the result of the equation 
    '''
    quotient = 0
    try:
        quotient = num1/num2
        print(num1,"/",num2,"=",quotient)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        main()
    
def rectArea(b=1,h=1):
    '''
    Name: rectArea

    Description: This is a function used to find the area of a rectangle

    Input: 2 values

    Output: This will print out the area of the rectangle, in a text-number format

    Variables:
    b - the base
    h - the height
    area - the result of the equation 
    '''
    area = b*h
    print("The area of the rectangle is",area)
    
def sqrArea(side=1):
    '''
    Name: sqrArea

    Description: This is a function used to find the area of a square

    Input: 1 value

    Output: This will print out the area of the square, in a text-number format

    Variables:
    side - the side length
    area - the result of the equation 
    '''
    area = side**2
    print("The area of the square is",area)

def circArea(r=1):
    '''
    Name: circArea

    Description: This is a function used to find the area of a circle

    Input: 1 value

    Output: This will print out the area of the circle, in a text-number format

    Variables:
    r - the side length
    area - the result of the equation 
    '''
    area = math.pi*r**2
    print("The area of the circle is",area)
    
def triArea(b=1,h=1):
    '''
    Name: triArea

    Description: This is a function used to find the area of a triangle

    Input: 1 value

    Output: This will print out the area of the triangle, in a text-number format

    Variables:
    b - the base
    h - the height
    area - the result of the equation 
    '''
    area = b*h/2
    print("The area of the triangle is",area)
    
def cubeVol(side=1):
    '''
    Name: cubeVol

    Description: This is a function used to find the volume of a cube

    Input: 1 value

    Output: This will print out the volume of the cube, in a text-number format

    Variables:
    side - the side length
    volume - the result of the equation 
    '''
    volume = side**3
    print("The volume of the cube is",volume)
    
def rectVol(b=1,h=1,l=1):
    '''
    Name: rectVol

    Description: This is a function used to find the volume of a rectangular prism

    Input: 3 values

    Output: This will print out the volume of the rectangular prism, in a text-number format

    Variables:
    side - the side length
    volume - the result of the equation 
    '''
    volume = b*h*l
    print("The volume of the prism is",volume)
    
def cylVol(r=1,h=1):
    '''
    Name: cylVol

    Description: This is a function used to find the volume of a cylinder

    Input: 2 values

    Output: This will print out the volume of the cylinder, in a text-number format

    Variables:
    r - the radius
    h - the height
    volume - the result of the equation 
    '''
    volume = math.pi*r**2*h
    print("The volume of the cylinder is",volume)
    
def sphereVol(r):
    '''
    Name: cylVol

    Description: This is a function used to find the volume of a sphere

    Input: 1 value

    Output: This will print out the volume of the sphere, in a text-number format

    Variables:
    r - the radius
    volume - the result of the equation 
    '''
    volume = 4/3*math.pi*r**3
    print("The volume of the sphere is",volume)




    
#------------------------------------------------------------------------------------------------------------------
    
    
action_list = ["Arithmetic Operation","Area of Shapes","Volume of 3D Shapes","Exit"]
op_list = ["Add","Subtract","Multiply","Divide","Go back"]
area_list = ["Rectangle","Square","Circle","Triangle","Go back"]
vol_list = ["Rectangular prism","Cube","Cylinder","Sphere","Go back"]


#------------------------------------------------------------------------------------------------------------------





def operation():
    '''
    Name: operation

    Description: This is a function used to follow up main if the operation set is chosen

    Input: 1 number, the user's choice

    Output: This will provide a more specific menu, one with the target operation

    Variables:
    counter2 - not very important but used to print a list
    chosen_operation - the, well, chosen operation
    '''
    counter2 = 1
    for i in op_list:
        print(counter2,".",i)
        counter2 += 1
    while True:    
        try:
            chosen_operation = int(input("Select an operation(number): "))
            break
        except:
            print("What were you trying to accomplish...?")
            main()
    if chosen_operation == 1:
        while True:
            try:
                add(int(input("Enter the first number: ")),int(input("Enter the second number: ")))
                break
            except:
                print("Invalid number!")
                main()
    elif chosen_operation == 2:
        while True:
            try:
                subtract(int(input("Enter the first number: ")),int(input("Enter the second number: ")))
                break
            except:
                print("Invalid number!")
                main()
    elif chosen_operation == 3:
        while True:
            try:
                multiply(int(input("Enter the first number: ")),int(input("Enter the second number: ")))
                break
            except:
                print("Invalid number!")
                main()
    elif chosen_operation == 4:
        while True:
            try:
                divide(int(input("Enter the first number: ")),int(input("Enter the second number: ")))
                break
            except:
                print("Invalid number!")
                main()
    elif chosen_operation == 5:
        main()
    else:
        print("Not a valid option!")
        main()

def area():
    '''
    Name: area

    Description: This is a function used to follow up main if the area set is chosen

    Input: 1 number, the user's choice

    Output: This will provide a more specific menu, one with the target shape/operation

    Variables:
    counter3 - not very important but used to print a list
    chosen_operation2 - the, well, chosen operation/shape
    '''
    counter3 = 1
    for i in area_list:
        print(counter3,".",i)
        counter3 +=1
    while True:
        try:
            chosen_operation2 = int(input("Select an shape(number): "))
            break
        except:
            print("What were you trying to accomplish...?")
            main()
    if chosen_operation2 == 1:
        while True:
            try:
                rectArea(int(input("Enter the base: ")),int(input("Enter the height: ")))
                break
            except:
                print("Invalid number!")
                main()
    elif chosen_operation2 == 2:
        while True:
            try:
                square(int(input("Enter a side length: ")))
                break
            except:
                print("Invalid number!")
                main()
    elif chosen_operation2 == 3:
        while True:
            try:
                circArea(int(input("Enter the radius: ")))
                break
            except:
                print("Invalid number!")
                main()
    elif chosen_operation2 == 4:
        while True:
            try:
                triArea(int(input("Enter the base: ")),int(input("Enter the height: ")))
                break
            except:
                print("Invalid number!")
                main()
    elif chosen_operation2 == 5:
        main()
    else:
        print("Not a valid option!")
        main()

def volume():
    '''
    Name: volume

    Description: This is a function used to follow up main if the volume set is chosen

    Input: 1 number, the user's choice

    Output: This will provide a more specific menu, one with the target shape/operation

    Variables:
    counter - not very important but used to print a list
    chosen_operation3 - the, well, chosen operation/shape
    '''
    counter4 = 1
    for i in vol_list:
        print(counter4,".",i)
        counter4 +=1
    while True:
        try:
            chosen_operation3 = int(input("Select an shape(number): "))
            break
        except:
            print("What were you trying to accomplish...?")
            main()
    if chosen_operation3 == 1:
        while True:
            try:
                rectVol(int(input("Enter the base: ")),int(input("Enter the height: ")),int(input("Enter the length")))
            except:
                print("Invalid number!")
                main()
    elif chosen_operation3 == 2:
        while True:
            try:
                cubeVol(int(input("Enter a side length: ")))
            except:
                print("Invalid number!")
                main()
    elif chosen_operation3 == 3:
        while True:
            try:
                cylVol(int(input("Enter the radius: ")),int(input("Enter the height: ")))
            except:
                print("Invalid number!")
                main()
    elif chosen_operation3 == 4:
        while True:
            try:
                sphereVol(int(input("Enter the radius: ")))
            except:
                print("Invalid number!")
                main()
    elif chosen_operation3 == 5:
        main()
    else:
        print("Not a valid option!")
        main()

def main():
    '''
    Name: main

    Description: This is a function used to get the action group from the user; those groups being defined above

    Input: 1 number, the user's choice

    Output: This will provide a more specific menu, one with the target operations

    Variables:
    counter - not very important but used to print a list
    chosen_group - the, well, chosen group
    '''
    counter = 1
    print("What would you like to do? ")
    for i in action_list:
        print(counter,".",i)
        counter += 1
    while True:
        try:
            chosen_group = int(input("Select an action: "))
            break
        except:
            print("What were you trying to accomplish...?")
            main()
    if chosen_group == 1:
        operation()
    elif chosen_group == 2:
        area()
    elif chosen_group == 3:
        volume()
    elif chosen_group == 4:
        sys.exit
    else:
        print("Invalid action!")
        main()
main()
