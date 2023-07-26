# Homework Assignment: Data Types and Operators
# Matt Shen

# 1.
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

add = num1 + num2
sub = abs(num1 - num2)
mult = num1 * num2
if num2 == 0:
    print("Division and Modulus not possible.")
    div = None
    mod = None
else:
    div = num1 / num2
    mod = num1 / num2

print(f"Add: {add}\n\
Sub: {sub}\n\
Mult: {mult}\n\
Div: {div}\n\
Mod: {mod}\n")
'''


# 2.
'''
length = int(input("Input the length of the rect: "))
width = int(input("Input the width of the rect: "))
area = length * width
perim = (length + width) * 2

print(f"Area: {area}\nPerimeter: {perim}")
'''


# 3.
'''
sentence = input("Enter a sentene: ")
vowels = 0
consonants = 0
sentenceSep = list(sentence)

for n in range(0, len(sentenceSep)):
    if sentenceSep[n] == 'a' or sentenceSep[n] == 'e' or sentenceSep[n] == 'i' \
       or sentenceSep[n] == 'o' or sentenceSep[n] == 'u':
        vowels += 1
        
    else:
        consonants += 1

print(f"Vowels: {vowels}\nConsonants: {consonants}")
'''


# 4.
'''
numInput = input("Input a list of numbers seperated by spaces: ")
numList = numInput.split()

for i in range(len(numList)):
    numList[i] = float(numList[i])
    
numSum = sum(numList)
average = numSum / len(numList)
print("Average: ", average)
'''


# 5.
'''
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit: ", fahrenheit)
'''


# Examples: Control Flow with Decisions and Loops


# 1.
'''
integer = int(input("Enter integer: "))
if integer % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
'''


# 2.
'''
num = int(input("Enter a positive number: "))
for i in range(1, num + 1):
    print(i)
'''


# 3.
'''
num = int(input("Enter a positive number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i

print(fact)
'''


# 4.
'''
import random

randomNum = random.randint(1, 10)
print(randomNum)

guess = int(input("Guess the number between 1-10\n> "))

# keeps asking
while guess != randomNum:
    if guess > randomNum:
        print("The guessed number is too high!")
    elif guess < randomNum:
        print("The guessed number is too low!")
    
    guess = int(input("Try Again!\n> "))


print("You WIN!")
'''


# 5.
'''
num = int(input("Enter a positive number: "))
numSum = 0

for i in range(1, num + 1):
    numSum += i

print(numSum)
'''


# Examples: Input/Output Operations


# 1.
'''
import datetime

name = input("Enter your name: ")
print(f"Welcome, {name}!")

age = int(input("Enter your age: "))

birthYear = datetime.date.today()
birthYear = birthYear.year - age

print(f"Birth Year: {birthYear}")
'''


# 2.
'''
file = open("data.txt", 'w')

sentence = input("Enter a sentence: ")

file.write(sentence)

file.close()

file = open("data.txt", 'r')

content = file.read()

print(content)

file.close()
'''


# Examples: Code Documentation, Structure, Errors/Exceptions, Modules/Tools


# 1.
'''
import math

def calculateAreaCircle(radius):

##    ---------------------------------------------------------
##    Name: calculateAreaCircle
##
##    Desc: calculates the area of a circle by the given radius
##
##    Input(Parameter):
##        + radius: the radius of the circle
##
##    Output:
##
##    LocalVariables:
##    ---------------------------------------------------------


    area = math.pi * radius**2
    return area

radius = float(input("Enter the radius of a circle: "))
    
print("Area: ", calculateAreaCircle(radius))
'''


# 2.
'''
def sumOfSquares(start, end):
##    ---------------------------------------------------------
##    Name: sumOfSquares
##
##    Desc: gets the square of the numbers from start to finish and adds them up
##
##    Input(Parameter):
##        + start: the start of the numbers
##        + end: the end of the numbers
##        
##    Output:
##
##    LocalVariables:
##        + numSum: the sum of the squared numbers
##    ---------------------------------------------------------

    numSum = 0
    for i in range(start, end):
        print(i)
        numSum += i**2
        
    print(numSum)

sumOfSquares(1, 5)
'''


# 3.
'''
try:
    numer = float(input("Enter a numerator: "))
    denom = float(input("Enter a denominator: "))
    quotient = numer/denom
except ZeroDivisionError:
    print("Canot divide by zero.")
except:
    pass
'''


# 4.
'''
random = random.randint(1, 10)
print(random)
'''


# 5.
'''
import requests # doesn't exist?
get = requests.get("https://www.youtube.com/watch?v=fx2Z5ZD_Rbo")

# im confused on this and how it works
'''


##################################################################

### Review

# 1.
# Python is a high-level programming language that allows you to code things.

# 2.
# A list can be editted after it is made while a tuple cannot be
# a list uses [] but a tuple uses ()

# 3.
# A dictionary is like a hash table with key-value pairs
# accessing a key will give the key's value

# 4.
# the purpose of the if statement is to check if something is true or not and
# allow it to go to a block of code or not
# conditional statement

# 5.
# A loop in Python is when a block of code is repeated for a certain amount of times

# 6.
# a function is a block of code that can be accessed and used over and over again 
# a method is like a command or code that helps with code

# 7.
# the import statement can allow the coder to get packages or capabilities you would not
# not have access to in the code already

# 8.
# an excepction in python is when the code raises an error and shows it to the user

# 9.
# the difference between '==' and '=' is that '==' is a comparative operator while '='
# assigns values and data

# 10.
# the len() function allows the user to get the lenght of the parameter, like a list



################################################################


# 11.
'''
numSum = 0
for i in range(1, 101):
    if i % 2 == 0:
        numSum += i
        print(numSum)
    else:
        pass
print(numSum)
'''

# 12.
'''
def palindrome(word):
    flippedWord = word[::-1]
    if word == flippedWord:
        print("Palindrome")
    else:
        print("Not")

palindrome("tacocat")
'''

# 13.
'''
list = [1, 4, 82, 190, 1192, 42, 234, 0.11]
list.sort()
print(f"Largest Number: {list[-1]}")
'''

# 14. 
'''
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i

    print(fact)

factorial(4)
'''

# 15.
'''
num1 = 39
num2 = 100

for i in range(2, num1):
    if num1 % i == 0:
        print(f"{num1} is Not Prime")
        break
    else:
        print(f"{num1} is Prime")
        

for i in range(2, num2):
    if num2 % i == 0:
        print(f"{num2} is Not Prime")
        break
    else:
        print(f"{num2} is Prime")  
'''

# 16.
'''
def reverse(list1=[1, 2, 3]):
    list1.reverse()
    return list1

print(reverse([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
'''

# 17.
'''
vowels = 0
string = "Hello, world!"
string = list(string)

for n in range(0, len(string)):
    if string[n] == 'a' or string[n] == 'e' or string[n] == 'i' \
       or string[n] == 'o' or string[n] == 'u':
        vowels += 1
        
print(vowels)
'''

# 18.
'''
def secondSmallest(theList=[4,3,2,1]):
    theList.sort()
    print(f"Second Smallest Number: {theList[1]}")

secondSmallest([1023, 18, 13, 1, 0.01, 802])
'''

# 19.
'''
# confused ??
import math

a, b = 0, 1
count = 0

def fib(nterms, count = 0):
    if count < nterms:
        print(a)
        ab = a + b
        a = b
        b = ab
        count += 1
        fib()
    
fib(7)
'''

# 20.
'''
def triArea(base, height):
    area = (base * height) / 2
    print(f"The area is {area}.")
    
triArea(5, 10)
'''

















