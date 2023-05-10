
def get_class_grades():
     '''
     -------------------------------------------------------------------------------------------------------------
     Name: get_class_grades
     Description: This should prompt the user to enter a list of grades
     from their class. Then it returns the list

     Input:

     Output:
          + class_grades : The given list of grades by user
          
     Local Variables:
     -------------------------------------------------------------------------------------------------------------
     '''
     class_grades = input("Enter the grades for your class:  ")
     return class_grades

def class_summary(class_grades):
     '''
     -------------------------------------------------------------------------------------------------------------
     Name: class_summary
     Description: This should calculate the frequency of each Letter grade, and store it into
     a dictionary. It then returns the dictionary.

     Input:
          + class_grades : This represents the list of letter grades of the class
     Output:
          + dictionary_grades : This represents the table frequency of the class. 
          
     Local Variables:
          + dictionary_grades : This represents the table frequency of the class.
          + keys : keeps track of the keys in our dictionary
     -------------------------------------------------------------------------------------------------------------
     '''
     dictionary_grades = {}
     for letter_grade in class_grades:
          keys = dictionary_grades.keys()
          if letter_grade in keys:
               dictionary_grades[letter_grade] += 1
          else:
               dictionary_grades[letter_grade] = 1
     return dictionary_grades


# gets the grade list from teacher
my_class = get_class_grades()
summary = class_summary(my_class)
print(summary)
