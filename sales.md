# The leads and sales process

2i2c pursues new collaborations and contracts via following-up on leads for those who may be interested in 2i2c services.
This page has information to help guide this process.

(sales:questions-to-answer)=
## Questions to answer

To decide whether we should continue engaging with a particular lead, we need to know whether they are in-scope for our mission and likely to be able to successfully collaborate with us.
The [`MANIAC-T` framework](https://xxiibrands.com/sales/qualify-your-sales-leads-with-maniac-t/) can be helpful in coming to a decision. Here is a short description of these guideilnes:

* **Money**. Is there a specific amount of money set aside for the project? If they are seeking funding in order to pay for this, what are the details?
* **Authority**. Does the contact have the authority to make a buying decision? Who else will need to be involved in the decision-making process?
* **Need**. What are their clear pain-points with their current infrastructure setup? Do they seem to have a real need for change?
* **Impending Event**. Do they have an upcoming event that is urgent or pressing?
* **Application**. Is their use-case a good fit for 2i2c infrastructure? Would their use-case require major changes to our hubs? Is there a different organization better-suited to help them?
* **Competition**. What alternative options are they considering? e.g., other organizations, internal approaches, or deciding to do nothing?
* **Timeline**. What does the buying process look like for this prospect? E.g., finalizing a contract, or receiving a sub-award.

## Location of information for leads / customers

### Each lead gets an issue

We use a GitHub issue to track the progress of each lead (created when we are reasonably sure the lead is worth following-up on). 
We track leads in issues within the [`meta/` GitHub repository](https://github.com/2i2c-org/meta), using the {guilabel}`lead` tag.
We keep a high-level view of all leads [at this project board](https://github.com/2i2c-org/meta/projects/2).

### Each lead gets a folder

We create a folder for each lead / customer. These exist in the `sales/` folder of the 2i2c Google Drive.

- The [`leads/` folder](https://drive.google.com/drive/folders/1zBXL0X3S28W6iNAshBMaXF7gSpvnXa83?usp=sharing) contains information about prospective customers.
- The [`customers/` folder](https://drive.google.com/drive/folders/1UNmsJAiJTsb8hxCM1RJjFU_plnuOm-bC?usp=sharing) contains information about those who are paying us for services.

These folders will have all relevant materials for that specific lead (e.g., a budget, statement of work, any documents they've sent us, etc).

### The leads questionnaire

We gather the most structured and useful information for our leads using [the leads generation questionnaire](https://docs.google.com/forms/d/1KHw-4Wdyoofv-6CENeiOSbnC62LKdx55QTcZmXQVkkc/edit?usp=sharing). This should have questions that allow us to gather the information noted in [](sales:questions-to-answer).

As a part of the triage process, we'll send a lead a link to this questionnaire. Their responses should be linked in the GitHub issue for that lead.

## Checklist for new leads

Once someone or a team is interested in 2i2c, we should do the following things:

1. Set up a short meeting (or email if they prefer) to understand their general use-case and needs. If they seem like they're in-scope for 2i2c, proceed with the next steps.
2. Create a new GitHub issue for the lead [by using this issue template](https://github.com/2i2c-org/meta/issues/new?assignees=&labels=lead&template=new-lead.md&title=%5BLead+org+%2F+Lead+person%5D+-+%5BLead+title%5D)
3. Follow the steps in that issue
4. When work has officially begun on the lead (they have procured funding for and have signed the contract), move their folder to `customers/` and replace the {guilabel}`lead` tag with the {guilabel}`customer` tag.
