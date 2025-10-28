# Using FreshDesk

:::{note}
This page highlights Freshdesk, an online platform 2i2c uses for managing our technical support queue. Technical support is vital for the success of 2i2c's customers. As of 2025-04-25, there are team-wide discussions about responsibility, accountability and reporting lines around customer success.
:::

We [use FreshDesk](support:freshdesk) as part of our support processes.
This service has its own functionality and quirks, and this page is a place to document some common actions we must take.

(freshdesk:footer)=
## Add a footer to all replies

Sometimes it is useful to auto-add a footer to all support ticket responses.
This will come pre-populated in our response, and we can then add more text as we wish.
This is useful for things like [notifying communities about expected downtime](time-off:annual-expected).

[Here's the FreshDesk page on adding a footer](https://support.freshdesk.com/en/support/solutions/articles/196889-i-want-to-insert-a-footer-into-all-my-replies-how-do-i-do-this-).
And a quick summary:

1. Go to `Admin` > `Workflows` > `Email Notifications`.
2. Click on the `Templates` tab > `Agent Reply Template`.
3. Edit the form in order to add the text you'd like.

## Average Handling Time

FreshDesk tracks 'Average Handling Time (AHT)' for people whose role is 'Agent'. So we need to set up our team members as 'Agents' as well as 'Account Administrators' to enable this feature.

The AHT counter is only active while the ticket status is 'Open' (not Pending, Resolved, or Closed) and for the 'Assigned Agent'. The counter appears to increment only when the tab/window in the browser for that ticket is active and in-focus.
So it really is tracking the 'Handling Time' of the ticket by the assigned agent, and not the activity we are doing outside of FreshDesk related to solving the ticket.

FreshDesk also supports a 'Time Logs' feature of can be used for recording the time spent on a ticket but we are not using that feature within 2i2c.
