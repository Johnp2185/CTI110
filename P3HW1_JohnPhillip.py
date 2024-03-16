#Phillip John
#16 Mar 24
#P3HW1
#This program takes a number grade, determines average and displays letter grade for average.

#Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
#Print a blank line for readability.
print()

#Print the user inputs to confirm:
print('Enter grade for Module 1:', '{:.1f}'.format(mod_1))
print('Enter grade for Module 2:', '{:.1f}'.format(mod_2))
print('Enter grade for Module 3:', '{:.1f}'.format(mod_3))
print('Enter grade for Module 4:', '{:.1f}'.format(mod_4))
print('Enter grade for Module 5:', '{:.1f}'.format(mod_5))
print('Enter grade for Module 6:', '{:.1f}'.format(mod_6))
#Print a blank line for readability.
print()

#Print header for Results:
print('---------------Results-----------------------')

#Add grades entered to a list, determine lowest, highest, sum and average for grades.
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
lowest_grade = min(grades)
high_grade = max(grades)
sum_of_grades = sum(grades)
Average = sum_of_grades/len(grades)

#Print calculated grades with average appearing with two decimal positions:
print('Lowest Grade:         ', '{:.1f}'.format(lowest_grade))
print('Highest Grade:        ', '{:.1f}'.format(high_grade))
print('Sum of Grades:        ', '{:.1f}'.format(sum_of_grades))
print('Average:              ', '{:.2f}'.format(Average))
print('----------------------------------------------------')
#determine letter grade for average.
if Average >= 90:
   print('Your grade is: A')
if Average > 80:
   print('Your grade is: B')

else:
   print('Your grade is: F')







