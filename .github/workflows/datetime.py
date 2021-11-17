#import date function from datetime module
from datetime import date
import os

#provide the 1st date in YYYY,MM,DD format
start_date = date(2021,11,1)

#getting the result, abs = absolute value
#(date1-date2).days gives an integer number of dates
days = abs(date.today() - start_date).days

# // makes result an integer (and rounds down)
weeks = days // 7
is_two_weeks = (weeks % 2) == 0

# Store the variable value for use later
print(f'::set-output name=IS_TWO_WEEKS::{is_two_weeks}'
