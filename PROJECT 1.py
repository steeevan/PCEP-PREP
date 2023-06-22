def main():
    '''
------------------------------------------------
Name: main
Description: It has the main code here and all
the dictionaries, list, and other data types.

------------------------------------------------
    '''
    print('''Academic Link student Information System''')
    print('''
The is project 1.
This system interacts with students grades in which are able to be modified.
Student Information System (SIS) is a comprehensive software solution designed to manage
and organize student-related data with educational insitutions. It serves as a centralized
resporitory for storying and retrieving essential information about students, facilitating
efficient administration, communication, and academic processes.''')

    name_students = ["Emily Wokerson", "Caleb Cantroast", "Kent Taekehint", "Tim Iddboy"]
    adress_students = ["991 PineApple Avenue", "666 BlueGuest Street", "YoruBest Avenue", "OutroVert street"]
    grades_students = [['A','F','B','F'],['F','F','F','F'],['D','A','A','A'],['B','B','B','B']]
    personal_information = [adress_students, grades_students]
    
def find_student(user_decision = 1 or 2 or 3 or 4):
    while user_decision != 0:
        user_decision = int(input('''
Which of the following are you wanting to know more information about?
1. Emily wokerson
2. Caleb Cantroast
3. Kent Taekehint
4. Tim Iddboy
Enter the numbered student: '''))
        if user_decision == 1:
            print('You have selected Emily Wokerson')
        elif user_decision == 2:
            print('You have selected Caleb Cantroast')
        elif user_decision == 3:
            print('You have selected Kent Taekehint')
        elif user_decision == 4:
            print('You have selected Tim Iddboy')
        else:
            quit


           
print(main)
print(find_student)





























    
