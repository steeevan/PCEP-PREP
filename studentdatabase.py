import sys
def main():
    print("""
    This is Project 1, consisting of a student database that contains names,
    grades, and addresses. The user(you) will be able to access different
    parts of the database, as well as interact with the database and its
    contents in different ways.
    """)
#-------------------------------------------------------------------------------------------------------------
    '''
    Name: main

    Description: This is the main function, containing the dictionary and all the other functions

    Input: Everything from the other functions in the program (does that count?)

    Output: This function will print out the names of the students

    Variables:
    student_data: this is the dictionary that contains all of the student info; name, age, and address
    '''
    global student_data
    student_data = {"Sylas":['C','A','A','A',"110 Fake St."],
                    "Derrick":['B','A','A','B',"456 AUGHHH Ave."],
                    "Brista":['A','C','A','B',"789 Nope Rd."],
                    "Max":['D','C','A','A',"54321 Backrooms Way"],
                    "Matt":['A','B','A','A',"54321 Backrooms Way"]}
    global action_list
    action_list = ["Get grades","Get address","Update address","Remove student","Add student"]
    find_student()

def find_student():
    counter = 1
    print("Which student would you like to know more about? ")
    for i in student_data:
        print(counter,".",i)
        counter += 1
    global selected_student
    selected_student = input("Enter the name of the student here: ").title()
    global chosen_one
    chosen_one = student_data[selected_student]
    if selected_student in student_data:
        print("\nYou have selected", selected_student, "\n")
        choose_action()
    else:
        print("Invalid student name. Perhaps there is a spelling error?\n")
        find_student()
        
def choose_action():
    counter = 1
    print("What would you like to know about or do with this student?")
    for i in action_list:
        print(counter,".",i)
        counter += 1
    selected_action = int(input("Enter the number of the action here: "))
    if selected_action == 1:
        get_grades(selected_student)
    elif selected_action == 2:
        get_address()
    elif selected_action == 3:
        update_address()
    elif selected_action == 4:
        remove_student()
    elif selected_action == 5:
        add_student()
    elif selected_action == 0:
        sys.exit
def update_address():
    get_address(chosen_one)
    new_address = input("What is the new address of the student? ")
    student_data[selected_student][-1] = new_address
def get_address():
    print(chosen_one,"address is",chosen_one[-1])
def get_grades():
    
def remove_student():
    del(student_data[selected_student])
def add_student(database):
    name = input("Enter the name of the new student: ")
    info = print(list(input("Enter the grades and address of the student: ")))
    database[name] = info

main()
