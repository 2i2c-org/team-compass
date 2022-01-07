
(support:process)=
# Support team process

:::{admonition} In Beta!
:class: warning
We are currently working out our support process.
The content on this page might change over time, and we welcome suggested changes and pull requests!
:::

This is a team process to track **support requests** from users on the hubs that we run.

## Overview

The **support team** is a two-person team of Support Stewards that oversees all support requests for users of 2i2c hubs.
The Support Stewards work together to regularly **communicate** with users that open FreshDesk tickets, route support-related to engineering team members, and keep track of this work to ensure it is completed.

For most support requests, we use [a FreshDesk service](https://2i2c.freshdesk.com/a/) to handle communication with the communities.

## Support team structure

The Support Team is a **two-person team** of Support Stewards that work together.
Tenure on the support team is **for four weeks**.
Every **two weeks** (generally at the sprint meeting), a Support Steward cycles off the support team, and a new team member joins the team.
The support team rotates through [the “Open Infrastructure Engineering Team” on this page](https://team-compass.2i2c.org/en/latest/about/team.html), in alphabetical order.

:::{seealso}
See [our Team Roles calendar](team-roles-calendar) to know when each team member serves in this role.
:::

## Responsibilities and expectations

These are some major responsibilities and goals of the support team:

- Be the main point of contact for all support tickets regardless of the community
- Communicate with the person opening a support ticket, to keep them in the loop
- Create backlog issues as-needed
- Route support issues to the engineering team in order to make the changes necessary to resolve the issue.
- During events, be extra attentive to support channels in case a change is needed.

:::{note}
We should try to respond to all support-related communications **within one working day**.
Even if the support request is not resolved, others appreciate when we keep them in-the-loop about what we're doing.
:::

## Tracking support items

### FreshDesk requests

For bugs, hub changes, improvements, and general questions, we use the [e-mail address `support@2i2c.org`](mailto:support@2i2c.org).
This is connected with [the 2i2c FreshDesk account](https://2i2c.freshdesk.com/), and is a central place for all support-related requests.

Many requests may be immediately resolved via a quick action or response to the community representative.
If a request requires consultation with the team, then:

- Open a Slack thread in the {guilabel}`#support-freshdesk` channel to discuss with others. If we need to track a work item to resolve the ticket over time, then:
- Open a GitHub issue with the {guilabel}`support` label, and add it to our Sprint backlog.

(support:issues)=
### Support issues

If resolving a support issue requires ongoing or concerted work, open a backlog issue tagged with the {guilabel}`support` label.

Support backlog items should:

- Be placed in our [Sprint Board](coordination:sprint-board).
- Include a reference to any FreshDesk tickets if they exist.
- Be prioritized over other backlog items for that sprint.

## Communication channels

We use two Slack channels to discuss support-related questions on the 2i2c hub:

- The [#support-freshdesk](https://2i2c.slack.com/archives/C028WU9PFBN) is for discussing support tickets on Freshdesk.
  Open a Slack thread for each support ticket, to have conversation around it amongst the team.
  This channel is private because there’s an assumption of privacy when we discuss community-specific support matters.
- The [#hub-support](https://2i2c.slack.com/archives/C01DB2JRP8W) channel is for discussing more general support-related issues relating to operating the 2i2c Hubs, and not not related to a specific FreshDesk ticket.
  This channel is public, so can be useful if we wish to invite conversation from non 2i2c team members.

## Lifecycle of a support request


Below is a summary of the major steps that make up the support process, from beginning to end of a ticket.

:::{note}
We should try to respond to all support-related communications within one working day.
:::

- When you receive a ticket, communicate that you have received it and note the next steps you’ll follow to resolve it (even if this just means investigating because you're not sure what is wrong).
- If needed, open a [support issue and add it to the backlog](support:issues).
  Note that we should still use Freshdesk for support communication on this request, the GitHub issue is just for 2i2c team members to coordinate.
- Identify an engineering team member that can pick up this work.
- Give the user updates every day or two as we work to resolve the issue.
- When it is resolved, tell the user what you’ve done to resolve the issue.
- Close any FreshDesk tickets and support issues that are related to this request.
- In some cases, it might be useful to also write down a private note in the FreshDesk
  ticket with a short summary of the situatione and/or add links to relevant discussions
  from other platforms.

## How to prioritize support requests

- Ask questions that will help us understand whether an issue is "critical". For example, "Does this effect many users on the hub, or just a subset?", "Does this problem always happen, or intermittently?", "Is the hub accessible at all or is it totally down?".
- Events should be prioritized (or in general, moments with a large influx of users)
- In general, "how much does this incident impact the users of a given hub?" is a good guideline for deciding what to prioritize


## Asking for help from others

The support team is primarily a **communicator** and a **router** - they are not necessarily the ones who carry out the changes needed to resolve a support issue.
Instead, the support team is empowered to ask engineering team members to pick up backlog items that are related to support requests.

When a support request is made that requires an action from a 2i2c engineer, a Support Steward should describe this change in a GitHub issue, and add it to the [Sprint Board](coordination:sprint-board).
Think about an engineering team member that likely has the skills and capacity needed, and ask them if they are willing to take on resolving this issue.
Try not to ask the same person for support help many times in a row - we should spread the work needed to address support issues across the team.

## Who can make support requests?

See the [2i2c documentation support page](support:email) for information about how users can open support requests.
