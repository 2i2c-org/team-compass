"""
Calculate whether the number of weeks since a reference date is divisible by 2.
And use GitHub Actions outputs to store the result for use later on in the action.
"""
from datetime import date

# This is a Tuesday before a sprint meeting, so we'll calculate every-two-weeks relative to this
start_date = date(2021,11,9)  
difference_days = abs(date.today() - start_date).days

# // makes result an integer (and rounds down)
weeks = difference_days // 7
is_two_weeks = (weeks % 2) == 0

# Store the output value for use later
# See https://docs.github.com/en/actions/learn-github-actions/workflow-commands-for-github-actions#using-workflow-commands-to-access-toolkit-functions
# for more information
print(f'::set-output name=IS_TWO_WEEKS::{is_two_weeks}')
