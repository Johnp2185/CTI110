#Phillip John
#11 Apr 24
#P4HW2
#A program that displays hours an employee(s) worked and rate of pay.

total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

#Enter employee's name.
while True:
   employee_name = input("Enter employee's name or 'Done' to terminate: ")
   if employee_name.lower() == "done":
      break
   total_employees += 1

   #Enter employee's hours worked and pay rate.
   hours_worked = float(input(f"How many hours did {employee_name} work? "))
   pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

   #Print a blank line for readability.
   print()

   #Print next employee:
   print("Enter name:  ", employee_name)

   #Print a blank line for readability.
   print()

   #Calculate hours worked, pay rate, overtime, overtime pay, reghour pay and gross pay.
   if hours_worked> 40:
      overtime_hours = hours_worked - 40
      regular_hours = 40
      overtime_pay = overtime_hours * pay_rate * 1.5
      total_overtime_pay += overtime_pay

   else:
     regular_hours = hours_worked
     overtime_hours = 0
     overtime_pay = 0
   regular_pay = regular_hours * pay_rate
   gross_pay = regular_pay + overtime_pay
   total_regular_pay += regular_pay
   total_gross_pay += gross_pay

   #Print hours worked, pay rate, overtime, overtime pay, reghour pay and gross pay with dollar symbols and decimal points as needed.
   print("Hours Worked   Pay Rate   OverTime    OverTime Pay   RegHour Pay      Gross Pay")
   print('--------------------------------------------------------------------------------')
   print(f"{hours_worked:<15.1f}{pay_rate:<11.1f}{overtime_hours:<11.1f} {overtime_pay:<14.2f} ${regular_pay:<15.2f} ${gross_pay:<15.2f}")

   #Print a blank line for readability.
   print()

print("\nTotal number of employees entered:",total_employees)
print("Total amount paid for overtime: $",total_overtime_pay)
print("Total amount paid for regular hours: $",total_regular_pay)
print("Total amount paid in gross: $",total_gross_pay)
