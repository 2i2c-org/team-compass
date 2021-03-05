# Leads, sales, and hubs process

2i2c pursues new collaborations and contracts via following-up on leads for those who may be interested in 2i2c services.
This page has information to help guide this process.

## Overview of workflow

We use two repositories to track leads / customers
: - [**`2i2c-org/leads`**](https://github.com/2i2c-org/leads). Information about all leads and sales that might lead to a new contract or sub-award.
  - [**`2i2c-org/pilot-hubs`**](https://github.com/2i2c-org/pilot-hubs). Information about *currently running hub deployments* to keep track of our running hubs and divide responsibility between them.

See the [`pilot-hubs/` operations guide](pi:operate:team-process) for more information on the technical side of setting up a hub.


### Lead generation and triage

Creating a lead
: Often people will contact us just to ask questions and learn more. When they show obvious interest in working with 2i2c, they are now a lead. [**Create an issue in `leads/`**](https://github.com/2i2c-org/leads/issues/new?assignees=&labels=lead&template=new-lead.md&title=%5BLead+org+%2F+Lead+person%5D+-+%5BLead+title%5D) and follow the checklist in that issue to follow-up. (a short overview is below)

Each lead gets an issue
: We use [issues in the `leads/` repository](https://github.com/2i2c-org/leads/issues) to track the progress of each lead. [Use this issue template](https://github.com/2i2c-org/leads/issues/new?assignees=&labels=service%3Ahub&template=new-hub-service.md&title=%5BLead+org+%2F+Lead+person%5D+-+%5BLead+title%5D) for new "hub as a service" leads. Follow the instructions in the template.

Leads each have a stage on the project board
: We keep a high-level view of all leads [at this project board](https://github.com/2i2c-org/leads/projects/1). This board gives an overview of where we are in the follow-up process for each lead.

Each lead gets a Drive folder
: Once we create any kind of asset attached to a lead (e.g., a budget, SOW, or notes from a meeting), create a folder for them. These exist in [the `sales/leads/` folder of the 2i2c Google Drive](https://drive.google.com/drive/folders/1zBXL0X3S28W6iNAshBMaXF7gSpvnXa83?usp=sharing).

### Converting leads into sales

The leads questionnaire helps triage and estimate work
: We gather the most structured and useful information for our leads using [the leads generation questionnaire](https://docs.google.com/forms/d/1KHw-4Wdyoofv-6CENeiOSbnC62LKdx55QTcZmXQVkkc/edit?usp=sharing). This should have questions that allow us to gather the information noted in [](sales:questions-to-answer).

Use the pricing assets to quote a price
: See the [issue template for lead generation](https://github.com/2i2c-org/leads/issues/new?assignees=&labels=service%3Ahub&template=new-hub-service.md&title=%5BLead+org+%2F+Lead+person%5D+-+%5BLead+title%5D) for links to these documents.

  :::{warning}
  Once we quote an actual price for somebody, it is time to start looping our contracts   and administration team into the conversation. This process is still undefined, and   this section should be added once we understand it.
  :::

Once a customer agrees to work with us at a price, begin the contracting process
: After a lead agrees to work with us, they become a customer. We must coordinate with our contracts team to generate a contract for them, and potentially set ourselves up as a vendor in their system. Once this is finished, we can start sending monthly invoices.

  :::{admonition} To Do
  :class: warning
  We need to define the contract / vendorization process with our contracts team and the customer organization.
  :::

### Converting sales into hubs

Each hub gets an issue
: We use [issues in the `pilot-hubs/` repository](https://github.com/2i2c-org/hubs/issues) with the [{guilabel}`Hub` label](https://github.com/2i2c-org/pilot-hubs/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3AHub) to track the progress of each hub we are running.

The New Hub generation process
: Follow the [process defined in the `pilot-hubs` repo](pi:operate:team-process) in creating a new hub for a lead. This will then track the operation and maintenance of the hub.

## Tips and FAQs

(sales:questions-to-answer)=
### When to decide to work with a lead

To decide whether we should continue engaging with a particular lead, we need to know whether they are in-scope for our mission and likely to be able to successfully collaborate with us.
The [`MANIAC-T` framework](https://xxiibrands.com/sales/qualify-your-sales-leads-with-maniac-t/) can be helpful in coming to a decision. Here is a short description of these guideilnes:

* **Money**. Is there a specific amount of money set aside for the project? If they are seeking funding in order to pay for this, what are the details?
* **Authority**. Does the contact have the authority to make a buying decision? Who else will need to be involved in the decision-making process?
* **Need**. What are their clear pain-points with their current infrastructure setup? Do they seem to have a real need for change?
* **Impending Event**. Do they have an upcoming event that is urgent or pressing?
* **Application**. Is their use-case a good fit for 2i2c infrastructure? Would their use-case require major changes to our hubs? Is there a different organization better-suited to help them?
* **Competition**. What alternative options are they considering? e.g., other organizations, internal approaches, or deciding to do nothing?
* **Timeline**. What does the buying process look like for this prospect? E.g., finalizing a contract, or receiving a sub-award.

## Resources for running the hub

See [the team SRE guide](sre.md) for our resources and process around running a hub.