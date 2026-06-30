(delivery:engagement-management)=
# Engagement Management

Project Management Tool: [Asana](https://app.asana.com/)

## Creating a new Engagement

When a [HubSpot](hubspot:index) Deal has reached the pipeline stage of either 'Contract Admin' or 'Closed Won' we need to create an corresponding Asana Project to track the delivery for this engagement.

:::{note}
We have not, **yet**, automated the creation of Asana Projects from Hubspot Deals. Until then, follow the instructions below to create a new Asana Project when needed.
:::

Engagements are encoded in Asana as _Projects_. To create a new Engagement, click **Create** in Asana and selection **Project**.

Use the project template *Engagement Project*. Set the name of the project to be the same string as the HubSpot Deal Name. (If the HubSpot Deal Name is incorrect, fix this first).
Once the `HubSpot Deal URL` field is set (see below), a [daily automation](#operations:data-sync) keeps the project name, contract value, and start/end dates matched to the HubSpot deal, so later changes in HubSpot propagate automatically.

The templates sets the visibility of this new project to be "Everyone at 2i2c" and grants everyone "Project admin" access rights. The project creator is automatically joins the project -- remove yourself from the project unless you personally want to receive notifications for each for every message, status update, and added task.

This new project is automatically added to the portfolio of "Active Engagements". We use the "Active Engagements portfolio in Asana to drive 2i2c discussions about the health of our delivery. All new engagements need to be added to this portfolio. If the engagement serves a community with more than one contract, make sure the new engagement is also added to that community's portfolio.

After creating a new project, click the down arrow to the right of the project name (tooltip: 'Actions') and select 'Edit project details'.

Due date: Set the start and end date to match the (expected) contract start and end dates for this engagement.

::: {attention} Ensure data consistency
Ensure that we create a "delivery brief" for the engagement that has all the information needed to understand the core objectives of that engagement.
Also, ensure the fields in Asana link back to the correct hubspot record
:::

Edit the custom fields to match the metadata for the corresponding Hubspot Deal:

- Contract Value
- HubSpot Deal ID
- HubSpot Deal URL
- Membership status (Member, Premier, Starter)
- Sage Grant ID (where available)

:::{note}
Hubspot Deal ID. Within Hubspot, look the URL in browser when look at the Deal page. The URL is something of the form

`https://app-na2.hubspot.com/contacts/242496330/record/0-3/86933236464?eschref=%2Fconta[…]496330%2Fobjects%2F0-3%2Fviews%2Fall%2Flist%3Fquery%3Diveda`

The HubSpot Deal URL is the string

`https://app-na2.hubspot.com/contacts/242496330/record/0-3/86933236464`

The HubSpot Deal ID is the identifier

`86933236464`

The intention is for this to eventually automated.
:::

## Adding tasks to an Engagement

Within an engagement, add tasks that need to completed deliver value to our community partner. Tasks can be divided into sub-tasks.

Tasks and sub-tasks can have an associated GitHub issue url.

::: {warning}
We don't, **yet**, have any automation to keep status or comments of GitHub issue in sync with Asana (sub-)tasks. Asana has built in support for tracking GitHub PRs within Asana but not Github Issues.
:::

### Guidance for Date fields

- Use the Due Date fields for each task to capture the **anticipated** timeline when the task is to be scheduled.
- Use the Estimated Time field to list the total time expected for the task to be completed. Due Dates and Estimate Time are needed for Asana to show the task on the Timeline view and to be used in capacity planning.

## Outcomes of the Engagement Management meeting

1. Review Engagements that are 60-days from expiration

- Ideally, we should have a check-in with the community.
- Start renewal conversations.
- Ensure that their is a renewal deal in HubSpot that represents this opportunity.

2. Review invoices - We want to focus on invoices that are more than 90-days outstanding

- Note that CS&S deals with all invoices that are less than 90-days.
- Use the finance [Overdue invoices](https://finance.2i2c.org/recovery/#overdue-invoices) plot to identify those invoices.

3. Review invoices that are `Off-track`, `At risk`, then `On-track`.

- Ensure that actions are recorded and assigned to an owner via the Asana Status feature.
- Whenever possible, create team visibility by creating a tracking GitHub issue on the [Operations board](https://github.com/orgs/2i2c-org/projects/64), then link that to the asana status.
One of the default tasks in any engagement could be 'Confirm Renewal with Community' with a due date set to 60 days before the end of the engagement.

(delivery:tracking-time)=
## Tracking time on tasks

Each engagement shows a standard set of task columns: `Allocation`, `GitHub URL`, `Estimated time`, `GitHub Hours`, and `Total Time`, plus the native `Assignee`, `Due date`, and `Actual time`.

Log your time in one place per task, and `Total Time` adds them up:

- `Actual time`: time logged directly in Asana with its built-in timer, for work not tracked in a GitHub issue.
- `GitHub Hours`: hours logged on the linked GitHub issue, synced into Asana automatically. Don't edit it in Asana, since the [sync](#operations:data-sync) overwrites it.
- `Total Time`: `GitHub Hours` plus `Actual time`, the combined figure to report against an engagement.

Use `Estimated time` for the hours a task is expected to take.
