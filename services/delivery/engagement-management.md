# Engagement Management

Project Management Tool: [Asana](https://app.asana.com/)

## Creating a new Engagement

When a HubSpot Deal has reached the pipeline stage of either 'Contract Admin' or 'Closed Won' we need to create an corresponding Asana Project to track the delivery for this engagement.

:::{note}
We have not, **yet**, automated the creation of Asana Projects from Hubspot Deals. Until then, follow the instructions below to create a new Asana Project when needed.
:::

Engagements are encoded in Asana as *Projects*.  To create a new Engagement, click **Create** in Asana and selection **Project**.

Use the project template *Engagement Project*. Set the name of the project to be the same string as the HubSpot Deal Name. (If the HubSpot Deal Name is incorrect, fix this first).

:::{attention}
Today, there is only one template called *Engagement Project*. In a future iteration of these instructions there could be templates of the form

- Premier Member Engagement
- Advanced Member Engagement
- Essential Member Enagagement

or equivalents for any class of Engagements that should have the same overall structure
:::
  
The templates sets the visibility of this new project to be "Everyone at 2i2c" and grants everyone "Project admin" access rights.  The project creator is automatically joins the project -- remove yourself from the project unless you personally want to receive notifications for each for every message, status update, and added task. 

This new project is automatically added to the portfolio of "Active Engagements". We use the "Active Engagements portfolio in Asana to drive 2i2c discussions about the health of our delivery. All new engagements need to be added to this portfolio. If the engagement serves a community with more than one contract, make sure the new engagement is also added to that community's portfolio.

After creating a new project, click the down arrow to the right of the project name (tooltip: 'Actions') and select 'Edit project details'.

Due date: Set the start and end date to match the (expected) contract start and end dates for this engagement.

Edit the custom fields
- Contract Value
- HubSpot Deal ID
- HubSpot Deal URL
- Membership Tier

to match the metadata for the corresponding Hubspot Deal.

## Adding tasks to an Engagement

Within an engagement, add tasks that need to completed deliver value to our community partner.  Tasks can be divided into sub-tasks.

Tasks and sub-tasks can have an associated GitHub issue url. 

::: {warning}
We don't, **yet**, have any automation to keep status or comments of GitHub issue in sync with Asana (sub-)tasks. Asana has built in support for tracking GitHub PRs within Asana but not Github Issues.
:::

Asana is a project planning tool. Use the Due Date fields for each task to capture the **anticipated** timeline when the task is to be scheduled.  Use the Estimated Time field to list the total time expected for the tast to be completed.  Due Dates and Estimate Time are needed for Asana to show the task on the Timeline view and to be used in capacity planning.

One of the default tasks in any engagement could be 'Confirm Renewal with Community' with a due date set to 60 days before the end of the engagement.
