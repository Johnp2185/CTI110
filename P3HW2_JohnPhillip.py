#Phillip John
#17 Mar 24
#P3HW2
#A program that displays hours an employee worked and rate of pay.

#Enter employee's name, hours worked and pay rate.
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print('--------------------------------------------')

#Print the user inputs to confirm:
print("Enter name:  ", employee_name)

#Print a blank line for readability.
print()

#Calculate hours worked, pay rate, overtime, overtime pay, reghour pay and gross pay.
if hours_worked> 40:
   overtime_hours = hours_worked - 40
   regular_hours = 40
   overtime_pay = overtime_hours * (pay_rate * 1.5)

else:
     regular_hours = hours_worked
     overtime_hours = 0
     overtime_pay = 0
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

#Print hours worked, pay rate, overtime, overtime pay, reghour pay and gross pay with dollar symbols and decimal points as needed.
print("Hours Worked   Pay Rate   OverTime    OverTime Pay   RegHour Pay      Gross Pay")
print('------------------------------------------------------------------------------------')
print(f"{hours_worked:<15.1f}{pay_rate:<11.1f}{overtime_hours:<11.1f} {overtime_pay:<14.2f} ${regular_pay:<15.2f} ${gross_pay:<15.2f}")





