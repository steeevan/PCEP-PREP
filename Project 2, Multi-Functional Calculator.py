# Project 2 | Multi-Functional Calculator
# Matt Shen
# 6 / 27 / 23

import sys
import math


def intro():
    '''
    ---------------------------------------------------------
    Name: intro

    Desc: prints the intro of project

    Input(Parameter):

    Output:

    LocalVariables:
    ---------------------------------------------------------
    '''
    
    print("""Project 2
Multi-Functional Calculator: Arithmetic Operations and Area Calculation.
The Multi-Functinal Calculator is a powerful tool designed to assist
users in performing arithmetic calculations and finding the areas of
different geometric shapes. It combines the convenience of a standard
calculator with the added functionality of shape-specific area
calculations.
""")



def add():
    '''
    ---------------------------------------------------------
    Name: add

    Desc: asks the user to input the numbers needed to add and
          stores them in a list Then adds all the numbers in
          the list and displays the result as well as the adding
          Can catch if any errors occurr

    Input(Parameter):

    Output:

    LocalVariables:
        + addSum: result of the added numbers in addNums
        + addNums: stores the numbers that will be added
        + addNumber: the determination of wether to add the
                     numbers in the list now or not
    ---------------------------------------------------------
    '''
    
    addSum = 0
    addNums = []
    addNumber=''
    
    try:
        # keeps asking for number
        while addNumber != 0:
            print(f"Numbers: \n{addNums}")
            print("Enter zero to add the numbers.")
            addNumber = int(input("\nEnter a number to add: "))
            addNums.append(addNumber)

        # adds
        for i in range(0, len(addNums)):
            addSum += addNums[i]

            # prints display
            if i == len(addNums)-1:
                print(f"+_________\n  {addSum}")
            else:
                print(f"  {addNums[i]}")
        

    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")


        
def subtract():
    '''
    ---------------------------------------------------------
    Name: subtract

    Desc: asks the user for two numbers to subtract and prints
          the result Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + num1: the first number to be inputted and used
        + num2: the second number to be inputted and used
        + difference: finds the difference of num1 and num2
    ---------------------------------------------------------
    '''
    
    try:
        num1 = int(input("Enter a number to subtract from: "))
        num2 = int(input("Enter a number to subtract by: "))
        difference = num1 - num2
        print(f"{num1} - {num2} = {difference}")
        
    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")


    
def divide():
    '''
    ---------------------------------------------------------
    Name: divide

    Desc: asks the user for two numbers to divide and prints
          the result Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + numerator: the number to be divided by denominator
        + denominator: the number to divide the numerator by
        + quotient: the result of numerator / denominator
    ---------------------------------------------------------
    '''
    
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        quotient = numerator / denominator
        print(f"{numerator} / {denominator} = {quotient}")
        
    except ValueError:
        print("Enter a number next time!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except:
        print("An Error has occurred.")


        
def multiply():
    '''
    ---------------------------------------------------------
    Name: multiply

    Desc: asks the user for two numbers to multiply and prints
          the result Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + num1: the first number to be inputted and used
        + num2: the second number to be inputted and used
        + product: finds the product of num1 and num2
    ---------------------------------------------------------
    '''
    
    try:
        num1 = int(input("Enter a number to multiply: "))
        num2 = int(input("Enter another number to multiply: "))
        product = num1 * num2
        print(f"{num1} * {num2} = {product}")
        
    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")



def rectArea():
    '''
    ---------------------------------------------------------
    Name: rectArea

    Desc: asks the user for two numbers to multiply for area
          and prints the result Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + base: the base of a shape inputted by the user
        + height: the height of a shape inputted by the user
        + area: finds the area of the rectangle by multiplication
                with the base and height
    ---------------------------------------------------------
    '''
    
    try:
        base = int(input("Enter the base: "))
        height = int(input("Enter the height: "))
        area = base * height
        print(f"{base} * {height} = {area}")
        
    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")


        
def sqrArea():
    '''
    ---------------------------------------------------------
    Name: sqrArea

    Desc: asks the user for one number to multiply for area
          and prints the result Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + base: the base of a shape inputted by the user
        + area: finds the area of the square by multiplication
                with the base
    ---------------------------------------------------------
    '''
    
    try:
        base = int(input("Enter the base of a side: "))
        area = base ** 2
        print(f"{base}^2 = {area}")
        
    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")


        
def circArea():
    '''
    ---------------------------------------------------------
    Name: circArea

    Desc: asks the user for the radius to multiply for area
          and prints the result Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + radius: the radius inputted by the user
        + area: finds the area of the circle by multiplication
                with radius
    ---------------------------------------------------------
    '''
    
    try:
        radius = int(input("Enter the radius: "))
        area = (radius ** 2) * math.pi
        print(f"{radius}^2 * {math.pi} = {area}")
        
    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")


        
def triArea():
    '''
    ---------------------------------------------------------
    Name: triArea

    Desc: asks the user for two numbers to multiply for area
          and prints the result Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + base: the base of a shape inputted by the user
        + height: the height of a shape inputted by the user
        + area: finds the area of the triangle by multiplication
                and division with base and height
    ---------------------------------------------------------
    '''
    
    try:
        base = int(input("Enter the base: "))
        height = int(input("Enter the height: "))
        area = (base * height) / 2
        print(f"{base} * {height} / 2 = {area}")
        
    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")


        
def cubeVol():
    '''
    ---------------------------------------------------------
    Name: cubeVol

    Desc: asks the user for the base to multiply for volume
          and prints the result Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + base: the base of a shape inputted by the user
        + vol: finds the volume of the cube by multiplication
               with base
    ---------------------------------------------------------
    '''
    
    try:
        base = int(input("Enter the base of a side: "))
        volume = base ** 3
        print(f"{base}^3 = {volume}")
        
    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")


        
def rectPrismVol():
    '''
    ---------------------------------------------------------
    Name: rectPrismVol

    Desc: asks the user for the length, width, and height to
          multiply for volume and prints the result
          Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + length: the length of a shape inputted by the user
        + width: the width of a shape inputted by the user
        + height: the height of a shape inputted by the user
        + vol: finds the volume of the rectangular prism by
               multiplication with length, width, and height
    ---------------------------------------------------------
    '''
    
    try:
        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))
        height = int(input("Enter the height: "))
        volume = length * width * height
        print(f"{length} * {width} * {height} = {volume}")
        
    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")


        
def cyliVol():
    '''
    ---------------------------------------------------------
    Name: cyliVol

    Desc: asks the user for the radius and height to
          multiply for volume and prints the result
          Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + radius: the radius of the circle inputted by the user
        + height: the height of the cylinder inputted by the user
        + vol: finds the volume of the cylinder by multiplication
               with radius and height
    ---------------------------------------------------------
    '''
    
    try:
        radius = int(input("Enter the radius: "))
        height = int(input("Enter the height: "))
        volume = math.pi * (radius ** 2) * height 
        print(f"{radius}^2 * {math.pi} * {height} = {volume}")
        
    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")


        
def sphereVol():
    '''
    ---------------------------------------------------------
    Name: sphereVol

    Desc: asks the user for the radius to
          multiply for volume and prints the result
          Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + radius: the radius the circle shape inputted by the user
        + vol: finds the volume of the sphere by multiplication
               with radius and pi
    ---------------------------------------------------------
    '''
    
    try:
        radius = int(input("Enter the radius: "))
        volume = (4/3) * math.pi * (radius ** 3) 
        print(f"4/3 * {math.pi} * {radius}^3 = {volume}")
        
    except ValueError:
        print("Enter a number next time!")
    except:
        print("An Error has occurred.")


        
#######################################################################


def mainMenu():
    '''
    ---------------------------------------------------------
    Name: mainMenu

    Desc: asks the user for an input on what catagory of
          math to do and what equation to perform
          and uses the helper functions for performing
          equations
          Can exit or go back if the uesr enters 0
          Can catch errors

    Input(Parameter):

    Output:

    LocalVariables:
        + exitOption: the determination of wether to quit the
                      program or not
        + operationCatagory: the user's input of what catagory
                             of math to do
        + operationEquation: the user's input of what type of equation
                             to perform
        + backOption: checks if the user's command is to go back and
                             goes back
    ---------------------------------------------------------
    '''
    
    exitOption = False
    
    while exitOption != True: # break if command is go back
        print("""
Select Option:
1. Arithmetic Operations
2. Area of Shapes
3. Volumes of 3D Shapes
0. Exit
""")
        
        try:
            # command
            operationCatagory = int(input("> "))
       

            # Quit
            if operationCatagory == 0:
                print("You have exited.")
                exitOption = True



            ############ Arithmetic Options ############
            if operationCatagory == 1:
                backOption = False

                while backOption == False:
                    print("""
Select Option:
1. Addition
2. Subtraction
3. Multiplication
4. Division
0. Go Back
""")

                    # command
                    operationEquation = int(input("\n> "))


                    # Arithmetic Options Results
                    if operationEquation == 0:
                        backOption = True
                    elif operationEquation == 1: # add
                        add()
                    elif operationEquation == 2: # subtract
                        subtract()
                    elif operationEquation == 3: # multiply
                        multiply()
                    elif operationEquation == 4: # divide
                        divide()



            ############ Area of Shape Options ############
            elif operationCatagory == 2:
                backOption = False

                while backOption == False:
                    print("""
Select Option:
1. A of Rectangle
2. A of Square
3. A of Circle
4. A of Triangle
0. Go Back
""")
                    # command
                    operationEquation = int(input("\n> "))

                    # Area of Shapes Results
                    if operationEquation == 0:
                        backOption = True
                    elif operationEquation == 1: # rectangle
                        rectArea()
                    elif operationEquation == 2: # square
                        sqrArea()
                    elif operationEquation == 3: # circle
                        circArea()
                    elif operationEquation == 4: # triangle
                        triArea()



            ############ Volumes of Shapes ############
            elif operationCatagory == 3:
                backOption = False

                while backOption == False:
                    print("""
Select Option:
1. V of Rectangular Prism
2. V of Cube
3. V of Cylinder
4. V of Sphere
0. Go Back
""")
                    # command
                    operationEquation = int(input("\n> "))

                    # Area of Shapes Results
                    if operationEquation == 0:
                        backOption = True
                    elif operationEquation == 1: # rectangular prism
                        rectPrismVol()
                    elif operationEquation == 2: # cube
                        cubeVol()
                    elif operationEquation == 3: # cylinder
                        cyliVol()
                    elif operationEquation == 4: # sphere
                        sphereVol()



        # checks if user entered invalid input
        except ValueError:
            print("Enter a number choice!")
        except:
            print("An Error has occurred.")


############################################################

  

mainMenu()

exit()








