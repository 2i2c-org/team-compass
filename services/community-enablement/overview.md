# Overview

The Community Enablement Service supports communities that benefit from collaborative partnership with 2i2c. It allows us to allocate dedicated staff to work closely with a community to reach specific goals. These engagements are time-bound and effort-bound.

```{note}
# Commmunity Enablement
- Foster strong partnerships between 2i2c and community leaders.
- Enable communities to build capacity using open tools.
- Provide dedicated consulting, meeting participation, documentation support, and more.
```

The communities that 2i2c serves have a variety of needs. For some communities, a streamlined and highly scalable service that is lower cost is a primary objective. For other communities, 2i2c may agree to work in a more collaborative way to achieve shared goals and outcomes.  

When Business Development identifies that a community may benefit from an increased level of service beyond what is offered in our Managed Interactive Computing Service and Technical Support Service, BD should offer 2i2c Community Enablement Service as an option.

Community Enablement Service represents an allocation of one or more 2i2c team members to working with a community to achieve a shared objective or outcome.The particular details of the allocation should be broadly understood when the Community Enablement Service is negotiated but BD should reserve the right to make changes (such as the particular 2i2c team members involved) during the Community Enablement Service engagement.

If software engineering or feature development is the goal, a different 2i2c service is more appropriate so that explicit deliverables can be as laid out in a scope of work. Community Enablement Service is most appropriate where 2i2c is committing to participating in a community or a project with **well defined time bounds on the nature of that commitment**. Some examples may include:

- Dedicated consultation and guidance on open source science and tools
- Dedicated consultation and community participation in open science  
- Regular participation in community led meetings
- Peer support through a dedicated channel

The key pieces of information to be clarified when a Community Enablement Service is being offered are
1. The period over which the Community Enablement Service is active;
2. The number of hours (as a proxy for FTE equivalency) being offered;
3. A general description of the nature of work being committed to by 2i2c.

Community Enablement Service is meant for allocating small fractions of a FTE and not intended to be used for secondments or subcontracting of 2i2c team members. Time (measured in hours) spent on Community Enablement Service needs to represent the capacity consumed by the overall 2i2c team. Internally, 2i2c needs to represent this work as a fraction of our overall team’s capacity. It needs to recognize the opportunity cost of context switching. 

The following scale is suggested to record, in units of hours, activity performed as part of Community Enablement Service:

- “1” -  Less than an hour of activity. Responding to an email or participating in a short call.
- “2” - An hour long synchronous meeting with a community including additional time for preparation and follow up.
- “3” - Up to two hours of effort on a project such as a code review or document preparation.
- “5” - Half a day’s effort, such as a long co-working session.
- “8” - Full day (“8 hours”) of activity dedicated to a Partnership Service activity

If multiple people are providing a Community Enablement Service concurrently, then the number of units consumed should be increased accordingly.

A unit of effort (even if nominally 1 billable hour) will, in almost all cases, never be exactly equal to one hour of wall clock time. We are not tracking 2i2c team members’ time to the minute. One unit of effort needs to represent not only the frontstage activity of the person doing the Partnership Service activity but also the backstage activity of the rest of the team involved in supporting that activity.

## Objective of the Service

2i2c’s mission is to grow a _global network of community hubs for interactive learning and discovery_. The ideal Community Enablement Service project is 2i2c helping research and education communities create and develop an interactive computing platform that gives communities a digital home to create and share knowledge with a global network of communities to learn from.

## Implementation

Business Development needs to seek confirmation from the corresponding Area Lead (Product & Services Leadership, Business Development Lead, Delivery Manager, or Executive Director) that there is sufficient capacity and capability available in the team to make a commitment to a Partnership Service offering.

In closing an Opportunity, the service agreement must contain a Statement of Work that describes the Partnership Service being offered. See Statements of Work for details of what needs to be included. 

When an Opportunity is closed, Delivery Enablement creates the Engagement to define what 2i2c has committed to deliver. Engagements are composed of Projects which describe time- bound outcomes from the engagement.  When a Partnership Service is offered under a service agreement, it is encoded as an ‘Allocation’ associated with a Project with 

- Allocation Start Date
- Allocation End Date
- Allocation Description
- Allocation Units of Time

This captures what 2i2c has actually committed to a community partner: a shared outcome and goal with the constraints of a certain maximum units of effort in a given period. A Project may have multiple Allocations if the Partnership Service needs to be broken up into over discrete subperiods of a project. Unused Partnership Service units of time are not normally carried over from one Allocation period to another.

2i2c teams need to assign people to these allocations as part of our regular prioritization process e.g., biweekly P&S iteration planning meeting. It is not necessary to allocate team members to every Community Enablement Service allocation. As long as the overall commitment (usually over a quarter) is met that is sufficient.

The assigned team member should then proactively reach out to the community to remind them they have Community Enablement Service available and how the collaborative support will be offered. This could be by email, or participation in asynchronous Slack workspace, in a community meeting, or a scheduled virtual meeting. The specific details will depend on the nature of work covered under the Partnerships Agreement.
 
Once a team member has provided time towards a Partnership Service allocation, they need to report, by recording the units of time and a brief description of the work performed.  The data that needs to be collected are

- Activity allocation
- Activity team member
- Activity units of time
- Activity description
- Activity date(s)

Activities can be recorded broken down into several entries or reported together in an aggregation. It is the responsibility of the assigned team member to record activity performed within two weeks of the activity.  Line managers should periodically review recorded assignments and provide oversight to ensure this data is being collected.

Using the data available from Allocations and Activities, automatic monthly reports will be generated to provide transparency to Business Development, Delivery Enablement, Product & Services, and our clients are the state and status of each Community Enablement Service offering.

## AirTable Interfaces

AirTable interfaces support the delivery of Community Enablement Service.

### Dashboard Overview

Interface: [Dashboard - Airtable](https://airtable.com/appbjBTRIbgRiElkr/pageGsJuDhaRP53RU)

- A dashboard showing all Allocations and Activities
- This visualization shows the usage of the Community Enablement Service
- This interface aggregates all commitments under Community Enablement Service to track total allocation across the team against a maximum capacity.

### Project Details

Interface: [Project Details - Airtable](https://airtable.com/appbjBTRIbgRiElkr/pagrJZzCMfFwI1W1i)

```{note}
A Project includes Community Enablement Service when the Partnerships Service Allocation string is non-empty. Edit this string in the [Delivery Enablement > Project interface](https://airtable.com/appbjBTRIbgRiElkr/pag0zFFd2NaJHBHN5). 
```

- This is primary interface for recording and managing Activities and Allocations under the Community Enablement Service.
- Each Project has has an Engagment, Project Status, Project Start Date, Project End Date.
- Projects appear in this interface if and only if they have a non-empty Partnerships Service Allocation string.
- Project Description provides context of the scope of activies that expected as part of Community Enablement.

**Allocation Provider (usually P&S Team member)**
- Use this interface to add Activity under the corresponding Allocation period
- This data will be used to generate reports for each project for the Activities used, and report on unused units of time.

**Delivery Enablement**
- Use this interface to create and manage Allocation Periods
- The Allocation Periods are manually created based on the Project Start Date, Project End Date, and the Partnerships Service Allocation

## Activity Reporting

Interface: [All Activity - Airtable](https://airtable.com/appbjBTRIbgRiElkr/pagfFoxonzqRA3QRd)

- For each 2i2c team member, show a table of all Activity with a table to record units of time completed with description of activity, and dates.
- By selecting a particular Project from the dropdown, we can use this interface to generate and export a CSV report of activities associated with this Project. This functionality is not available in the Project Details interface.

