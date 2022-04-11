"""
Calculate whether the number of weeks since a reference date is divisible by 2.
And use GitHub Actions outputs to store the result for use later on in the action.
"""
from datetime import date

# This is a Thursday after a cycle meeting, so we'll calculate every-two-weeks relative to this
start_date = date(2021,11,11)  
difference_days = abs(date.today() - start_date).days
n_days_since_last_meeting = difference_days % 14  # Because we have a new meeting every 14 days.
n_weeks_since_last_meeting = (n_days_since_last_meeting // 7) + 1
is_two_weeks = (n_weeks_since_last_meeting % 2) == 0  # Add 1 because we are effectively 0-indexed

# Store the output value for use later
# See https://docs.github.com/en/actions/learn-github-actions/workflow-commands-for-github-actions#using-workflow-commands-to-access-toolkit-functions
# for more information
print(f'::set-output name=N_DAYS_SINCE::{n_days_since_last_meeting}')
print(f'::set-output name=N_WEEKS_SINCE::{n_weeks_since_last_meeting}')
print(f'::set-output name=IS_TWO_WEEKS::{is_two_weeks}')
