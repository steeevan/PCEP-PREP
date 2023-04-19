import math as M
import collections
##############
string=str(input("String: "))
if "ing" not in string:
    print(string+"ing")
if "ing" in string:
    print(string+"ly")
##############
sting=str("The lyrics are poor.")
if 'not' and 'poor' in sting:
    print("The lyrics are good!")
    print(sting)
##############
test_list=['gfg','is','best']
print("The original list: "+str(test_list))
res=max(len(ele) for ele in test_list)
print("Length of maximum string is :"+str(res))
##############
stri="greek, latin, roman."
n=4
modded_str=" "
for char in range(0,len(stri)):
    if(char!=n):
        modded_str+=stri[char]
print(modded_str)
##############
def removeOddIndexCharacters(s):
    new_s=""
    i=0
    while i<len(s):
        if(i%2==1):
            i+=1
            continue
        new_s+=s[i]
        i+=1
    return new_s
if __name__=="__main__":
    strig="abcdefr"
    sttr=removeOddIndexCharacters(strig)
    print(sttr)
##############
dictionary1={1:"ABC123",2:"Goofy Ahh Beat Vol.1",3:"Limon Soda: Ripoff Sprite",4:"Starring: Dude, It Isn't Halloween Yet"}
print(1+2+3+4)
##############
print(1*2*3*4)
##############
print(dictionary1.pop(4))
##############
tuple1=tuple("124")
tuple2=tuple("14")
print(tuple1+tuple2)
##############
tupletty=tuple("1")
print(tupletty[0])
##############
tupleton=tuple(":")
print(tupleton[0])
##############
listyfoot=[(3,4),(4,5),(3,4),
           (3,4),(4,5),(6,7)]
print("The original list:"+str(listyfoot))
res=[]
for i in range(len(listyfoot)):
    for j in range(i+1,len(listyfoot)):
        if listyfoot[i]==listyfoot[j] and listyfoot[i] not in res:
            res.append(listyfoot[i])
print("Duplicates: " + str(res))