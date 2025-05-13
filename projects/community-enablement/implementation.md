# Implementation

## Service Blueprint

[Service Blueprint (Miro)](https://miro.com/app/board/uXjVIdLC25c=/)

```{figure} images/blueprint.png
The service blueprint describes the stages of interaction between a community and 2i2c.
```

## Broad overview

1. Business Development (BD) identifies opportunity
2. Partnerships and Service (P&S) Area Lead confirms capacity and expertise.
3. BD encodes offer in proposal using a SoW template.
4. Delivery Enamblement (DE) creates Engagement, Projects, and Allocations in Airtable.
5. P&S assigns allocation provider for biweekly iteration planning.
6. Allocation provider initiates contact with community.
7. Allocation provider performs work and tracks effort in Airtable.
8. Monthly reports generated automatically for oversight by all stakeholders.

## Detailed Process 


```{attention}
This is more verbose description of the implementation described in [Overview](overview) and is intended to be understood in conjuction with the Service Blueprint.
```

1. 2i2c Business Development decides to offer Community Enablement to prospective customers. This offer should be made if a community will benefit from an active collaboration with 2i2c to achieve a shared objective or outcome that collaboration requires the allocation of specific individuals from our team. This is usually part of a broader membership tier but may be sold as a separate add-on service.

2. During the negotiation phase, Business Development needs to make explicit what a community should expect from 2i2c while allowing 2i2c to continue to sustainably manage its capacity. 

    1. The offer needs to be encoded in a proposal in the form of a service agreement with a [Statement of Work](scenarios).
    2. These details are required to ensure successful delivery of the service.

| Section                     | Details                                                                                  |
|--------------------------|----------------------------------|
| **Description of Services** | Description of the nature of the partnership, objectives, or intended outcomes. The language used in this section will be reused in the reporting of Community Enablement Service. |
| **Budget/Expected # of Hours (if applicable)** | Use the general pattern of “Up to {xx} hours / {time period} by {2i2c team or role providing the service}”. |
| **Other Terms (if applicable)** | Hours available for {shared objectives or outcome} reset at the start of each {quarter (Jan 1, Apr 1, Jul 1, Oct 1)}. Additional time can be purchased at a rate of ${xx} / hour [up to a maximum of {xx} hours]. |

3. BD may assume that sufficient capacity exists within P&S if the total requested capacity over all projects will not exceed P&S Team Capacity on average during the requested period. This information is contained in the Community Enablement Service report which is generated automatically:

```{figure} images/total_commitment.png
Placeholder example of total committed capacity. See monthly report for real data.
```

4. P&S Team Capacity is set by the P&S Area Leads. Within this capacity limit, BD may safely make commitments on behalf of 2i2c. If the capacity limit is exceeded, BD should seek confirmation from a P&S Area Lead that sufficient capacity will be available.

5. If the “nature of the partnership, objectives, or intended outcomes” is the same as a currently active engagement, BD can assume that the expertise exists within P&S to deliver the service. 

6. If the “nature of the partnership, objectives, or intended outcomes” is new, or not currently being offered in a currently active engagement, BD should seek confirmation from a P&S Area Lead that sufficient expertise exists to deliver.

7. Once a Deal has converted to Closed-Won, BD, with the support of Delivery Enablement, needs to ensure the following steps have been taken:

    1. The Deal is updated in the CRM with to have the status of ‘Closed-Won’
    1. A new Engagement record is created in Airtable with the following information:
        - Engagement name – a combination of the community name, engagement start year, and engagement title.
        - Engagement start date
        - Engagement end date
        - Engagement description – a description of the overall scope and nature of the engagement. When applicable, this simply the Membership Tier (Essential Tier, Advanced Tier,  Premier Tier). The first line in the description needs to be a one line title.
        - Community – name of the customer’s organization or suborganization that 2i2c should refer to as the primary beneficiary of the Community Enablement Service. This may be different from the buying organization especially if a 2i2c has been contracted through a third party management service or a university.
        - Link to the signed service agreement
        - Administrative and Technical Contacts information (name, email, GitHub id, phone number, organization, position title) of one or more persons from the community who are the primary points of contact for delivering the Community Enablement Service
        - If multiple contacts are known, clearly mark their roles as
            * Administrative Contact – individuals responsible for the agreement; the “buyer” or leadership role from the customer’s side; included in partnerships service reporting
            * Technical Contact – individuals responsible for coordinating with 2i2c in the implementation of the project; detailed knowledge of project details; the person(s) P&S should contact directly to advance the project; included in partnerships service reporting
            * Billing Contact - individuals responsible for the purchasing or paying invoices from CS&S; not included in partnerships service reporting
    1. A new Project associated with this engagement is created in Airtable with the following information:
        - Project name – combination of community name and project title
        - Project start date
        - Project end date
        - Project description – Description of the nature of the partnership, objectives, or intended outcomes. The first line in the description needs to be a one line title.
        - Community Enablement Service Capacity allocations: “Up to {xx} hours / {time period}”
        - Additional Projects may be created as needed with different dates, outcomes, or capacity allocations
    1. The Engagement is marked ‘Active’.
    1. Completion of this process indicates that an engagement has been ‘handed off’ from Business Development to Delivery Enablement/Product and Services for delivery.

8. In the biweekly Project Management meeting, all active engagements and projects should be reviewed for status and progress. 
    1. Definitions of Engagement status
        1. An engagement is ‘ On Track (Green)’ if all of its projects are well defined and scheduled to be completed are expected to be completed within their respective due dates.
        16. An engagement is ‘Monitor/At Risk (Yellow)’ if there are projects that are not fully refined or the dates are not clear. This is the starting point for any engagement when first created because at least some manual refinement is required. ‘Monitor/At Risk’ also may indicate that we are getting to the end of the engagement period and renewal is required.
        17. An engagement is ‘Action Needed (Red)’ if the deliverable due dates are going to be missed or exceed the duration of the project. This status indicates that, without intervention, we are going to not meet one or more of our deliverables. ‘Action Needed’ also may indicate we are still providing services and spending money beyond the contract period. We need to force a resolution such as a renewal of service contract, renegotiate the terms of the agreement, or decommission infrastructure.
    1. For each project that has a Community Enablement Service as a component, a deliverable should be created that corresponds to each capacity allocation: “Up to {xx} hours / {time period}”. Each deliverable represents an allocation of 2i2c’s overall capacity.  
        1. Delivery Enablement is responsible to the creation of the individuals deliverable allocation (or allocation for short) in Airtable (automatable)
        1. Each allocation will correspond to a P&S initiative that can go on to the P&S project board.  (automatable)
        2. An allocation needs to have the following information:
            * Allocation start date
            * Allocation end date
            * Hours available
        1. An allocation is completed when either the allocation end date has passed or the hours available have used up.  Hours do not roll over from one allocation to the next.
    1. The work in creating and updating the Engagements / Projects / Deliverables can occur asynchronously, but it is during the biweekly Project Management meeting that any ambiguity or scheduling conflicts should be resolved. It is the responsibility of the Delivery Manager to verify that deliverables on being scheduled to be completed by their internal due dates. If a deliverable is anticipated to be not completed on time, its engagement’s status to be elevated to ‘Action Needed (Red)’

9. An allocation goes on the ‘Upcoming P&S Initiatives’ at least two iterations before it is scheduled to start.  (automatable)
    1. P&S Area Leads need to review the list of all upcoming P&S initiatives to make decisions on relative priority and ordering across all deliverables.  
    1. Allocations need to have a specific individual assigned to the allocation. This individual is the Allocation Provider.
    1. P&S Area Leads are responsible for ensuring that allocation has been assigned (likely balancing between capacity and capability across the team)
    1. P&S Area Leads are responsible for pulling an allocation onto the “P&S Initiatives in flight” column in the project board. If there is insufficient capacity in the P&S team this information should be raised in the biweekly Project Management meeting so the information can be communicated to Delivery Enablement and the Business Development.

10. Once an allocation is moved over to “P&S Initiatives in flight”, the allocation provider is responsible for championing the initiative.  This process is:
    1. (task) An initial ‘refinement task’ to orient the allocation provider to the Project and to create the subsequent issues needed throughout the allocation period.

    2. (task) Email the Technical Contact (s) on the project introducing yourself and reminding the community that they have an allocation of 2i2c’s capacity up to {xx} hours over the next allocation period.

    3. (tasks, repeated) create GitHub issues that represent the units of work you are doing with or on behalf of a community within each iteration
        1. Meeting with the community is a task
        2. Implementing or researching a technical feature is a task
        3. Each task should have a corresponding due date and estimated number of points. 
        4. Tasks can be placed into ‘Refined’ or ‘Up next’ to be scheduled in an upcoming iteration as appropriate.
        5. Tasks may be created as needed should have the parent as the Delivery Allocation. (Limitations within GitHub may require creating duplicate tasks as placeholders since each issue can only have one parent)
    4. (task) Reporting and Request for Feedback. Review the work done over the allocation period and verify that the information has been transferred to the Airtable:
        - Allocation providers are responsible for using the Airtable reporting tool to account for the hours spent.  
        - Reporting does not have been aligned with PS iterations if that doesn’t make sense for the project.
        - The description will used in reporting back to the community
        - Reporting should be updated every two weeks and not left to the very end of the allocation period.The community and business development will be using this tool to lookup ‘how many hours do I have left’
        - This task should be scheduled in the last iteration of the allocation period and include an email to the community;
    5. It is not necessary to have an issue for every iteration contained within an allocated period.  If no work is planned with a community during an iteration, there should not be a corresponding card in Committed. Unplanned and Emergency tags should be used when work is pulled in after iteration planning.

```
To: Technical Contacts; Cc: Administrative Contacts. 

Dear {Community or names if known}. 

I’ve been assigned by the 2i2c Product and Services team to provide additional support to your community (up to {xx} hours}) between {Allocation start date} and {Allocation end date}. 
 
I am looking forward to collaborating with you on {Project Objectives and Outcome} for {Community Name}.  

{
Describe provider’s availability and preferred methods of contact during the allocation period.  
May be some variation of:
- Would you like to schedule a meeting with me to discuss changes to your image environment?
- I plan on attending the community meetings A, B, C on these dates and time
- I’ll be active in this Slack channel if you need additional support during this period.
- Or something else that describes how the provider is making themselves available to the community or what you intend to be doing on the community's behalf
- Identify periods of time during the allocation period where you are not likely to be available.
} 

Thank you and looking forward to working with {Community}

{Allocation Provider}
```

```{figure} images/interface.png
```

```
To: Technical Contacts; Cc: Administrative Contacts, cc: 2i2c Business Development. 

During {Allocation Period start date – end date}, I have been collaborating with {Community Name} on {Project Objectives and Outcome} 

{Link to Community Enablement Service Report}

{Request for feedback: Please fill out this Google Form regarding the value received by your community from 2i2c (tie in here to CSAT tool)}

{[If you are no longer assigned to this project after this iteration] Thank you for the opportunity to work on this project. In this next period my colleague, {name}, will be in contact with you regarding their availability.} 

{[If you are are assigned to this project in the next iteration] 

Describe provider’s availability and preferred methods of contact during the next allocation period.  Could some variation any of:
- Would you like to schedule a meeting with me to discuss changes to your image environment?
- I plan on attending the community meetings A, B, C on these dates and time
- I’ll be active in this Slack channel if you need additional support during this period.
- Or something else that describes how the provider is making themselves available to the community or what you intend to be doing on the community's behalf
- Identify periods of time during the allocation period where you are not likely to be available. }

{Optional: Business Development may have a call to action here such as a request for a renewal}

2i2c is pleased to continue to work with {Community}

{Allocation Provider}
```

11. Community Enablement Service Reporting.  
    - https://github.com/2i2c-org/partnerships-reporting
    1. Aggregated reporting across all engagements.  An automated report (MyST based) creates a dashboard that can be used across 2i2c to see the status of the Community Enablement Service
        - Measuring allocated capacity
        - Measuring cost of the service
        - Measure usage of service by communities
        - Static reports can be generated monthly (uploaded as PDF to GDrive)
        - Dynamically generated data updated daily as website available to internal to 2i2c
    2. Per engagement reporting. An automated report (MyST based) to report on activity done per month or per allocation period.
        - Used for reporting back to the community what has been accomplished and what remaining capacity is still available.
        - Community Enablement Service is a prepaid model so it is not expected that there will be an invoicing component that involves CS&S.
        - Per engagement reports are intended to be supplementary material sent out as a component out as part of a monthly 2i2c usage report that will also cover MAUs, hub configurations, cloud costs, and invoicing.  
        - Static PDF reports generated monthly (uploaded as PDF to GDrive)
        - No dynamic or website site access to per engagement reports.