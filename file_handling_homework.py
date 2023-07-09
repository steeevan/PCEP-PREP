# Task 1
a = input("Enter a file name:  ")
# Open the file
file = open("output2.txt", 'w')
# Write previous variable in the file
file.write(a)
# Close the file to save contents
file.close()
# Task 2
b = input("Enter a sentence:  ")
# Open the file
file = open("output2.txt", 'w')
# Write the user's input into the file
file.write(b)
# Close the file and let them know that the data has been saved
file.close()
print("Data saved successfully.")
# Task 3
# Totally not hacking
c = input("Enter your name:  ")
d = input("Enter your Email:  ")
# Open da file
file = open("contacts.txt", 'a')
# Append the data
file.writelines("\n"+c+"\n")
file.writelines("\n"+d+"\n")
# Close the file
file.close()
print("Data saved successfully.")
# Task 4
e = "John"
e2 = "24"
e3 = "johnny@gmail.com"
# Open the CSV file
file = open("people.csv", "w")
# Write the data into the file
file.write("\n"+e+"\n")
file.write("\n"+e2+"\n")
file.write("\n"+e3+"\n")
# Close the file and print a message to confirm that the data has been saved
file.close()
print("Data saved successfully.")
