#Phillip John
#5 Mar 24
#P2HW1
#Create a program that calculate and display travel expenses based on user input

#Prompt user to input their budget, travel destination, estimated gas expense, accommodation/hotel expense, and food expense.
#Read the user inputs and store them in variables: Budget, Travel_Destination, Gas, Accommodation_Hotel, and Food.


Budget = int(input()) 
Travel_Destination = input()
Gas = int(input())
Accommodation_Hotel = int(input())
Food = int(input())

# Print the user inputs to confirm:
print('This program calculates and displays travel expenses')
# Print a blank line for readability.
print()
print('Enter Budget:', Budget)
# Print a blank line for readability.
print()
print('Enter your travel destination:', Travel_Destination)
# Print a blank line for readability.
print()
print('How much do you think you will spend on gas?', Gas)
# Print a blank line for readability.
print()
print('Approximately, how much will you need for accommodation/hotel?', Accommodation_Hotel)
# Print a blank line for readability.
print()
print('Last, how much do you need for food?', Food)
# Print a blank line for readability.
print()

# Print header for Travel Expenses:
print('---------------Travel Expenses-----------------------')
# Print the location and initial budget:
print('Location:            ', Travel_Destination)
print('Initial Budget:      ', '${:.2f}'.format(Budget))
# Print individual expense:
print('Fuel:                ', '${:.2f}'.format(Gas))
print('Accommodation:       ', '${:.2f}'.format(Accommodation_Hotel))
print('Food:                ', '${:.2f}'.format(Food))
# Calculate Travel Expenses:
Total_expenses = Gas + Accommodation_Hotel + Food
# Calculate Remaining balance:
Remaining_balance = Budget - Total_expenses 
print('----------------------------------------------------')
# Print a blank line for readability.
print()
# Print the remaining balance:
print('Remaining Balance:   ', '${:.2f}'.format(Remaining_balance))



 
