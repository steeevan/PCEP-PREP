# Note: This program doesn't run any functions made.
# Please run them yourself if you need to double check them, since I wasn't sure if you wanted to run them
# 1.
# Getting the two numbers by using an input. 
num1 = int(input("Please enter your first number: "))
num2 = int(input("please enter your second number: "))
# Addition
print("Addition: ",num1 + num2)
# Subtraction
print("Subtraction: ",num1 - num2)
# Multiplication
print("Multiplication: ",num1 * num2)
# Divison
print("Division: ",num1/num2)
# Modulus
print("Modulus: ",num1 % num2)
# 2.
# Getting the length and width by using an input. 
length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))
# Getting the area
area = length * width
# Getting the perimeter
perimeter = 2*length + 2*width
# Printing the area and perimeter
print("Area: ",area)
print("Perimeter: ",perimeter)
# 3.
# Getting the sentence
sentence = input("Please enter a sentence: ")
# Setting up all of the variables needed
l = len(sentence)
n = 0
vowels = 0
consonates = 0
# Making the loop so that way we go thru all of the of the letters in the sentence
for x in sentence:
    if sentence[n] == "a" or sentence[n] == "e" or sentence[n] == "i" or sentence[n] == "o" or sentence[n] == "u" or sentence[n] == "A" or sentence[n] == "E" or sentence[n] == "I" or sentence[n] == "O" or sentence[n] == "U":
        vowels += 1
    elif sentence[n] == "b" or sentence[n] == "c" or sentence[n] == "d" or sentence[n] == "f" or sentence[n] == "g" or sentence[n] == "h" or sentence[n] == "j" or sentence[n] == "k" or sentence[n] == "l" or sentence[n] == "m" or sentence[n] == "n" or sentence[n] == "p" or sentence[n] == "q" or sentence[n] == "r" or sentence[n] == "s" or sentence[n] == "t" or sentence[n] == "u" or sentence[n] == "v" or sentence[n] == "w" or sentence[n] == "x" or sentence[n] == "y" or sentence[n] == "z" or sentence[n] == "B" or sentence[n] == "C" or sentence[n] == "D" or sentence[n] == "F" or sentence[n] == "G" or sentence[n] == "H" or sentence[n] == "J" or sentence[n] == "K" or sentence[n] == "L" or sentence[n] == "M" or sentence[n] == "N" or sentence[n] == "P" or sentence[n] == "Q" or sentence[n] == "R" or sentence[n] == "S" or sentence[n] == "T" or sentence[n] == "U" or sentence[n] == "V" or sentence[n] == "W" or sentence[n] == "X" or sentence[n] == "Y" or sentence[n] == "Z":
        consonates += 1
    else:
        pass
    n += 1
# Prints the number of vowels and then the consonates
print(vowels)
print(consonates)
# 4.
# Getting the list of numbers and making it an actual list
numbers = input("Please input a list of numbers you wish to find the average from by entering a list seperated by space: ")
numbers2 = numbers.split()
# Making all of the parts of the list integers
for i in range(len(numbers2)):
    numbers2[i]= int(numbers2[i])
# Getting the total
total = sum(numbers2)
# Getting the length of the list
length = len(numbers2)
# Calculating the mean
mean = total / length
# Prints the mean
print(mean)
# 5.
# Getting the degrees in celcius from  the user
celcius = input("Enter the degrees celcius you want to turn into farenheit: ")
# Converting the variable celcius into a float then converting it to farenheit
celcius = float(celcius)
farenheit = (celcius * 9/5) + 32
# Printing the degrees in farenheit.
print(farenheit)
# 1.
# Getting the number to check if even or odd and converting the number into an integer so we can use modulus
num = input("Enter a number to check if its even or odd: ")
num = int(num)
# Use modulus to see if the number is even or odd and print the whether the number is even or odd
if num % 2 == 0:
    print("This number is even!")
else:
    print("This number is odd!")
# 2.
# Getting the number to count from one to that number and turn it into an integer
num2 = int(input("Enter a positive number for the program to print from one to that number: "))
# Making a for loop to count from one to that number and printing each number
for i in range(1,num2 + 1,1):
    print(i)
# 3.
# Getting the number to use to make a factorial
num3 = int(input("Enter a positive number for the program to use to make a factorial: "))
# Making the variable for the value of the factorial
facnum = 1
# Multiplying the variable by each value until the given number
for i in range(1,num3 + 1,1):
    facnum = facnum * i
# Prints the end value
print(facnum)
# 4.
# Importing random
import random
# Using random to get a random number between 1 and 10
randnum = random.randint(1,10)
# Making the user guess the number
guess = int(input("Guess a number from 1 to 10: "))
# Checking if the user was right, and repeating if they weren't
while guess != randnum:
    if guess > randnum:
        print("Your number was too high! Try again.")
        guess = int(input("Guess a number from 1 to 10: "))
    else:
        print("Your number was too low! Try again.")
        guess = int(input("Guess a number from 1 to 10: "))
# Printing that they got it right
print("Yay! You got the correct number!")
# 5.
num5 = int(input("Enter a positive number for the program to use to make a sum of all the numbers from 1 to the number you enter: "))
# Making the variable for the sum
sumofnum = 0
# Adding each value to the variable until the given number
for i in range(1,num5 + 1,1):
    sumofnum = sumofnum + i
# Prints the end value
print(sumofnum)
# 1.
# Importing datetime so we can use it
import datetime
# Getting the user's name and printing welcome with the user's name
name = input("Please enter your name: ")
print("Welcome " + name + "!")
# Getting the user's age and using that information to find out the user's birthyear and printing it out
age = int(input("Please enter your age: "))
now = datetime.datetime.now()
year = now.year
birthyear = year - age
print("You were born in " + str(birthyear) + "!")
# 2.
# Opening data.txt in write mode
file = open("data.txt","w")
# Getting the user to input a sentence or line of text
sen = input("Please enter a sentence or line of text: " )
# Writing that the user inputted into the file and closing it
file.write(sen)
file.close()
# Reopening the file in read mode and printing what is in the file
file2 = open("data.txt","r")
print("You have inputted: ",file2.read())
file2.close()
# 1.
import math
def calculate_area_circle(radius):
    '''
    --------------------------------------------------------------------------------------------------
    Name:calculate_area_circle
    Description:
    This function calculates a circle's area.
    Input: radius, which is the radius of the circle whose area the function will calculate.
    Ouptput: This function outputs the circle's area.
    Local Variables: area, a variable to hold the area of the circle
    --------------------------------------------------------------------------------------------------
    '''
    area = radius ** 2 * math.pi
    return area
rad = float(input("Enter a radius for a circle whose area you would like to calculate: "))
print("The area is ", calculate_area_circle(rad))

# 2.
def sum_of_squares(start,end):
    '''
    --------------------------------------------------------------------------------------------------
    Name:sum_of_squares
    Description:
    This function takes a start and ending number, gets all the numbers between them and squares them then find the sum of all of the squared numbers.
    Input: start: the starting number, end: the ending number
    Ouptput: This function outputs the total of all the squared numbers in between the start and ending numbers
    Local Variables: sumofnums, a variable to hold the sum of all the squared numbers
    --------------------------------------------------------------------------------------------------
    '''
    sumofnums = 0
    for i in range(start,end+1,1):
        sumofnums += i**2
    return sumofnums
st = int(input("Please enter a starting number for a sum of all numbers between this and the next number squared and added up: "))
en = int(input("Please enter a ending number for a sum of all numbers between this and the next number squared and added up: "))
print(sum_of_squares(st,en))
# 3.
# Getting the numerator and denomator from the user
num = float(input("Please enter a numerator for a division problem: "))
den = float(input("Please enter a denomenator for a division problem: "))
# Trying the division and seeing if there is the ZeroDivisionError and printing the answer if there was no error, and if there was, telling them that
try:
    ans = num/den
    print(ans)
except ZeroDivisionError:
    print("You tried to divide by ZERO! Why would you do that? Did you want to break my computer?!")
# 4.
# Importing random
import random
#Printing the randomized number from 1 to 10
print(random.randint(1,10))
# 5.
# Importing requests
import requests
# Assigning data from google into variable response
response = requests.get('https://www.google.com/')
# Assigning the content from respopnse into the variable content
content = response.content
# Printing the content
print(content)
# These are the REVIEW answers
'''
1. Python is a high-level programming language.
2. Lists are mutable, which means they can be changed, while tuples aren't.
3. A dictionary is a type of data storage that has a pair of values, first the key and tehn the value.
4. The purpose of an if statement is to check if something is true and if it is true, do something in the if statement.
5. A loop in Python is something that repeats certain code inside the loop until a certain condition is met.
6. A function is a reusable bit of code and a method is a function that is associated with an object or class.
7. The import statement lets you import different modules so you can use them in your program.
8. An exception in Python is an event where an error occurs.
9. The difference is that == is to check if two things are equal and is used in things like if statements, while is returns True or False based on if two things are the same.
10. The purpose of the len() function is to check how long an object is.
'''
# Please note that for any functions, I didn't actually use them in the program unless it was for testing
# This program doesn't use the function I make for these question, so feel free to run the functions if you're not sure that they're correct.
# 11.
# Making a variable to hold the sum
sumofeven = 0
# Adding all of the even numbers between 1 and 100 with a loop
for i in range(0,101,2):
    sumofeven += i
# Printing the end result
print(sumofeven)
# 12.
def palindromeCheck(string):
    '''
    --------------------------------------------------------------------------------------------------
    Name:palindromeCheck
    Description:
    This functionchecks if a string is palindrome.
    Input: string, which is the string the function will check if is palindrome
    Ouptput: This function outputs if the string is palindrome.
    Local Variables: reverse, a variable to hold the reverse of the string
    --------------------------------------------------------------------------------------------------
    '''
    reverse = string[:: -1]
    if reverse == string:
        print(string, "is palindrome.")
    else:
        print(string, " is not palindrome.")

# 13.
# Making a list with a bunch of numbers
listy = [1,2,3,4,57,1,1,1,1,1,1]
# Using the max function finds the biggest number and I assigned the number to a variable
maxy = max(listy)
# Priting the max number
print(maxy)
# 14.

def factorial(number):
    '''
    --------------------------------------------------------------------------------------------------
    Name:factorial
    Description:
    This function calculates a factorial of 1 to the input number.
    Input: number, the number the function calulates the factorial from 1 to
    Ouptput: This function outputs the factorial.
    Local Variables: facnum, the variable that stores the factorial's value
    --------------------------------------------------------------------------------------------------
    '''
    facnum2 = 1
    for i in range(1,number + 1,1):
        facnum = facnum * i
    print(facnum)
# 15.
# Making a variable with a number to check if the number is prime
checkprimenum = 11
# Making sure the number is bigger than 1, and if it is, checking if it is prime by seeing if it has a remainder of zero when dividing it by numbers from 2 to checkprimenum/2 + 1
# Once it figues out if the number is prime or not, it prints the answer
if checkprimenum > 1:
    for i in range(2, int(checkprimenum/2)+1):
        if checkprimenum % i == 0:
            print(checkprimenum,"is not a prime number.")
            break
    else:
        print(checkprimenum,"is a prime number.")
else:
    print(checkprimenum,"is not a prime number.")
# 16.
def reverselist(list2):
    '''
    --------------------------------------------------------------------------------------------------
    Name:reverselist
    Description:
    This function makes a reverse of the list.
    Input:list2, the list that will be reversed 
    Ouptput: This function outputs the reversed list.
    Local Variables: reverse3, the reversed version of the list
    --------------------------------------------------------------------------------------------------
    '''
    reverse3 = list2[:: -1]
    print("The reverse of ", list2, "is ",reverse3)
# 17.
# Making a sentence
sentence = "This is a sentence."
# Setting up all of the variables needed
l = len(sentence)
n = 0
vowels = 0
# Making the loop so that way we go thru all of the of the letters in the sentence
for x in sentence:
    if sentence[n] == "a" or sentence[n] == "e" or sentence[n] == "i" or sentence[n] == "o" or sentence[n] == "u" or sentence[n] == "A" or sentence[n] == "E" or sentence[n] == "I" or sentence[n] == "O" or sentence[n] == "U":
        vowels += 1
    else:
        pass
    n += 1
# Prints the number of vowels and then the consonates
print("There are ", vowels, " vowels in ", sentence)
# 18.
def second_smallest(listy):
    '''
    --------------------------------------------------------------------------------------------------
    Name:second_smallest
    Description:
    This function finds the second smallest number in a list.
    Input: listy, the list that this function will look through to find the second smallest number
    Ouptput: This function outputs the second smallest number in listy.
    Local Variables: smallest, the smallest number in the list, and second_smallest, the second smallest number in the list
    --------------------------------------------------------------------------------------------------
    '''
    smallest = listy[0]
    second_smallest = listy[1]
    for i in range(2, len(listy)):
        if listy[i] < smallest:
            second_smallest = smallest
            smallest = listy[i]
        elif listy[i] < second_smallest:
            second_smallest = listy[i]
    return second_smallest
# 19.
# Making the variables needed for the Fibonacci sequence
n = 30
a = 0
b = 1
square_a = a
square_b = b
# Printing how many terms will be printed
print("This is the Fibonacci sequence for ",n,"terms.")
# Printing the first number of the Fibonacci sequence
print(square_a)
# Using a for loop to generate the Fibonacci sequence, print it out a repeat it a certain amount of times
for i in range(1, n):
    temp = square_b
    square_b = square_b + square_a
    square_a = temp
    print(square_a)
# 20.
def triArea(base,height):
    '''
    --------------------------------------------------------------------------------------------------
    Name:triArea
    Description:
    This function is the function that calculates a triangle's area.
    Inputs: base and height, which both are the measurements of the triangle that this function will use to find the triangle's area
    Output: This function outputs the area of the triangle
    Local Variables: total, a variable that holds the triangle's area.
    --------------------------------------------------------------------------------------------------
    '''
    total = (base * height)/2
    print(total)


        
