#!/usr/bin/env python3

'''
OPS445 Assignment 1b 
Program: assignment1.py 
The python code in this file is original work written by
"Alexander Ko". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Author: Alexander K>
Semester: Fall 2024
Description: This script is for Assignment1b, thiws will hel;p with the calculation of a future or past date from given
date on the specified number of days.
'''

import sys

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) #This is the leap year logic, this will be checking the given year with the logic.

def mon_max(month: int, year: int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    if month == 2: #This is for the month feburary as its the only month that is special with less days 28 or 29.
     return 29 if leap_year(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]: # This is for the other months that have 31 days
     return 31
    elif month in {4, 6, 9, 11}: #This is for the months with 30 days so the 4 6 9 11 months.
     return 30
    else:
     raise ValueError("Invalid month") #This is the error handling for invalid month input if an incorrect on ei sgiven.

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function has been tested to work for year after 1582
    '''
    year, mon, day= (int(x) for x in date.split('-')) #This will helpp us split the input date in the format year month and the day.
    day += 1  # This will increase the day by 1

    lyear= year % 4 #
    if lyear == 0:
     leap_flag = True
    else:
     leap_flag = False #This is not a leap year

    lyear = year % 100
    if lyear == 0:
     leap_flag = False # this is not a leap year

    lyear = year % 400
    if lyear == 0:
     leap_flag = True #This is a leap year

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
     mon_max = 29
    else:
     mon_max = mon_dict[mon]

    if day > mon_max: # if the day inputted exceed max days
     mon += 1 #this will move to next month
     if mon > 12: # if month is over december
      year +=1 #this will move year by 1
      mon = 1 #this will reset month to jan
     day = 1 #if tmp_day > this month's max, reset to 1
    return f"{year}-{mon:02}-{day:02}" #this is the formatted date

def before(date: str) -> str:
    "Returns previous day's date as YYYY-MM-DD"
    year, mon, day = (int(x) for x in date.split('-')) #this will also help split input date into  the year month and day like the after function.
    day -= 1 # this is decreasing the day b 1

    if day < 1: #if the day is less than 1 it will move to previous month with mon -=1
     mon -= 1
     if mon < 1: #if month is less than the 1sst month which is janurary
      mon = 12 #this will reset month back to 12 month which is december
      year -= 1 #this will decrease year by 1 
     day = mon_max(mon, year) #this wills et day to max days in new month
    return f"{year}-{mon:02}-{day:02}" # same return formatted date

def usage():
     "Print a usage message to the user"
     print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")
     sys.exit() #this is just exiting the program

def valid_date(date: str) -> bool:
    "This function will check validity of date in YYYY-MM-DD."
    try:
     year, mon, day = (int(x) for x in date.split('-')) #this will split  again into year month and day
     if year < 1000 or year > 9999: #this is the range for years to check if its valid or not
      print('Error: Incorrect year entered') #this is my error message
      return False
     elif mon < 1 or mon > 12:  #this will help check if my month is valid
      print('Error: Incorrect month entered') #this is my error message
      return False
     last_day = mon_max(mon, year)
     if day < 1 or day > last_day:
      return False
     return True
    except ValueError: #this is for invalid date input
     return False


def dbda(start_date: str, step: int) -> str:
    "given a start date and a number of days into the past/future, give date"
    # create a loop
    # call before() or after() as appropriate
    # return the date as a string YYYY-MM-DD
    date = start_date #this is to start the date with start_date

    for _ in range(abs(step)): #this will be my loop through number of steps
     if step > 0:
      date = after(date) #this will move forward
     else:
      date = before(date) #this will go backward
    return date #this is the final calcuated date after deciding whetehr to move forward oe backward with date

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
   if len(sys.argv) != 3: # this is to check for correct number of arguments
     usage()

   start_date = sys.argv[1] #this is the start date from command line arugments
   step = int(sys.argv[2]) #this is the step from command line arguments

   if not valid_date(start_date):  #this i sto validate
    print("Error: Incorrect date format.")  #this is my error message
    usage()


   try:
    step = int(step) #this is to oconvert step to integer
    if step == 0:  #this is to check if step is 0
     print("Error: Step cannot be zero.")  #this is error message saying cant be 0
     usage()
   except ValueError:  #this is to handle the non integer step
    print("Error: Step has to be an integer.") #error message saying step must be an integer
    usage()


   days = round(365 / abs(step)) #this is the  calculation days based on the step

   past_date = dbda(start_date, -days) #this will calcualte past date
   future_date = dbda(start_date, days) #thi sis to calcuate the future

   print(f"The year divided by {step} is {days} days.")  #this is the display of the results
   print(f"The date back then was {days} days ago was {past_date}.")
   print(f"The date in the future is {days} days from now will be {future_date}.")
