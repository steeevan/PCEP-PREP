# Task 1
# Make sure both files are in the same location
# Get the new file name and make a new file with the new name
file_name = input("Choose a name for the file:")
file = open(file_name+".txt","w")
# get the sample file and read it
file2 = open("sample.txt","r")
contents = file2.read()
file.write(contents)
# close both files
file.close
file2.close
# read the new file made
file = open(file_name+".txt","r")
# print the new file's contents
contents = file.read()
print(contents)
# close the file
file.close()

# Task 2

# Get the user to input a sentence
sentence = input("Enter a sentence")
# open the output.txt file and put the sentence in it 
file = open("output.txt","w")
file.write(sentence)
# close the file and print a message confirming the write operation
file.close()
print("The write function has been successfully done.")

# Task 3

# Get the user to input their name and email
name = input("Please enter your name: ")
email = input("Please enter your email: ")
# open the file contact.txt in append mode
file = open("contact.txt","a")
# put the user's name and email on a new line
file.writelines("name: "+name+"email: "+email+"\n")
# close the file and print a message confirming the append operation
file.close()
print("The append operation was completed.")

# Task 4

#import csv so we can use csv
import csv
# Create a list of dictionaries with people's details
person1 = {"name":"Estevan","age":"23","email":"estevanaquiano@magikid.com"}
person2 = {"name":"Rob","age":"25","email":"roberto@robots.com"}
person3 = {"name":"John","age":"48","email":"john@gmail.com"}
list_of_names = [person1,person2,person3]
# open a file called people.csv in write mode and write the contents of the list into the file
file = open("people.csv","w")
writer = csv.writer(file)
writer.writerow(["name", "age", "email"])
writer.writerow([person1["name"],person1["age"],person1["email"]])
writer.writerow([person2["name"],person2["age"],person2["email"]])
writer.writerow([person3["name"],person3["age"],person3["email"]])
# close the file and display a message confirming the write operation
file.close()
print("The write operation was completed")
