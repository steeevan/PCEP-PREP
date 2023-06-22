# Project 1, School System
# Matt Shen
# 6 / 15 / 23

import sys

isQuit = False


# the one that uses the support functions
def findStudent():
    '''
    ---------------------------------------------------------
    Name: findStudent

    Desc: finds student based of studentChoice in students
          if entered 0, quit Can add new student if the user
          inputs the last option When a student is selected, displays
          options on what to view from the student Then, studentInfo
          will decide what action to do, like viewing address or
          removing that student

    Input(Parameter):

    Output:

    LocalVariables:
        + studentNumber: list of students keys (student names)
    ---------------------------------------------------------
    '''

    global studentNumber
    studentNumber = list(students.keys())

    # to quit
    if studentChoice == 0:
        print("You have left the program.")
        exit()

    # Adding a student
    if studentChoice == len(studentNumber)+1:
        addNewStudent(students, studentChoice, studentNumber)

    
    else:
        print(f"You have selected {studentNumber[studentChoice-1]}.")

        print('''
What would you like to do?
1. View Report Card
2. View Current Address
3. Update Address
4. Remove Student
''')

        # input for command
        studentInfo = int(input("\n> "))

        # Quitting
        if studentInfo == 0:
            print("You have left the program.")
            exit()

        # Getting Grades
        elif studentInfo == 1:
            getGrades()

        # Address
        elif studentInfo == 2: 
            print("The current address is", students[studentNumber[studentChoice-1]]["Address"])#students.get(studentNumber[studentChoice-1], {}).get("Address"),".")
            
        # updating address
        elif studentInfo == 3:
            updateAddress()

        elif studentInfo == 4:
            removeStudent()
    

def addNewStudent(students, studentChoice, studentNumber):
    '''
    ---------------------------------------------------------
    Name: addNewStudent

    Desc: asks for new student name and address and grades
          Then adds them to students

    Input(Parameter):
        + studentChoice: The user's choice of which student to view
        + students: the dictionary with the students info and names
        + studentNumber: the list of students keys (student names) 

    Output:

    LocalVariables:
        + newStudentName: new student's name
        + newStudentAddress: new student's address
        + newStudentGrades: new student's grades
    ---------------------------------------------------------
    '''
    newStudentName = input("Enter the new student's name: ").title()
    newStudentAddress = input("Enter the new student's address: ")
    newStudentGrades = input("Enter the new student's grades: ")

    students[newStudentName] = {"Address": newStudentAddress,
                            "Grades": newStudentGrades}


def updateAddress():
    '''
    ---------------------------------------------------------
    Name: updateAddress

    Desc: show the current address and ask the user to input
          the new address Then make that the new address for
          the student

    Input(Parameter):

    Output:

    LocalVariables:
    ---------------------------------------------------------
    '''
    print("The current address is", students[studentNumber[studentChoice-1]]["Address"])
    students[studentNumber[studentChoice-1]]["Address"] = input("Enter new address: ")
    print(f"Address has been updated to: {students[studentNumber[studentChoice-1]]['Address']}")



def getGrades():
    '''
    ---------------------------------------------------------
    Name: getGrades

    Desc: retrieves the student's grades and display them

    Input(Parameter):

    Output:

    LocalVariables:
    ---------------------------------------------------------
    '''
    print(f"The student's grades are {students[studentNumber[studentChoice-1]]['Grades']}")


def removeStudent():
    '''
    ---------------------------------------------------------
    Name: removeStudent

    Desc: removes student from students

    Input(Parameter):

    Output:

    LocalVariables:
    ---------------------------------------------------------
    '''
    del(students[studentNumber[studentChoice-1]])
    print("The student has been removed.")
    


def main():
    '''
    ---------------------------------------------------------
    Name: main

    Desc: creates dictionary of students and prints intro

    Input(Parameter):

    Output:

    LocalVariables:
        + students: dictionary of students' names and info
            
    ---------------------------------------------------------
    '''
    
    print("---Student Information System---")
    print('''
Student Information System (SIS) is a comprehensive software solution
designed to manage and organize student-related data within educational
institutions. It serves as a centralized repository for storing and
retrieving essential information about students, facilitating efficient
administration, communication, and academic processes.

To quit the program, enter '0'.
''')
    
    ################# Dictionary of Students ###################
    global students
    students = {
        "John": {
            "Grades": ['A', 'B', 'A-', 'B+'],
            
            "Address": "Burger St. 9284"        
        },
        
        "Bill": {
            "Grades": ['C', 'C-', 'C+', 'B-'],
            
            "Address": "McDonalds"
        },
        
        "Johnny": {
            "Grades": ['F', 'F', 'F+', 'F'],
            
            "Address": "NE KFC 3802 "
        },
        
        "Billy": {
            "Grades": ['D', 'D-', 'D-', 'D+'],
            
            "Address": "BK 382394u83415089"
        }
    }


def askCommand():
    '''
    ---------------------------------------------------------
    Name: askCommand

    Desc: displays students names and asks the user which
          student they would like to know more about
          Or they may add a student

    Input(Parameter):

    Output:

    LocalVariables:
        + students: dictionary of students' names and info
            
    ---------------------------------------------------------
    '''
    counter = 1
    
    # Answering
    print("\nWhich student would you like to know more information about?")

    
    for k in students: 
        print(f"{counter}. {k}") 
        counter += 1
    print(f"{counter}. [ Add Student ]")
        
    # Choice
    global studentChoice
    studentChoice = int(input("\n> "))





main()    

while isQuit != True:
    askCommand()
    findStudent()

exit()

