from copy import  deepcopy
#1
#string = input("Give me a verb, i'll add ing or ly accordingly: ")
#if len(string)>=3:
#    if ("ing") == string[-3:]:
#        string += "ly"
#        print string
#    else:
#        string += "ing"
#        print string
#else len(string)<3:
#    print string
#2
#sentence = input("Insert a sentence, preferrably with 'not' and 'poor' in it.")
#if ('not') and ('poor') in sentence:    
#3(revisit)
words = input("Give me a list of comma separated words.")
words = words.split(",")
words = list(words)
word_lengths = []
for word in words:
    length = len(word)
    word_lengths.append(length)
    max_value = str(max(words))
    max_value1 = str(max(word_lengths))
print ('Longest word: ' + max_value)
print ('Length of longest word: ' + max_value1)

#4
#string = input('Write stuff: ')
#string = list(string)
#item = int(input('What character would you like to be removed (starts from zero btw)'))
#del string[item]
#print string
#5?

#6

#7

#8
#d = {1:'a',2:'b',3:'c'}
#del(d[1])
#print (d)
#9, I copied this from class
names = ['Max','Matt','Sylas','Derrick']
ages = [11,11,13,10]
class_dictionary = dict(zip(names,ages))
print (class_dictionary)
#10

#11
#atuple = tuple(input('Give me letters'))
#addition = input('What would you like to add to the letters?')
#megatuple = atuple + tuple(addition)
#print str(megatuple)
#12
#atuple = ('abc','def','ghi')
#alist = str(atuple)
#alist_clean = alist.replace(",","").replace("'","").replace("(","").replace(")","")
#print (alist_clean)
#13
#atuple = tuple(input('Give me letters:'))
#print atuple[-5]
#14, I copied this from class
tuplex = ('Hello',5,[],True)
print tuplex
tuplecopy = deepcopy(tuplex)
print tuplecopy
tuplecopy[2].append(50)
print(tuplex)
print(tuplecopy)
