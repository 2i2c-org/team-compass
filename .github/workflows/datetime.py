#import date function from datetime module
from datetime import date
import os

# This is a Tuesday before a sprint meeting, so we'll calculate every-two-weeks relative to this
start_date = date(2021,11,9)  
difference_days = abs(date.today() - start_date).days

# // makes result an integer (and rounds down)
weeks = difference_days // 7
is_two_weeks = (weeks % 2) == 0

# Store the variable value for use later
print(f'::set-output name=IS_TWO_WEEKS::{is_two_weeks}')
