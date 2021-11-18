# Sales, contracts, and invoicing process

This section has information about pursuing and creating new contracts for 2i2c services.

## Location of sales assets and documents

Here are some locations of common documents used in the sales process (other than the repositories described below).

[The Managed Hub Service folder](https://drive.google.com/drive/folders/1QuvUvwFxPAxw-bJ6_zjgwKXPurHC6UfW?usp=sharing)
: Contains all folders and information that cover the Managed Hub Service, including assets for creating new contracts and following leads.

[The leads and partnerships AirTable](https://airtable.com/appDUEjjcSqHfilFD/tblxLUQ3ElIaaQuM8/viwXstuM3K48smZXW)
: An AirTable with the pipeline for potential communities we will serve.
  This table is the source of truth about who we are talking to about serving hub infrastructure, and who we have an active service with.

[The partnerships and leads assets folder](https://drive.google.com/drive/folders/1aMZILBmFSTYBSB9EwyV5wRpcuprM06dJ?usp=sharing)
: Contains all templates, email copy, stationery, etc that is useful in 2i2c sales.

## Steps to create new services and contracts

### AirTable for tracking leads

We use AirTable to track our leads for prospective communities to serve.
: [**This AirTable**](https://airtable.com/appDUEjjcSqHfilFD/tblxLUQ3ElIaaQuM8/viwXstuM3K48smZXW?blocks=hide) keeps track of all potential communities we may serve. Below is an overview of each step in the process.

Status fields indicate each step of the sales process
: We use the **status column** to indicate where a community is in the process. There are roughly five statuses that a community can have:

  - {guilabel}`active lead` is a community that is actively interested in our service.
  - {guilabel}`inactive lead` is a potential community that is less-responsive or does not seem interested anymore.
  - {guilabel}`needs contract` is a lead that has agreed to a service tier but needs a contract set up.
  - {guilabel}`active service` is a community for which we have an active service contract.
  - {guilabel}`inactive service` is a community that we used to run a service for, but who has since stopped that service.
  - {guilabel}`waiting` is a community that is interested in our service, but we are intentionally waiting for an extended period of time to follow-up (for example, if they are waiting to learn if they have received a grant).

Fill in information following each status column
: As leads progress through the sales process, we need more information from them, eventually leading to a contract. Fill in this information, and once we reach the next "status" column on the board, we have entered a new phase of the process. At the end of a sale (AKA, once an invoice is sent an paid), all columns of the row should be filled.

### Steps in selling new contracts

These steps roughly follow the entire process of first making contact with a prospective community, to creating an active service contract for them.

:::{admonition} Always cc `partnerships@2i2c.org`
If you ever send an email related to selling services to communities, cc the `partnerships@2i2c.org` account so that others have visibility.
This will also ensure that our fiscal sponsorship admin team gets the email for their records.
:::

First contact / describe the service
: When others show obvious interest in working with 2i2c, they are now a lead.

  - [**Send them an email describing our services**](https://docs.google.com/document/d/18h4mn2cB96w-jyqFef2x6RmHwbr_wQ8CN1-BK6jFqvQ/edit?usp=sharing) and help them clarify any questions they may have.
  - [**Create a new item in the leads AirTable**](https://airtable.com/appDUEjjcSqHfilFD/tblxLUQ3ElIaaQuM8/viwXstuM3K48smZXW?blocks=hide) and fill in the relevant information for them. Set their status to {guilabel}`Active Lead`.

Confirm a service
: If the prospective community is interested in a particular service, we should confirm the details of that service and move on to the contracting stage.
Send the questionnaire.

  - [**Send them an email confirming their service**](https://docs.google.com/document/d/1BUuk_giDKSADsL8QeKnWonBXmJcpnH5sAER6c8H_yn4/edit?usp=sharing) and clarify any questions they may have
  - **Convert their status to {guilabel}`Needs Contract`** and ensure that `partnerships@2i2c.org` was cc'ed on the email above.

Set up the service
: Once we've received an email confirmation of a particular service offering, it is time to set up the administrative and technical infrastructure for the service.

  - **The CS&S team will set up the admin paperwork**. They will contact the community we're working with to set up the proper billing channels.
  - [**Create a {guilabel}`New Hub` issue**](https://github.com/2i2c-org/infrastructure/issues/new?assignees=&labels=type%3A+hub&template=2_new-hub.yml&title=%5BNew+Hub%5D+%7B%7B+HUB+NAME+%7D%7D). This will alert the engineering team that it is time to create a new hub for this community!
  - [**Add their hub to the "Active Hubs" AirTable**](https://airtable.com/appDUEjjcSqHfilFD/tbljaAnHkE4Ry8j9J/viwVt9283ZKimUg4o?blocks=hide). This table cross-references the "leads table", so that we can track which hubs are being run for each community.
  - **Set their status to {guilabel}`Active Service`**. This hub is now actively running!

### Sending invoices

We send invoices to communities at the end of each month.
Here's the process for doing this:

- (If we are paying cloud costs for the hub), calculate the community's monthly cloud spend so we can include it in the invoice.
- Send an email confirming that the hub service has gone well, along with an invoice for that month's service + cloud spend.
- When they confirm that this looks correct, the CS&S Admin Team will send them an invoice for that month's service.

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
