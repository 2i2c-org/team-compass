# Sales and running hubs process

2i2c pursues new collaborations and contracts via following-up on leads for those who may be interested in 2i2c services.
This page has information to help guide this process.

## Overview of workflow

**We use two repositories to track leads / customers**
: - [**`2i2c-org/leads`**](https://github.com/2i2c-org/leads). Information about all leads and sales that might lead to a new contract or sub-award.
  - [**`2i2c-org/hubs`**](https://github.com/2i2c-org/hubs). Information about *currently running hub deployments* to keep track of our running hubs and divide responsibility between them.

**Each lead gets an issue**
: We use a GitHub issue to track the progress of each lead (created when we are reasonably sure the lead is worth following-up on).
  We track leads in issues within the [`leads/` GitHub repository](https://github.com/2i2c-org/leads), using the {guilabel}`lead` tag.

**Leads each have a stage on the project board**
: We keep a high-level view of all leads [at this project board](https://github.com/2i2c-org/leads/projects/1). This board gives an overview of where we are in the follow-up process for each lead.

**Each lead gets a Drive folder**
: Once we create any kind of asset attached to a lead (e.g., a budget, SOW, or notes from a meeting), create a folder for them. These exist in the `sales/leads/` folder of the 2i2c Google Drive.

  - The [`leads/` folder](https://drive.google.com/drive/folders/1zBXL0X3S28W6iNAshBMaXF7gSpvnXa83?usp=sharing) contains information about prospective customers.
  - The [`customers/` folder](https://drive.google.com/drive/folders/1UNmsJAiJTsb8hxCM1RJjFU_plnuOm-bC?usp=sharing) contains information about those who are paying us for services.

**The lead questionnaire helps triage and estimate work**
: We gather the most structured and useful information for our leads using [the leads generation questionnaire](https://docs.google.com/forms/d/1KHw-4Wdyoofv-6CENeiOSbnC62LKdx55QTcZmXQVkkc/edit?usp=sharing). This should have questions that allow us to gather the information noted in [](sales:questions-to-answer).

  As a part of the triage process, we'll send a lead a link to this questionnaire. Their responses should be linked in the GitHub issue for that lead.


## Lead generation workflow

1. Make contact with a lead, if it is worth following-up on, [**create an issue in `leads/`**](https://github.com/2i2c-org/leads/issues/new?assignees=&labels=lead&template=new-lead.md&title=%5BLead+org+%2F+Lead+person%5D+-+%5BLead+title%5D).
2. Follow the checklist in that issue to follow-up on the load.
3. If the lead converts into a customer, [create an issue in the `hubs/`](https://github.com/2i2c-org/hubs/issues/new?assignees=&labels=&template=new-hub.md&title=%5BLead+org+%2F+Lead+person%5D+-+%5BLead+title%5D)
4. Complete the checklist in the `leads/` issue, and begin work on the checklist in the `hubs/` issue.


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
