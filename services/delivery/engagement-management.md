(delivery:engagement-management)=
# Engagement Management

Project Management Tool: [Asana](https://app.asana.com/)

## Creating a new Engagement

When a [HubSpot](hubspot:index) Deal reaches the pipeline stage 'Contract Admin' or 'Closed Won', we create a corresponding Asana Project to track the delivery for this engagement.

:::{note}
We have not yet automated the creation of Asana Projects from HubSpot Deals. Until then, follow the instructions below to create one when needed.
:::

Engagements are encoded in Asana as *Projects*. To create a new Engagement, click **Create** in Asana and select **Project**.

Use the project template *Engagement Project* (currently the only template). Set the name of the project to be the same string as the HubSpot Deal Name. (If the HubSpot Deal Name is incorrect, fix this first).
Once the `HubSpot Deal URL` field is set (see below), a [daily automation](#operations:data-sync) keeps the project name, contract value, and start/end dates matched to the HubSpot deal, so later changes in HubSpot propagate automatically.

The template sets the project's visibility to "Everyone at 2i2c" and grants everyone "Project admin" access. The project creator automatically joins the project; remove yourself unless you want notifications for every message, status update, and added task.

The new project is automatically added to the "Active Engagements" portfolio, which we use to drive discussions about the health of our delivery. All engagements must be on this portfolio. If the engagement serves a community with more than one contract, also add it to that community's portfolio.

After creating a new project, click the down arrow to the right of the project name (tooltip: 'Actions') and select 'Edit project details'.

Due date: Set the start and end date to match the (expected) contract start and end dates for this engagement.

Edit the custom fields
- Contract Value
- HubSpot Deal ID
- HubSpot Deal URL
- Membership status (Member, Premier, Starter)

to match the metadata for the corresponding Hubspot Deal.

:::{note}
To find these values, open the Deal page in HubSpot and look at the browser URL. The HubSpot Deal URL is everything before the `?` (e.g. `https://app-na2.hubspot.com/contacts/242496330/record/0-3/86933236464`), and the Deal ID is the final number in it (e.g. `86933236464`). We intend to eventually automate this.
:::
