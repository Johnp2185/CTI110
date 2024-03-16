#Phillip John
#16 Mar 24
#P3LAB
#A program that takes in a year and determines if it's a leap year.


#Input year
input_year = int(input('Enter year:'))

#If-else calculation and structure
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
#Print year and leap year determination
if is_leap_year(input_year):
    print(input_year, '- leap year')
else:
    print(input_year, '- not a leap year')
 
