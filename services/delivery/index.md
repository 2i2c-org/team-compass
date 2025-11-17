(delivery:index)=

# Delivery

In [Sales Operations](sales-operations:index), we describe an broad structure for working with communities:

:::{figure} ../../business-development/images/sales-process.png
Simplified sales process
:::

This section describes what Delivery means for 2i2c.

## Sales to Delivery 

Business Development uses [Hub Spot](https://app.hubspot.com/) as the source of truth for the development of agreements with communities.  In HubSpot, these records are called **deals** and each represents a transaction with a contact or company. Each deal tracks potential revenue through various stages of the sales process until it is marked as won or lost.

:::{note}
HubSpot Deal Stages: Lead, Qualified, Proposal, Negotiation, Contract Admin, Closed Won, Closed Lost
:::

1. The Lead and Qualified stages on BD owned stages. See [link here to sales operations].

2. At the Proposal stage, BD notifies PS if there is a need for additional input or review. This is the stage where the scheduling and capacity requirements for the work should be determined. 

During this stage requests from BD to PS are used to help develop Statements of Work.

:::{warning}
Missing step: Is there sufficient capacity in P&S to deliver on this proposal? Has the communication between BD and PS occurred? 
:::

3. During the Negotiation stage the contractual details are need to be worked out. Specifics like start date, end dates, deliverable dates should be clearly identified during this stage. CS&S/Legal may need to be included in this stage.

There needs to be an artefact (usually, a 'Service Agreement') that is used as the source of truth for deal.

BD should also document what they know about a Community in HubSpot.

:::{note}
# What we want to learn about a community

Here is information BD is asked to provide for P&S to be able to deliver the service. This information should be discoverable from HubSpot.

- Community Short Name (Short version ~1 word)
- Community Long Name (Long version -- full formal name)
- community_id (one word, alphabetic and lowercase,  to use for naming clusters, accounts, database keys, and other infrastructure internal to 2i2c. In most cases this may be a variation of the Community Short Name)
- People contact information (Full name, first name, email address, github ids) with roles assigned for this engagement:
  - Buyers
  - Community Champion(s) / PI(s)
  - Community Representatives
  - Technical Community Leads
  - Technical Contacts
  - Authorized PR Submitters
- Community Website
- Community GitHub organization and representative repos (if applicable)
- Logo (as url)
- Cloud and region preferences (if known). This important to identify early so that infrastructure is deployed close to data and other compute resources.

-Service Tier  (Essential, Advanced, Premier)
:::

:::{note}
Community Context questions:

- Q: What do you want to achieve by working with 2i2c? Can you paint me a picture that describes the future you wish to materialize?
- Q: Can you describe this research community more? Is it segmented? Are there archetypes or personas?
- Q: At a high level, what is your community trying to achieve and how open data/compute infrastructure will help advance toward your mission/vision?
- Q: Can you describe the data? Collaborating open science communities orbit around the heaviest objects in their science space -- their data. Where is it?
:::

5. To reach the Contract Admin stage, the Lead needs to be verbally closed. CS&S is requested to collect the signatures on the Service Agreement.  CS&S sets up SAGE to prepare for invoices.

A Deal move out of Contract Admin when two conditions are satisfied:
- There is a fully executed (signed by all parties) Service Agreement or Purchase Order to complete the work described in the Deal.
- BD requests PS to start Delivery on hub deployments and interaction with the community. Outcomes of this request will be

  - create the Engagements, Project, and Deliverables to manage the project.  

  - create new columns in the cloud billing spreadsheet for this new deal.

BD uses the Order concept within HubSpot to initiate the request for Delivery.  We use n8n to automate the information transfer between HubSpot and GitHub/Airtable. 

:::{warning}
We are trying to automate using n8n but this does not yet capture everything about a Deal to guarantee delivery. It remains important for information held within BD about related to the Deal to be transferred to PS.

We need to build structures and system so that BD can verify the delivery by PS has been completed successfully. 
:::

:::{note}
# Engagements, Projects, and Deliverables



:::

6. Closed Won. The Sales phase of the deal has concluded and we move into the Delivery phase. 

## Delivery to Renewal

During the Delivery phase, 2i2c completes the work as defined in the Service Agreement or Purchase Order agreed to in the Deal.  We call the overall scope of work an **Engagement**.

The goal of an Engagement is to provide value to our communities.  

:::{note}
There is a 1:1 correspondance between a Deal in HubSpot and a **Engagement** as described in this section. 
:::

:::{attention}
We are using AirTable to project and delivery management of our engagements. We use GitHub to manage our task level activities using GitHub Projects. We recognize that neither software platform is ideal for our needs and remain open to suggestions for considering a different implementation.
:::



## Cloud Budget Alerts

On AWS, we set up Budget alerts to trigger actions (sent to support+<commuity>@2i2c.org) when the budget threshhold is exceeded.


## Renewal

At 60 days before the end of an Engagement, a AirTable automation triggers an "Agreement expiring in 60 days" email to partnerships@2i2c.org



```{toctree}
premier-tier
advanced-tier
essential-tier
```