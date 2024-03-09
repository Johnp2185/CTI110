#Phillip John
#7 Mar 24
#P2HW2
#Create a program that list grades and calculates the results

#Prompt user to enter grades for the following Modules.
#Read the user inputs and store in a list.

Module_1 = float(input())
Module_2 = float(input())
Module_3 = float(input())
Module_4 = float(input())
Module_5 = float(input())
Module_6 = float(input())

#Print a blank line for readability.
print()

#Print the user inputs to confirm:
print('Enter grade for Module 1:', '{:.1f}'.format(Module_1))
print('Enter grade for Module 2:', '{:.1f}'.format(Module_2))
print('Enter grade for Module 3:', '{:.1f}'.format(Module_3))
print('Enter grade for Module 4:', '{:.1f}'.format(Module_4))
print('Enter grade for Module 5:', '{:.1f}'.format(Module_5))
print('Enter grade for Module 6:', '{:.1f}'.format(Module_6))

#Print a blank line for readability.
print()

#Print header for Results:
print('---------------Results-----------------------')
#Create grade for each Module list:
Grades = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]

#Display lowest, highest, sum of grades and grades' average:
Lowest_Grade = min(Grades)
Highest_Grade = max(Grades)
Sum_of_Grades = sum(Grades)
Average = Sum_of_Grades/len(Grades)

#Print calculated grades with average appearing with two decimal positions:
print('Lowest Grade:         ', '{:.1f}'.format(Lowest_Grade))
print('Highest Grade:        ', '{:.1f}'.format(Highest_Grade))
print('Sum of Grades:        ', '{:.1f}'.format(Sum_of_Grades))
print('Average:              ', '{:.2f}'.format(Average))
print('----------------------------------------------------')


 
