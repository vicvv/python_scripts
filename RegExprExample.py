####################################################################
# Description: the task at hand is to create a date format converter.
# The program will convert a date in the format “mm/dd/yyyy” to the format
# month day, year
# Development Environment:  MAC, Home
#
# ###################################################################
introduction = '''
Prompt the user to obtain a date from the user.  Specify the required input 
format: mm/dd/yyyy  Use a regular expression to validate the user input date 
format. If the format is incorrect raise a SystemExit. Split the input string 
into respective month, day, and year components. Using a list to hold the month 
format as a string, convert the month input to the correct string month name.  
Use the Gregorian calendar.
'''
'''To determine whether a year is a leap year, follow these steps: 
1.If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
2.If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
3.If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
4.The year is a leap year (it has 366 days).
5.The year is not a leap year (it has 365 days).'''

import re


# function checks if year is leap and if yes it changes the number of days in
# list calendar for month December. Maybe it should of been class static method?
def check_leap(iyear):
    year = int(iyear)
    if year%FOUR == 0 and year%HUNDRED == 0 and year%(FOUR*HUNDRED) == 0:
        dcalendar[1][1] = DAYSINF
        return True
    else:
        return False


class UserInput:
    # class variables
    MINYEAR = 1000
    MAXYEAR = 2999
    MINDAY = 1
    MINM = 1

    # variables that can change
    default_input = 'X'
    # init the constructor
    def __init__(self, dinput=None):
        self.dinput = dinput if dinput is not None else self.default_input
    # setting the input. Making sure that the input meets the requirement
    def set_input(self, dinput):
        uinput = self.valid_input(dinput)
        if uinput:
            self.dinput = uinput
            return True
        else:
            self.dinput = self.default_input
            return False

    # getting the day value
    def get_day(self):
        try:
            if self.dinput != self.default_input and \
                    self.MINDAY <= int(self.dinput[0]) \
                    <= dcalendar[int(self.dinput[1])-self.MINM][1]:
                return self.dinput[0]
        except IndexError:
            return False
        return False

    # getting the month
    def get_month(self):
        if self.dinput != self.default_input and \
                self.MINM <= int(self.dinput[1]) <= len(dcalendar):
            return dcalendar[int(self.dinput[1])-self.MINM][0]
        else:
            return False

    # getting the year
    def get_year(self):
        if self.dinput != self.default_input and \
                self.MINYEAR <= int(self.dinput[2]) <= self.MAXYEAR:
            return self.dinput[2]
        else:
            return False

    # this method uses re module to check if our input is
    # correct and also it checks the leap year
    @staticmethod
    def valid_input(dinput):
        try:
            (dd, mm, yyyy) = re.split('/',dinput)
        except ValueError:
            return False
        try:
            if int(dd) < 0 and not re.match('\d{2}', dd):
                return UserInput.default_input
            elif int(mm) < 0 and not re.match('\d{2}', mm):
                return UserInput.default_input
            elif yyyy[0] == '0' and not re.match('\d{4}', yyyy):
                return UserInput.default_input
            else:
                check_leap(yyyy)
                return (dd, mm, yyyy)
        except (ValueError, SystemExit):
            return False



FOUR = 4
HUNDRED = 100
DAYSINF = 29


dcalendar = [['January', 31],
['February',28 ],
['March',31],
['April',30],
['May',31],
['June',30],
['July',31],
['August',31],
['September',30],
['October',31],
['November',30],
['December',31]]

while True:
    uinput = input("Enter the date if the following format dd/mm/yyyy: ")
    if uinput.upper() == 'Q':
        break
    checkInput = UserInput()
    checkInput.set_input(uinput)

    (month, day, year) = \
        (checkInput.get_month(), checkInput.get_day(), checkInput.get_year())
    if False in (day, month, year):
        print("\nInvalid input in day, month or year")
    else:
        print("\nYou entered ", uinput, end = '')
        print(" The conversion result is " , month, day, year)
        continue








