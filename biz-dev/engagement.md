# Engagement workflow

2i2c's **Engagement workflow** is a sub-step of the [Sales Operation's](sales-operations.md) Delivery stage and includes activities required to manage delivery commitments (including reporting), ensuring that customers derive value from 2i2c’s offerings.

:::{figure} images/engagements-workflow.png

The structure of 2i2c's Engagement management workflow (linking CRM and Delivery Enablement)
:::

### Why this structure

Broadly, our sales processes span two main flows:

-   **Customer Relationship Management (CRM)** - This covers Pre-sales and Sales stages, championed by the Business Development team
-   **Delivery** - This covers everything in the Delivery stage. The Delivery Enablement and P&S teams are the champions.

Consequently, we need distinct engagement and project activities to improve delivery management, reporting and collaboration between the teams.

Implicit to the structure are the following:

1. The end-to-end delivery of community value is the responsibility of multiple teams within 2i2c
1. The Business Development (BD) team triggers the creation of delivery work after a customer agreement is created and,
1. The delivery of value requires distinct units of work (i.e. Engagement, Project and Project Deliverables, etc.)
1. The Delivery Enablement team can trigger renewal conversation in the BD team.

## Relationship between work activities

A successful sale (closed-won), triggers a sequence of processes in the Delivery Enablement and Product and Services team.

Below we identify the relationship between the different units of work in more detail.

**1. Opportunity management**

The Opportunity management process (also referred to as Customer Relationship Management (CRM) pipeline) governs how we acquire customers (opportunity to paying customer).

:::{figure} images/current-leads-process.png

CRM Opportunity management
:::

Within 2i2c, there are two types of Opportunities:

-   New Opportunities

    -   Each _Closed-Won_ Opportunity, must have at least one contract or an MOU in Airtable
    -   Only _Closed-Won_ Opportunities get assigned Engagements
    -   A _Closed-Won_ Opportunity can only have one Engagement

-   Renewal Opportunities
    -   These opportunities can automatically get an Engagements without an Memorandums of understanding (MoUs) or Contracts

**2. Engagement management**

**Engagements** (AirTable [link](https://airtable.com/appbjBTRIbgRiElkr/pagpZcdEaghJQiYH3)) are internal, 2ic abstractions that represent a collection of 2i2c projects used to manage the delivery of products and services in accordance with a contractual agreement. They have a discrete start and end which spans the lifetime of the associated grant or contract.

Additional properties of _Engagements_ include:

-   Each Engagement can have only one parent Opportunity.
-   Engagements can have multiple projects.

**3. Project management**

**Projects** (AirTable [link](https://airtable.com/appbjBTRIbgRiElkr/pag0zFFd2NaJHBHN5)) are a collection of project deliverables that need to be provisioned by the P&S team. Naturally, _Project deliverables_ represents the related work items required to deliver a service or value to a community or stakeholder.

Additional properties of _Project_ include:

-   Projects can only belong to a single Engagement
-   Projects can have multiple Project Deliverables
-   The Statement of Work will determine the Project and the deliverables
-   The completion of Projects enable service delivery

Let's clarify by way of an example.

> Example: Several things may need to be done to provision a new hub for a community that needs to run a 3-day workshop.
>
> -   **The project** would be to “Setup workshop hub”.
> -   **The project deliverables** would be all of the discreet tasks needed to complete the project.

**4. Project Deliverable tracking**

**Project Deliverables** (AirTable [link](https://airtable.com/appbjBTRIbgRiElkr/pagH0VmYIvboNT4Sh)) are the actual units of works that we track in the P&S Team.

Key properties of _Project Deliverables_ include:

-   These are discreet measurable units of work
-   We must be able to determine if the work is done
-   These discreet units of work are linked to GitHub issues
