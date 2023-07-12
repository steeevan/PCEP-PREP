# File Handling Homework
# Matt Shen


# Task 1.
'''
fileName = input("File name: ")

                               # its not finding sample.txt and idk why
file = open(f"sample.txt", 'r')

content = file.read()

    
file.close()

print(content)
'''


# Task 2.
'''
sentence = input("Enter a sentence: ")

file = open("output.txt", 'w')

file.write("Sentence: {}".format(sentence))

file.close()

print(f"Sentence has been added.")
'''


# Task 3.
'''
name = input("Enter your name: ")
email = input("Enter your email: ")

file = open("contacts.txt", 'a')

file.write("\nName: {} \nEmail: {}\n".format(name, email))

file.close()

print("done")
'''


# Task 4.
# confused
'''
info = [{
    
    "name1": "John",
    "age1": 928,
    "email1": "bestemailever",


    "name2": "Johnny",
    "age2": 927,
    "email2": "secondbestemailever",


    "name3": "Johnathan",
    "age3": 926,
    "email3": "thirdbestemailever"
        
}]

file = open("people.csv", 'w')

# only the names
file.write("Names:\n{}\n{}\n{}".format(info[0]["name1"], info[0]["name2"], info[0]["name3"]))

file.close()







'''



























