import math
import sys
def main():
    '''
    --------------------------------------------------------------------------------------------------
    Name:main
    Description:
    This function is the entire program and has everything needed for the program to run.
    No Input
    Ouptput: This function outputs the entire user interface.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    intro()
    while True:
        mainMenu()
        mainMenu2()
        print(" ")
def intro():
    '''
    --------------------------------------------------------------------------------------------------
    Name:intro
    Description:
    This function is the intro.
    No Input
    Ouptput: This function outputs the intro.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print("Project 2")
    print("Multi-Functional Calculator: Arithmetic Operations and Area Caluculation.")
    print("The Multi-Functional Calculator is a powerful tool designed to assist users in performing arithmetic calculations and finding the areas of different geometric shapes. It combines the convenience of a standard calculator with the added functionality of shape-specific area calculations.")
def add(num1 = 0,num2 = 0):
    '''
    --------------------------------------------------------------------------------------------------
    Name:add
    Description:
    This function is the function that calculates addition.
    Inputs: num1 and num2, both of which have a default value of 0. 
    No Output
    Local Variables: total, a variable that holds the sum of num1 and num2.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = num1 + num2
    return total
def subtract(num1 = 0, num2 = 0):
    '''
    --------------------------------------------------------------------------------------------------
    Name:subtract
    Description:
    This function is the function that calculates subtraction.
    Inputs: num1 and num2, both of which have a default value of 0. 
    No Output
    Local Variables: total, a variable that holds the difference of num1 and num2.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = num1 - num2
    return total
def multiply(num1 = 1, num2 = 1):
    '''
    --------------------------------------------------------------------------------------------------
    Name:multiply
    Description:
    This function is the function that calculates multiplication.
    Inputs: num1 and num2, both of which have a default value of 1. 
    No Output
    Local Variables: total, a variable that holds the product of num1 and num2.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = num1 * num2
    return total
def divide(num1 = 1, num2 = 1):
    '''
    --------------------------------------------------------------------------------------------------
    Name:divide
    Description:
    This function is the function that calculates division.
    Inputs: num1 and num2, both of which have a default value of 1. 
    No Output
    Local Variables: total, a variable that holds the quotient of num1 and num2.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = num1/num2
    return total
def rectArea(base = 1, height = 1):
    '''
    --------------------------------------------------------------------------------------------------
    Name:rectArea
    Description:
    This function is the function that calculates a rectangle's area.
    Inputs: base and height, both of which have a default value of 1. 
    No Output
    Local Variables: total, a variable that holds the rectangle's area.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = base * height
    return total
def sqrArea(base = 1):
    '''
    --------------------------------------------------------------------------------------------------
    Name:sqrArea
    Description:
    This function is the function that calculates a square's area.
    Inputs: base, which is at a default value of 1
    No Output
    Local Variables: total, a variable that holds the square's area.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = base * base
    return total
def circArea(radius = 1):
    '''
    --------------------------------------------------------------------------------------------------
    Name:circArea
    Description:
    This function is the function that calculates a circle's area.
    Inputs: radius, which is at a default value of 1
    No Output
    Local Variables: total, a variable that holds the circle's area.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = math.pi * (radius* radius)
    return total
def triArea(base = 1, height = 1):
    '''
    --------------------------------------------------------------------------------------------------
    Name:triArea
    Description:
    This function is the function that calculates a triangle's area.
    Inputs: base and height, which both have a default value of 1.
    No Output
    Local Variables: total, a variable that holds the triangle's area.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = (base * height)/2
    return total
def cubeVol(side = 1):
    '''
    --------------------------------------------------------------------------------------------------
    Name:cubeVol
    Description:
    This function is the function that calculates a cube's volume.
    Inputs: side, which is at a default value of 1.
    No Output
    Local Variables: total, a variable that holds the cube's volume.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = side * side *side
    return total
def rectVol(length = 1, width = 1, height = 1):
    '''
    --------------------------------------------------------------------------------------------------
    Name:rectVol
    Description:
    This function is the function that calculates a rectangle's volume.
    Inputs: length, width, and height, all of which are at a default value of 1.
    No Output
    Local Variables: total, a variable that holds the rectangle's volume.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = length * width * height
    return total
def cyliVol(radius = 1, height = 1):
    '''
    --------------------------------------------------------------------------------------------------
    Name:cyliVol
    Description:
    This function is the function that calculates a cylinder's volume.
    Inputs: radius and height, both of which are at a default value of 1
    No Output
    Local Variables: total, a variable that holds the cylinder's volume.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = math.pi * radius*radius * height
    return total
def sphereVol(radius = 1):
    '''
    --------------------------------------------------------------------------------------------------
    Name:sphereVol
    Description:
    This function is the function that calculates a sphere's volume.
    Inputs: radius, which is at a default value of 1
    No Output
    Local Variables: total, a variable that holds the sphere's volume.
    --------------------------------------------------------------------------------------------------
    '''
    global total
    total = 4/3 * math.pi * radius*radius
    return total
def addEquation(a,b,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:addEquation
    Description:
    This function is the function that prints an equation for the add function.
    Inputs: a,b, and ans, all of which are used print out the right equation.
    Output: This function outputs the equation for the add function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print(a, " + ", b, " = ", ans)
def subEquation(a,b,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:subEquation
    Description:
    This function is the function that prints an equation for the subtract function.
    Inputs: a,b, and ans, all of which are used print out the right equation.
    Output: This function outputs the equation for the sub function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print(a, " - ", b, " = ", ans)
def mulEquation(a,b,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:mulEquation
    Description:
    This function is the function that prints an equation for the multiply function.
    Inputs: a,b, and ans, all of which are used print out the right equation.
    Output: This function outputs the equation for the multiply function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print(a, " * ", b, " = ", ans)
def divEquation(a,b,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:divEquation
    Description:
    This function is the function that prints an equation for the divide function.
    Inputs: a,b, and ans, all of which are used print out the right equation.
    Output: This function outputs the equation for the divide function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print(a, " / ", b, " = ", ans)
def rectEquation(a,b,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:rectEquation
    Description:
    This function is the function that prints an equation for the rectArea function.
    Inputs: a,b, and ans, all of which are used print out the right equation.
    Output: This function outputs the equation for the rectArea function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print("Area of Rectangle: ", a, " * ", b, " = ", ans)
def sqrEquation(a,b,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:sqrEquation
    Description:
    This function is the function that prints an equation for the sqrArea function.
    Inputs: a,b, and ans, all of which are used print out the right equation.
    Output: This function outputs the equation for the sqrArea function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print("Area of Square: ", a, " * ", b, " = ", ans)
def circEquation(radius,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:circEquation
    Description:
    This function is the function that prints an equation for the circArea function.
    Inputs: radius and ans, both of which are used print out the right equation.
    Output: This function outputs the equation for the circArea function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print("Area of Circle: 3.141592653589793", " * ", radius, "^2 = ", ans)
def triEquation(a,b,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:triEquation
    Description:
    This function is the function that prints an equation for the triArea function.
    Inputs: a,b, and ans, all of which are used print out the right equation.
    Output: This function outputs the equation for the triArea function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print("Area of Triangle: (", a, " * ", b, ")/2 = ", ans)
def cubeVolEquation(a, ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:cubeVolEquation
    Description:
    This function is the function that prints an equation for the cubeVol function.
    Inputs: a and ans, both of which are used print out the right equation.
    Output: This function outputs the equation for the cubeVol function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print("Area of Cube: ", a, " * ", a, " * ", a, " = ", ans)
def rectVolEquation(a,b,c,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:rectVolEquation
    Description:
    This function is the function that prints an equation for the rectVol function.
    Inputs: a,b,c, and ans, all of which are used print out the right equation.
    Output: This function outputs the equation for the rectVol function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print("Area of Rectangular Prism: ", a, " * ", b, " * ", c, " = ", ans)
def cyliVolEquation(radius,b,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:cyliVolEquation
    Description:
    This function is the function that prints an equation for the cyliVol function.
    Inputs: radius,b, and ans, all of which are used print out the right equation.
    Output: This function outputs the equation for the cyliVol function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print("Area of Cylinder: 3.141592653589793", radius, "^2 * ", b, " = ", ans)
def spheVolEquation(radius,ans):
    '''
    --------------------------------------------------------------------------------------------------
    Name:spheVolEquation
    Description:
    This function is the function that prints an equation  for the sphereVol function.
    Inputs: radius and ans, both of which are used print out the right equation.
    Output: This function outputs the equation for the sphereVol function.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    print("Area of Sphere: (4/3) * 3.141592653589793 * ", radius, "^2 = ", ans)

def mainMenu():
    '''
    --------------------------------------------------------------------------------------------------
    Name:mainMenu
    Description:
    This function prints the first menu that stems out into other menus. It aslo makes sure that the user doesn't enter a letter when selecting an answer.
    No Input
    Output: This function outputs the first menu a user will need.
    Local Variables: option is used to get the user's input and optionNum is what is changed into an integer and checked for errors.
    --------------------------------------------------------------------------------------------------
    '''
    print("1. Arithmetic Operation")
    print("2. Area of Shapes")
    print("3. Volumes of 3D Shapes")
    print("0. Exit")
    print(" ")
    option = input("Select an option:")
    try:
        global optionNum
        optionNum = int(option)
    except ValueError:
        print("Please use a number to select your option. Please try again")
        mainMenu()

def mainMenu2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:mainMenu2
    Description:
    This function is the function that prints the next menus based on the previous selection. 
    No Input
    Output: This function outputs the next menu needed and starts the next functions that take the selection from the user.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    if optionNum == 1:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("0. Go back")
        print(" ")
        arithMenuop()
        arithMenu()
    elif optionNum == 2:
        print("1. Area of rectangle")
        print("2. Area of square")
        print("3. Area of circle")
        print("4. Area of triangle")
        print("0. Go back")
        print(" ")
        areaMenuop()
        areaMenu()
    elif optionNum == 3:
        print("1. Volume of rectangular prism")
        print("2. Volume of cube")
        print("3. Volume of cylinder")
        print("4. Volume of sphere")
        print("0. Go back")
        print(" ")
        volMenuop()
        volMenu()
    elif optionNum == 0:
        sys.exit()
    else:
        print("Please select an option based on a number. Please do not enter numbers greater than 3.")
        mainMenu()

def arithMenuop():
    '''
    --------------------------------------------------------------------------------------------------
    Name:arithMenuop
    Description:
    This function is the first part of the arithemtic menu selection.
    No Input
    Output: This function outputs the instructions to select the next action and if you need to try again.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global option2Num
    option2 = input("Select an option:")
    try:
        global option2Num
        option2Num = int(option2)
    except ValueError:
        print("Please use a number to select your option. Please try again")
        arithMenuop()
def arithMenu():
    '''
    --------------------------------------------------------------------------------------------------
    Name:arithMenu
    Description:
    This function is the next part of the arithmetic menu and chooses what functions to use next and uses them.
    No Input
    Output: This function outputs if you selected wrong.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    if option2Num == 1:
        addp2()
        addp3()
        addPrint()
    elif option2Num == 2:
        subp2()
        subp3()
        subPrint()
    elif option2Num == 3:
        mulp2()
        mulp3()
        mulPrint()
    elif option2Num == 4:
        divp2()
        divp3()
        divPrint()
    elif option2Num == 0:
        mainMenu()
        mainMenu2()
    else:
        print("Please select an option based on a number. Please do not enter numbers greater than 4.")
        mainMenu()
def areaMenuop():
    '''
    --------------------------------------------------------------------------------------------------
    Name:areaMenuop
    Description:
    This function is the first part of the area menu selection.
    No Input
    Output: This function outputs the instructions to select the next action and if you need to try again.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global option2Num
    option2 = input("Select an option:")
    try:
        global option2Num
        option2Num = int(option2)
    except ValueError:
        print("Please use a number to select your option. Please try again")
        arithMenuop()
def areaMenu():
    '''
    --------------------------------------------------------------------------------------------------
    Name:areaMenu
    Description:
    This function is the next part of the area menu and chooses what functions to use next and uses them.
    No Input
    Output: This function outputs if you did the selection wrong.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    if option2Num == 1:
        recp2()
        recp3()
        recPrint()
    elif option2Num == 2:
        sqrp2()
        sqrPrint()
    elif option2Num == 3:
        circp2()
        circPrint()
    elif option2Num == 4:
        trip2()
        trip3()
        triPrint()
    elif optionNum == 0:
        mainMenu()
        mainMenu2()
    else:
        print("Please select an option based on a number. Please do not enter numbers greater than 4.")
        mainMenu()
def volMenuop():
    '''
    --------------------------------------------------------------------------------------------------
    Name:volMenuop
    Description:
    This function is the first part of the volume menu selection.
    No Input
    Output: This function outputs the instructions to select the next action and if you need to try again.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global option2Num
    option2 = input("Select an option:")
    try:
        global option2Num
        option2Num = int(option2)
    except ValueError:
        print("Please use a number to select your option. Please try again")
        volMenuop()
def volMenu():
    '''
    --------------------------------------------------------------------------------------------------
    Name:volMenu
    Description:
    This function is the next part of the volume menu and chooses what functions to use next and uses them.
    No Input
    Output: This function outputs if you did the selection wrong.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    if option2Num == 1:
        recVp2()
        recVp3()
        recVp4()
        recVPrint()
    elif option2Num == 2:
        cubeVp2()
        cubeVPrint()
    elif option2Num == 3:
        cyliVp2()
        cyliVp3()
        cyliVPrint()
    elif option2Num == 4:
        spheVp2()
        spheVPrint()
    elif optionNum == 0:
        mainMenu()
        mainMenu2()
    else:
        print("Please select an option based on a number. Please do not enter numbers greater than 4.")
        mainMenu()
def addp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:addp2
    Description:
    This function is the what takes in the first number for the addition sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    if option2Num == 1:
        global numAdd
        num = input("Please enter a number")
        try:
            numAdd = int(num)
        except ValueError:
            print("Please use a number to select your numbers. Please try again")
            addp2()
def addp3():
    '''
    --------------------------------------------------------------------------------------------------
    Name:addp2
    Description:
    This function is the what takes in the second number for the addition sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global num2Add
    num2 = input("Please enter a number")
    try:
        num2Add = int(num2)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        addp3()
    
def addPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:addPrint
    Description:
    This function is the what takes the inputs from the previous functions and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever addition question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    add(numAdd,num2Add)
    addEquation(numAdd,num2Add,total)
#----------------------------
def subp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:subp2
    Description:
    This function is the what takes in the first number for the subtraction sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numSub
    num = input("Please enter a number")
    try:
        numSub = int(num)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        subp2()
def subp3():
    '''
    --------------------------------------------------------------------------------------------------
    Name:subp3
    Description:
    This function is the what takes in the second number for the subtraction sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global num2Sub
    num2 = input("Please enter a number")
    try:
        num2Sub = int(num2)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        subp3()
    
def subPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:subPrint
    Description:
    This function is the what takes the inputs from the previous functions and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever subtraction question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    subtract(numSub,num2Sub)
    subEquation(numSub,num2Sub,total)
#----------------------------
def mulp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:mulp2
    Description:
    This function is the what takes in the first number for the multiplication sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numMul
    num = input("Please enter a number")
    try:
        numMul = int(num)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        mulp2()
def mulp3():
    '''
    --------------------------------------------------------------------------------------------------
    Name:mulp3
    Description:
    This function is the what takes in the second number for the multiplication sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global num2Mul
    num2 = input("Please enter a number")
    try:
        num2Mul = int(num2)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        mulp3()
    
def mulPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:mulPrint
    Description:
    This function is the what takes the inputs from the previous functions and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever multiplication question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    multiply(numMul,num2Mul)
    mulEquation(numMul,num2Mul,total)
#----------------------------
def divp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:divp2
    Description:
    This function is the what takes in the first number for the division sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numDiv
    num = input("Please enter a numerator")
    try:
        numDiv = int(num)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        divp2()
def divp3():
    '''
    --------------------------------------------------------------------------------------------------
    Name:divp3
    Description:
    This function is the what takes in the first number for the division sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global num2Div
    num2 = input("Please enter a denomenator")
    try:
        num2Div = int(num2)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        divp3()
    
def divPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:divPrint
    Description:
    This function is the what takes the inputs from the previous functions and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever division question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    try:
        divide(numDiv,num2Div)
    except ZeroDivisionError:
        print(numDiv,"/",num2Div,"= Cannot divide by zero!")
    else:
        divEquation(numDiv,num2Div,total)
#----------------------------
def recp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:recp2
    Description:
    This function is the what takes in the first number for the rectangle area sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numRec
    num = input("Please enter a side")
    try:
        numRec = int(num)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        recp2()
def recp3():
    '''
    --------------------------------------------------------------------------------------------------
    Name:recp2
    Description:
    This function is the what takes in the second number for the rectangle area sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global num2Rec
    num2 = input("Please enter a side")
    try:
        num2Rec = int(num2)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        recp3()
    
def recPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:recPrint
    Description:
    This function is the what takes the inputs from the previous functions and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever rectangle area question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    rectArea(numRec,num2Rec)
    rectEquation(numRec,num2Rec,total)
#----------------------------
def sqrp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:sqrp2
    Description:
    This function is the what takes in the first and only number for the square area sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numSqr
    num = input("Please enter a side")
    try:
        numSqr = int(num)
    except ValueError:
        print("Please use a number to select your number. Please try again")
        Sqrp2()
def sqrPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:sqrPrint
    Description:
    This function is the what takes the input from the previous function and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever square area question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    sqrArea(numSqr)
    sqrEquation(numSqr,numSqr,total)
#----------------------------
def circp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:circp2
    Description:
    This function is the what takes in the first and only number for the circle area sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numCirc
    num = input("Please enter a radius")
    try:
        numCirc = int(num)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        circp2()

def circPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:rircPrint
    Description:
    This function is the what takes the input from the previous function and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever circle area question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    circArea(numCirc)
    circEquation(numCirc,total)
#----------------------------
def trip2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:trip2
    Description:
    This function is the what takes in the first number for the triangle area sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numTri
    num = input("Please enter a side")
    try:
        numTri = int(num)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        trip2()
def trip3():
    '''
    --------------------------------------------------------------------------------------------------
    Name:trip3
    Description:
    This function is the what takes in the second number for the triangle area sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global num2Tri
    num2 = input("Please enter a height")
    try:
        num2Tri = int(num2)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        trip3()
    
def triPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:triPrint
    Description:
    This function is the what takes the inputs from the previous functions and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever triangle area question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    triArea(numTri,num2Tri)
    triEquation(numTri,num2Tri,total)
#----------------------------
def recVp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:recVp2
    Description:
    This function is the what takes in the first number for the rectangle volume sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numrecV
    num = input("Please enter a side")
    try:
        numrecV = int(num)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        recVp2()
def recVp3():
    '''
    --------------------------------------------------------------------------------------------------
    Name:recVp3
    Description:
    This function is the what takes in the second number for the rectangle volume sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global num2recV
    num2 = input("Please enter a side")
    try:
        num2recV = int(num2)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        recVp3()
def recVp4():
    '''
    --------------------------------------------------------------------------------------------------
    Name:recVp4
    Description:
    This function is the what takes in the third number for the rectangle volume sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global num3recV
    num3 = input("Please enter a side")
    try:
        num3recV = int(num3)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        recVp4()
def recVPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:recVPrint
    Description:
    This function is the what takes the inputs from the previous functions and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever rectangle volume question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    rectVol(numrecV,num2recV,num3recV)
    rectVolEquation(numrecV,num2recV,num3recV,total)
#----------------------------
def cubeVp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:cubeVp2
    Description:
    This function is the what takes in the first and only number for the cube volume sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numcubeV
    num = input("Please enter a side")
    try:
        numcubeV = int(num)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        cubeVp2()
def cubeVPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:cubeVPrint
    Description:
    This function is the what takes the input from the previous function and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever cube volume question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    cubeVol(numcubeV)
    cubeVolEquation(numcubeV,total)
#----------------------------
def cyliVp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:cyliVp2
    Description:
    This function is the what takes in the first number for the cylinder volume sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numcyliV
    num = input("Please enter a radius")
    try:
        numcyliV = int(num)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        cyliVp2()
def cyliVp3():
    '''
    --------------------------------------------------------------------------------------------------
    Name:cyliVp3
    Description:
    This function is the what takes in the second number for the cylinder volume sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global num2cyliV
    num2 = input("Please enter a height")
    try:
        num2cyliV = int(num2)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        cyliVp3()
def cyliVPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:clyiVPrint
    Description:
    This function is the what takes the inputs from the previous functions and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever cylinder volume question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    cyliVol(numcyliV,num2cyliV)
    cyliVolEquation(numcyliV,num2cyliV,total)
#----------------------------
def spheVp2():
    '''
    --------------------------------------------------------------------------------------------------
    Name:spheVp2
    Description:
    This function is the what takes in the first and only number for the sphere volume sequence.
    No Input
    Output: This function outputs what to input and if you input something wrong, like a letter.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    global numspheV
    num = input("Please enter a radius")
    try:
        numspheV = int(num)
    except ValueError:
        print("Please use a number to select your numbers. Please try again")
        sppheVp2()
def spheVPrint():
    '''
    --------------------------------------------------------------------------------------------------
    Name:spheVPrint
    Description:
    This function is the what takes the input from the previous function and uses them to calculate an answer and print it.
    No Input
    Output: This function outputs the equation and answer for what ever sphere volume question you asked.
    No Local Variables
    --------------------------------------------------------------------------------------------------
    '''
    sphereVol(numspheV)
    spheVolEquation(numspheV,total)


main()
