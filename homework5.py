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
def select_operator():
    useroperator=input("Enter the mathematical operator that will be used: ")
    return useroperator
def get_two_numbers():
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    return num1, num2
def calculate(number1,number2,operator):
    if operator=='*':
        return number1*number2
    elif operator=='/':
        return number1/number2
    elif operator=='+':
        return number1+number2
    elif operator=='-':
        return number1-number2
    else:
        print("Select correct operator")
0=selectoperator()
n1,n2=get_two_numbers()
print(calculate(n1,n2,0)
#3
'''
money=str(input("How much money did you earn today, numerical value please: "))
x=5
while x>0:
    print(money)
    x-=1
'''
#4
