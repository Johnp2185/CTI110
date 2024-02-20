#Phillip John
#20 Feb 24
#P1HW2
#Create a program that calculate and display travel expenses based on user input

#Take user inputs
Budget = int(input())
Travel_Destination = input()
Gas = int(input())
Accommodation_Hotel = int(input())
Food = int(input())

#Print user inputs
print('Enter Budget:', Budget)
print('Enter your travel destination:', Travel_Destination)
print('How much do you think you will spend on gas?', Gas)
print('Approximately, how much will you need for accommodation/hotel?', Accommodation_Hotel)
print('Last, how much do you need for food?', Food)
print()

#Print Travel Expenses
print('---------------Travel Expenses-----------------------')
print('Location:', Travel_Destination)
print('Initial Budget:', Budget)
print()
print('Fuel:', Gas)
print('Accommodation:', Accommodation_Hotel)
print('Food:', Food)
print()

#Calculate Travel Expenses
Total_expenses = Gas + Accommodation_Hotel + Food
Remaining_balance = Budget - Total_expenses 

print('Remaining Balance:', Remaining_balance)




 
