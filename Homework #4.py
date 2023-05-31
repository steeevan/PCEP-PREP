# Homework 4
import random

####### This does not work
# I dont know how to get parameters from UserInput into generate_number

### 1.
##def UserInput(min=0, max=10):
##    min = int(input("Enter the minimum: "))
##    max = int(input("Enter the maximum: "))
##    parameters = min,max
##    return parameters
##    
##print(UserInput())
##
### 2.
##def generate_number(parameters):
##
##    randomNumber = random.randint(min, max)
##    return randomNumber
##
###print(generate_number())
##
### 3.
##def mainFunction(min=1, max=2):
##    while min != max and max != 0:
##        UserInput()
##        generate_number()
##        
##        print(randomNumber)
##        
##    
##mainFunction()


# 4.
##def userNameAge():
##    '''
##    ---------------------------------------------------------
##    Name: userNameAge
##
##    Desc: asks the user for their name and age Then return
##
##    Input(Parameter):
##
##    Output:
##        + name: user's inputted name
##        + age: user's inputted age
##
##    LocalVariables:
##    ---------------------------------------------------------
##    '''
##    name = input("Enter your name: ")
##    age = int(input("Enter your age: "))
##    # put both items to return in same line
##    return name, age
##
##def HOYearsOld(age):
##    '''
##    ---------------------------------------------------------
##    Name: HOYearsOld
##
##    Desc: finds what year you will turn 100 by adding the
##          years you need to reach 100 to the current year
##          Then return the year
##
##    Input(Parameter):
##        + age: the user's inputted age
##
##    Output:
##        + sum of currentYear and differenceAge
##
##    LocalVariables:
##        + currentYear: the current year
##        + differenceAge: the difference of the user's current age
##                        and 100
##    ---------------------------------------------------------
##    '''
##    currentYear = 2023
##    differenceAge = 100 - age
##
##    return currentYear + differenceAge
##    
##name,age = userNameAge()
##futureYear = HOYearsOld(age)
##
##print(f"{name} is turning 100 years old in {futureYear}")


# 5. confused on wording of question
##def askForNumber():
##    '''
##    ---------------------------------------------------------
##    Name: askForNumber
##
##    Desc: asks user for a number Then returns
##
##    Input(Parameter):
##
##    Output:
##        + number: the user's inputted number
##
##    LocalVariables:
##                        
##    ---------------------------------------------------------
##    '''
##    number = int(input("Enter a number: "))
##    return number
##
##def oddOrEven(value=1):
##    '''
##    ---------------------------------------------------------
##    Name: oddOrEven
##
##    Desc: uses askForNumber() and finds if it is even or odd
##          Then prints result
##
##    Input(Parameter):
##        + value: the result of number % 2
##
##    Output:
##
##    LocalVariables:
##
##    ---------------------------------------------------------
##    '''
##    value = askForNumber() % 2
##    if value == 1:
##        print("Your number is odd.")
##    elif value == 0:
##        print("Your number is even.")
##        
##oddOrEven()


# 6.
##
##exampleList = [1, 11, 20, 5, 4, 8, 9, 2, 3]
##numbersLessThanFive = []
##
##for i in range(0, len(exampleList), 1):
##    if exampleList[i] < 5:
##        numbersLessThanFive.append(exampleList[i])
##    else:
##        continue
##
##print(numbersLessThanFive)
##        
##    
    



