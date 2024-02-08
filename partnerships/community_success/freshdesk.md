# Using FreshDesk

We [use FreshDesk](support:freshdesk) as part of our support and lead management processes.
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

## Email routing rules

The following email addresses (which are configured as [Google Groups](https://groups.google.com/all-groups) for @2i2c.org) are routed to FreshDesk and automatically assinged the following FreshDesk groups:

| Email Address         | FreshDesk Group |
|-----------------------|-----------------|
| support@2i2c.org      | Support         |
| invoices@2i2c.org     | Invoices        |
| partnerships@2i2c.org | Partnerships    |
| hello@2i2c.org        | Partnerships    |

These mappings are configured within FreshDesk from `Admin` > `Email`.

## Automations

FreshDesk can perform automations on tickets. These automations are configured using `Admin` > `Automations`

1. Auto-response to new support tickets
- `If Group is Support Send Email to Requester`
- Support tickets get an automatically generated email acknowledging receipt of the ticket.

2. Invoice email automation
- `If Group is Invoices AND If Requester email is accounting@codeforsociety.org Skip Notification AND Set Status as Closed`
- CS&S copies all outgoing invoices to invoices@2i2c.org. This automations closes those tickets automatically.
