# Homework 3
# Matt Shen

# Strings

# 1.
##word = input("Please enter a word: ").lower()
##if len(word)>= 3:
##    if word[-3::1] == "ing":
##        word += "ly"
##        print(word)
##    else:
##        word += "ing"
##        print(word)
##else:
##    print(word)


# 2.
##string = input("Please enter a string: ").lower()
##if "not" in string:


# 3. doesnt work
##words = []
##for i in range(4):
##    word = input("Enter a word: ")
##    words.append(word)
##    
##print(words)
##for i in range(len(words)+1):
##    if i == 0:
##        word1 = len(words[i])
##    if i == 1:
##        word2 = len(words[i])
##    if i == 2:
##        word3 = len(words[i])
##    if i == 3:
##        word4 = len(words[i])
##
##################################
##if word1 > word2:
##    if word1 > word3:
##        print(words[0] + str(word1))
##        
##        if word1 > word4:
##            print(words[0] + str(word1))
##            
##        if word1 < word4:
##            print(words[3] + str(word4))
##            
##    if word1 < word3:
##        print(words[2] + str(word3))
##
##        
##elif word2 > word3:
##    if word2 > word4:
##        print(words[1] + str(word2))
##        
##        if word2 > word1:
##            print(words[1] + str(word2))
##            
##        if word2 < word1:
##            print(words[0] + str(word1))
##            
##    if word2 < word4:
##        print(words[3] + str(word4))
##    
##
##        
##elif word3 > word4:
##    if word3 > word1:
##        print(words[2] + str(word3))
##        
##        if word3 > word2:
##            print(words[2] + str(word3))
##            
##        if word1 < word2:
##            print(words[1] + str(word2))
##            
##    if word3 < word1:
##        print(words[0] + str(word1))
##
##        
##elif word4 > word1:
##    if word4 > word2:
##        print(words[3] + str(word4))
##        
##        if word4 > word3:
##            print(words[0] + str(word1))
##            
##        if word1 < word3:
##            print(words[2] + str(word3))
##            
##    if word1 < word2:
##        print(words[1] + str(word2))
        

# Dictionary

# 8. doesnt work
##dictionary = {
##    "key": 5 
##}
##
##dictionary.remove[""]


# Tuples

# 11.
items = ("hi", "what", "who", "what")
##items = items + ("where",)
##print(items)

# 12.
items = "".join(items)
print(items)









