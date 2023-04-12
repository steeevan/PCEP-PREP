#1
#import sys
#print sys.version
#2
#import datetime
#current_time = datetime.datetime.now()
#print current_time
#3
import math
#radius = float(input('What is the radius of the circle?'))
#area = math.pi*radius**2
#print ("Area =" + str(area))
#4
#fname = input("What is your first name?")
#lname = input("What is your last name?")
#print (lname + " " + fname)
#5
values = input("Input some comma separated numbers: ")
v_list = values.split(',')
v_tuple = tuple(v_list)
print ('List: ', v_list)
print ('Tuple: ', v_tuple)
#6
#color_list = ["Red","Green","White","Black"]
#print (color_list [0], color_list [3])
a = int(input('Input an integer:'))
n1 = int('%s' % a)
n2 = int('%s%s' % (a,a))
n3 = int('%s%s%s' % (a,a,a))
print(n1+n2+n3)
#8
#radius = float(input('What is the radius of the sphere?'))
#volume = math.pi*4/3*radius**2
#print ('Volume =' + str(volume))
#9
#number = input('What do you want to subtract 17 from?')
#number = int(number)
#if number>17:
#    number -=17
#    number*=2
#    print number
#else:
#    number -=17
#    print number
#10
#a = int(input('What is your first number?'))
#b = int(input('What is your second number?'))
#c = int(input('What is your third number?'))
#if a == b == c:
#    big_sum=a + b + c
#    big_sum*=3
#    print (big_sum)
#else:
#    small_sum=a + b + c
#    print (small_sum)
#11
#number = int(input('What is the number that will be assigned even or odd?'))
#mod = number%2
#if mod == 1:
#    print ('This is an odd number')
#else:
#    print ('This is an even number')
#12
#letter = input('What is the letter that will be assigned to a vowel or consonant?')
#vowels = ['a', 'e', 'i', 'o', 'u']
#consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
#if letter in vowels:
#    print ('This is a vowel')
#elif letter in consonants:
#    print ('This is a consonant')
#else:
#    print ('What were you trying to accomplish...')
#13
#list1 = list(input('What are you trying to find something from?'))
#list2 = input('What are you trying to find?')
#if list2 in list1:
#    print ('It is inside the list')
#else:
#    print ('not inside lol')
#14
#listt = input('What is the list that will be entered?')
#16
#base = int(input('What is the base of your triangle?'))
#height = int(input('What is the height of your triangle'))
#area = base*height*0.5
#print area
#17

#18

#19
#i know how to do this problem, i just didnt have enough time to do it
#20
num1 = int(input('What is the first number of the equation?'))
num2 = int(input('What is the second number of the equation?'))
summ = num1+num2
if num1+num2 in range(15,20):
    return 20
else:
    return summ
