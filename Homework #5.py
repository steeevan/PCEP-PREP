### Homework 5
##
### 1. Fail
##
##'''
##wordLetters = {}
##word = input("Enter a string: ")
##position = 0
##repeat = False
##
##for i in word:
##    letters = wordLetters.keys() 
##    letter = word[position]
##    
##    if letter in letters:
##        wordLetters[letter] += 1
##        
##        repeat = True
##        
##    else:
##        wordLetters[letter] = 1
##        
##    highestNum = max(letters)
##    
##    print(wordLetters)
##    print(repeat)
##    print(highestNum)
##    
##    position += 1
##
##if repeat == False:
##    print("There were no repeated letters. ")
##else:
##    print()
##'''


### 2.
##
##def selectOperator():
    '''
    ---------------------------------------------------------
    Name: selectOperator

    Desc: asks the user to enter an operator Then returns

    Input(Parameter):

    Output:
        + userOperator: the user's chosen operator

    LocalVariables:
    ---------------------------------------------------------
    '''
##    userOperator = input("Enter the operator to use [*, +, -, /]: ")
##    
##    return userOperator
##
##
##def getTwoNumbers():
    '''
    ---------------------------------------------------------
    Name: getTwoNumbers

    Desc: asks user to input two numbers Then returns both

    Input(Parameter):

    Output:
        + num1: user's first number inputted
        + num2: user's second number inputted

    LocalVariables:
    ---------------------------------------------------------
    '''
##    num1 = int(input("Enter a number: "))
##    num2 = int(input("Enter a number: "))
##    
##    return num1, num2
##
###             Parameters can be named anything Name for their usage
##def calculate(num1, num2, operator):
    '''
    ---------------------------------------------------------
    Name: calculate

    Desc: uses operator to either add, subtract, divide, or multiply
          the user's two numbers If it is not valid operator,
          print select correct operator 

    Input(Parameter):
        + num1: user's first number inputted
        + num2: user's second number inputted
        + operator: the user's chosen operator

    Output:
        + sum of num1 and num2
        + difference of num1 and num2
        + quotient of num1 and num2
        + product of num1 and num2

    LocalVariables:
    ---------------------------------------------------------
    '''
##    if operator == '*':
##        return num1 * num2
##
##    elif operator == '/':
##        return num1 / num2
##
##    elif operator == '+':
##        return num1 + num2
##
##    elif operator == '-':
##        return num1 - num2
##
##    else:
##        print("Select correct operator.")
##
##o = selectOperator()
##n1,n2 = getTwoNumbers()
##
##print(calculate(n1,n2,o))


# 3. Im confused on the question's wording
##
##def moneyEarned():
##    money = int(input("Enter the amount of money earned: $"))
##    


### 4.
##
##def identifyNumber():
    '''
    ---------------------------------------------------------
    Name: identifyNumber

    Desc: asks user for a number and checks if the number is
         greater than or equal to True or if its less Then
         prints Error or True with the number depending on
         the number

    Input(Parameter): 

    Output:

    LocalVariables:
    ---------------------------------------------------------
    '''

##    number = int(input("Enter a number: "))
##    if number < True:
##        print("Error")
##    elif number >= True:
##        print(f"True, {number}")
##    
##identifyNumber()








