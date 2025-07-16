# Engagement Workflow Overview

Below we identify the relationship between the different units of work in more detail.

There are 3 critical abstractions for Engagement management that have been encoded in AirTable:

1. Engagements
2. Projects
3. Project Deliverables

## How we represent Engagments in AirTable

### Engagement management

**Engagements** (AirTable [link](https://airtable.com/appbjBTRIbgRiElkr/pagpZcdEaghJQiYH3)) are internal, 2ic abstractions that represent a collection of 2i2c projects used to manage the delivery of products and services in accordance with a contractual agreement. They have a discrete start and end which spans the lifetime of the associated grant or contract.

Additional properties of _Engagements_ include:

-   Each Engagement can have only one parent Opportunity (_Hubspot Deal_).
-   Engagements can have multiple projects.
-   RAG Statuses

**Engagement RAG Status**

RAG statuses are flags at the Engagements level that represent the overall assessment of how an engagement is progress towards meeting its deliverables across all projects.

RAG statuses are expected to trigger actions.

-   **Action needed (Red)** - We are not on track to complete the committed statement of work during the performance period of the engagement. Communication with the stakeholders and rescoping of the deliverables is required.
-   **Monitor/at risk (Amber)** - The statement of work is still likely on track for completion but requires reprioritization or additional attention to meet its deliverables and due dates.
-   **On track (Green)** - The statement of work is currently on track with no action needed.

### Project management

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

### Project Deliverable tracking

**Project Deliverables** (AirTable [link](https://airtable.com/appbjBTRIbgRiElkr/pagH0VmYIvboNT4Sh)) are the actual units of works that we track in the P&S Team.

Key properties of _Project Deliverables_ include:

-   These are discreet measurable units of work
-   We must be able to determine if the work is done
-   These discreet units of work are linked to GitHub issues
