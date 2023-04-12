#1
colors = ["blue", "red", "green","orange","black"]
#2
for i in colors:
     print(i)
#3
colors.append("aqua",)
colors.append("white")
print( colors)
#4
a = colors[0]
b = colors[6]
colors[0] = b
colors[6] = a
print(colors)
#-----------------------------------------------
#1
tuplex = ('a','b','c')
print(tuplex)
print(tuplex[0])
#2
n1, n2, n3 = tuplex
print(n1)
print(n2)
print(n3)
#3
tuplexx = tuplex + ('d',)
print(tuplexx)
#4
word = " ".join(tuplexx)
print(word)
#4 Derricks Not correct!
word = str(tuplexx)
print(word)


#--------------------------------------
word = "Matt"
word_size = len(word)
print(word_size)

def char_frequency(str1):
     dictionary = {}
     for n in str1:
          keys = dictionary.keys()
          if n in keys:
               dictionary[n] += 1
          else:
               dictionary[n] = 1
     return dictionary

print(char_frequency(word))
