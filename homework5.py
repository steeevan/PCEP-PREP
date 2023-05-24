#1
'''
def get_sentence():
    something=input("Spit words, preferrably with no spaces: ")
    return something
def char_count(something):
    chars={}
    for char in something:
        values=chars.keys()
        if char in values:
            chars[char]+=1
        else:
            chars[char]=1
    return chars
sentence = get_sentence()
list1 = char_count(sentence)
print (max(list1.keys()))
print (max(list1.values()))
'''
#2
'''
import sympy
op=input("Give me a mathematical operation sign: ")
num1=input("What is the first number that will be used in the equation?")
num2=input("What is the second number that will be used in the equation?")
equation=(num1,op,num2)
'''
#3
'''
money=str(input("How much money did you earn today, numerical value please: "))
x=5
while x>0:
    print(money)
    x-=1
'''
#4
1=int(input("Give me a number: "))
if 
