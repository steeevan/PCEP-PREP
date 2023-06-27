#Python HW day 6
#Brista Lin
#Mr. Estevan
import sys
def main():
    '''
    --------------------------------------------------------------------------------------------------
    Name:main
    Description:
    This function is the entire program and all of the helper functions in one function. 
    No Input
    Ouptput: This function outputs the entire user interface.
    Local Variables: This function makes the two dictionaries used to store the grades and addresses, along with the student names.
    --------------------------------------------------------------------------------------------------
    '''
    global student_grades
    global student_addresses
    student_grades = {"Estevan Aquiano":["A","A","B","A"],"Jessica Aguayo":["A","A","B","A"],"Jayden Duran":["A","B","A","A"],"Samantha Duran":["B","A","A","A"]}
    student_addresses = {"Estevan Aquiano":"1234 Magikid Lane", "Jessica Aguayo":"0900 Old Forester Lane", "Jadyen Duran": "1255 Winchester Lane","Samantha Duran": "1255 Winchester Lane"}
    while True:
        student_list()
        student_choice = input("Which student do you want? Choose the Student based on the number.")
        find_student(student_choice)
        student_options()
#start of functions

def student_list():
    '''
    --------------------------------------------------------------------------------------------------
    Name:student_list
    Description:
    This function is the start of the program and it is used to print out a number ordered
    list of the names in the grades dictionary. It also makes sure
    that it still works even when you change the list in some way. It also prints what the program is about.
    No Input
    Ouptput: This function outputs the numbered list that is fully formatted and adjusted to the student_grades dictionary.
    Local Variables: This function makes a variable called num to provide the numbers for the formatting of the list.
    --------------------------------------------------------------------------------------------------
    '''
    ##############
    # It looks like this prints each time when you are back at main menu. It should only print once in the beginnging of the project
    ##############
    print("Academic Link Student Information System")
    print("This is Project 1")
    print("This system interacts with student grades in which are able to be modified.")
    print("Student Information System (SIS) is a comprehensive software soultion designed to magane and oragnize student-related data within educcational institutions. It serves as a centralized repository for storing and retrieving essential information about students, facilitating efficient administration, communication, and academice processes.")
    num = 1
    for i in student_grades:
        print(num,". ",i)
        num +=1
    
def find_student(choice):
    '''
    --------------------------------------------------------------------------------------------------
    Name:find_student
    Description:
    This function is what uses the user's choice that was made right after student_list() and figures out what student the user would like. It is made to always work if a student is removed or added.
    Input: choice. This parameter is what is used to determine what the user wanted.
    Ouptput: This function outputs what student the user selected or tells you that you input too big of a number and lets you try again.
    Local Variables: This function makes a variable called num2 to make the program cycle through each choiceof student possible.
    --------------------------------------------------------------------------------------------------
    '''
    num2 = 1
    for i in student_grades:
        if choice == str(num2):
            print("You have selected",i)
            find_student.user_choice = i
            break
        elif int(choice) > len(student_grades):
            print("Please input the number of the student you want. Please try again.")
            student_list()
            student_choice = input("Which student do you want? Choose the Student based on the number.")
            find_student(student_choice)
            break
        elif int(choice) == 0:
           sys.exit()
        else:
            num2 +=1
        
        
def student_options():
    '''
    --------------------------------------------------------------------------------------------------
    Name:student_options
    Description:
    This function is what makes a list of what a user can do with the student they chose. It is also what gets the user's choice to give you what you requested or do what you wish to do.
    No Input
    Ouptput: This function outputs a list of what you can do with the student the user chose and does what the user chose.
    Local Variables: This function makes a variable called option to get the number of the option the user wants to do.
    --------------------------------------------------------------------------------------------------
    '''
    print("What would you like to do?")
    print("1. View Report Card")
    print("2. View Current Address")
    print("3. Update Address")
    print("4. Remove student")
    print("5. Add student")
    option = input("Enter: ")
    if option == "1":
        get_grades()
    elif option == "2":
        get_address()
    elif option == "3":
        update_address()
    elif option == "4":
        remove_student()
    elif option == "5":
        add_student()
    elif option == "0":
        sys.exit()
    else:
        print("Please try again")
        student_options()
def get_grades():
    '''
    --------------------------------------------------------------------------------------------------
    Name:get_grades
    Description:
    This function is what tells you what the user's choice of student's grades are.
    No Input
    Ouptput: This function outputs the user's choice of student's grades.
    No Local Variables made
    --------------------------------------------------------------------------------------------------
    '''
    print(find_student.user_choice, "'s grades are:")
    print(student_grades.get(find_student.user_choice))
def get_address():
    '''
    --------------------------------------------------------------------------------------------------
    Name:get_address
    Description:
    This function is what tells you what the user's choice of student's address is.
    No Input
    Ouptput: This function outputs the user's choice of student's address.
    No Local Variables made
    --------------------------------------------------------------------------------------------------
    '''
    print(find_student.user_choice, "'s address is:")
    print(student_addresses.get(find_student.user_choice))
def update_address():
    '''
    --------------------------------------------------------------------------------------------------
    Name:update_address
    Description:
    This function is what lets the user change the user's choice of student's address.
    No Input
    Ouptput: This function outputs the user's choice of student address updated address after allowing you to update it.
    Local Variables: This function makes a variable called update which is an input that gets what the user's choice of student's new address will be.
    --------------------------------------------------------------------------------------------------
    '''
    print("Update address Below")
    update = input("Enter new address:")
    student_addresses[find_student.user_choice] = update
    print(find_student.user_choice, "'s new address is:",student_addresses.get(find_student.user_choice))
def remove_student():
    '''
    --------------------------------------------------------------------------------------------------
    Name:remove_student
    Description:
    This function is what removes the user's choice of student.
    No Input
    Ouptput: This function outputs that the user is getting removed.
    No Local Variables made
    --------------------------------------------------------------------------------------------------
    '''
    print("Removing ",find_student.user_choice,"from school records.")
    del student_grades[find_student.user_choice]
    del student_addresses[find_student.user_choice]
def add_student():
    '''
    --------------------------------------------------------------------------------------------------
    Name:add_student
    Description:
    This function is what lets you add a new student, their grades and their address.
    No Input
    Ouptput: This function outputs the questions that help the user make a new student.
    Local Variables: This function makes the local variables new_name, new_grades1, new_grades2, new_grades3, new_grades4, and new_address. These inputs are used to input the information about the new student.
    --------------------------------------------------------------------------------------------------
    '''
    new_name = input("What is the new student's name:")
    new_grades1 = input("What is the new student's first grade?")
    new_grades2 = input("What is the new student's second grade?")
    new_grades3 = input("What is the new student's third grade?")
    new_grades4 = input("What is the new student's fourth grade?")
    new_address = input("What is the new student's address?")
    student_grades.update({new_name:[new_grades1,new_grades2,new_grades3,new_grades4]})
    student_addresses.update({new_name:new_address})
main()
