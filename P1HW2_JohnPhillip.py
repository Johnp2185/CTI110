#Phillip John
#2 Mar 24
#P1HW2
#Create a program that calculate and display travel expenses based on user input

#Prompt user to input their budget, travel destination, estimated gas expense, accommodation/hotel expense, and food expense.
#Read the user inputs and store them in variables: Budget, Travel_Destination, Gas, Accommodation_Hotel, and Food.
Budget = int(input())
Travel_Destination = input()
Gas = int(input())
Accommodation_Hotel = int(input())
Food = int(input())

#Print the user inputs to confirm:
print('Enter Budget:', Budget)
print('Enter your travel destination:', Travel_Destination)
print('How much do you think you will spend on gas?', Gas)
print('Approximately, how much will you need for accommodation/hotel?', Accommodation_Hotel)
print('Last, how much do you need for food?', Food)
#Print a blank line for readability.
print()

#Print header for Travel Expenses:
print('---------------Travel Expenses-----------------------')
#Print the location and initial budget:
print('Location:', Travel_Destination)
print('Initial Budget:', Budget)

#Print a blank line for readability.
print()

#Print individual expense:
print('Fuel:', Gas)
print('Accommodation:', Accommodation_Hotel)
print('Food:', Food)
#Print a blank line for readability.
print()

#Calculate Travel Expenses:
Total_expenses = Gas + Accommodation_Hotel + Food
#Calculate Remaining balance:
Remaining_balance = Budget - Total_expenses 
#Print the remaining balance:
print('Remaining Balance:', Remaining_balance)
