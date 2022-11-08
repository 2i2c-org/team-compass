# Sales and invoicing process

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

## Who participates in this process?

Anybody on the core team of 2i2c, or the steering council, is welcome to participate in the process below.
If you wish to help with sales and growing the service, please send an email to `partnerships@2i2c.org` so you can be added to that list, and be given a quick run-down of the process.

All members of `partnerships@2i2c.org` are invited to participate in the process below.

## Tracking leads with AirTable

We use AirTable to track our leads for prospective communities to serve.
: [**This AirTable**](https://airtable.com/appDUEjjcSqHfilFD/tblxLUQ3ElIaaQuM8/viwXstuM3K48smZXW?blocks=hide) keeps track of all potential communities we may serve. Below is an overview of each step in the process.

Status fields indicate each step of the sales process
: We use the **status column** to indicate where a community is in the process. There are a few statuses that a community can have:

  - {guilabel}`Active Lead` is a community that is actively interested in our service.
  - {guilabel}`Inactive Lead` is a potential community that is less-responsive or does not seem interested anymore.
  - {guilabel}`Needs Admin` is a lead that has agreed to a service tier and now needs CS&S to set up administrative infrastructure.
  - {guilabel}`Active Service` is a community for which we have an active service contract.
  - {guilabel}`Inactive Service` is a community that we used to run a service for, but who has since stopped that service.
  - {guilabel}`Waiting` is a community that is interested in our service, but we are intentionally waiting for an extended period of time to follow-up (for example, if they are waiting to learn if they have received a grant).

Fill in information following each status column
: As leads progress through the sales process, we need more information from them, eventually leading to a contract. Fill in this information, and once we reach the next "status" column on the board, we have entered a new phase of the process. At the end of a sale (AKA, once an invoice is sent an paid), all columns of the row should be filled.

## What we need in order to send an invoice

In order to send an invoice to a community, we need a few pieces of information from them:

- **An agreement of the service tier**. We need an email confirmation from them about what service they want, and at a specific price point.
- One of these two things:
  - **An agreement that service has been delivered**. This can be in the form of an email at the end of each month that explicitly confirms with the community representive that the services have been delivered as expected.
  - **A contract that describes delivery of the service**. If the community wants a more fully-specified service description, we can generate a contract with more explicit services offered and timelines. If a contract exists, we can send invoices according to the language in the contract.

For any of these pieces of information, it is crucial that the `operations@codeforsociety.org` email address is forwarded the relevant information and email responses, so that we can archive it!

## Steps in selling new services

These steps roughly follow the entire process of first making contact with a prospective community, to creating an active service for them.

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

  - [**Send them an email confirming their service**](https://docs.google.com/document/d/1BUuk_giDKSADsL8QeKnWonBXmJcpnH5sAER6c8H_yn4/edit?usp=sharing) and clarify any questions they may have
  - **Convert their status to {guilabel}`Needs Admin`**.
  - **Forward the email chain to CS&S `operations@codeforsociety.org`**. Note in the forward that this is confirmation of a new service, and that administrative infrastructure should now be set up.

Set up the service
: Once we've received an email confirmation of a particular service offering, it is time to set up the administrative and technical infrastructure for the service.

  - **The CS&S team will set up the admin paperwork**. They will contact the community we're working with to set up the proper billing channels.
  - [**Create a {guilabel}`New Hub - Request Information` issue**](https://github.com/2i2c-org/infrastructure/issues/new?assignees=&labels=type%3A+hub&template=3_new_hub-request-info.yaml&title=%5BRequest+Information%5D+New+Hub%3A+%7B%7B+HUB+NAME+%7D%7D). Follow the instructions in this issue template and provide a high-level description of this hub, as well as ping the community representative(s) in the appropriate section. This issue is meant to help you guide the community representative(s) and answer their questions in order to empower them to open a [**{guilabel}`💻 New Hub - Request deployment` issue**](https://github.com/2i2c-org/infrastructure/issues/new/choose).
  Feel free to ping the engineering team whenever their input is needed.
  - Conclude the step above by opening and linking a [**new {guilabel}`💻 New Hub - Request deployment` issue**](https://github.com/2i2c-org/infrastructure/issues/new/choose) and add it to the Engineering Team Backlog. This will alert the engineering team that it is time to create a new hub for this community! An engineer will be assigned to the issue in order to deploy this hub.
  - [**Add their hub to the "Active Hubs" AirTable**](https://airtable.com/appDUEjjcSqHfilFD/tbljaAnHkE4Ry8j9J/viwVt9283ZKimUg4o?blocks=hide). This table cross-references the "leads table", so that we can track which hubs are being run for each community.
  - (once the date for beginning service arrives) **Set their status to {guilabel}`Active Service`**. This hub is now actively running!

### Sending invoices

We send invoices to all communities at the end of each month.
We should set up the information and paperwork for each, and then issue invoices in a big batch to streamline the process.
Here's the process for doing this:

- **Start with a list of communities that have an active service.** Use [the Leads AirTable](https://airtable.com/appDUEjjcSqHfilFD/tblxLUQ3ElIaaQuM8/viwXstuM3K48smZXW?blocks=hide) to reference which communities we must invoice.
- **Calculate the monthly cloud spend for relevant communities.** For communities running on shared 2i2c infrastructure, or for whom we are managing cloud billing, we should calculate the amount of cloud spend each has incurred for that month, and add it to the relevant communities from the list above.
- **Add the monthly operations fee for all communities.** This will depend on the type of service for each hub that the community is using.
- **Send an email with this information to `operations@codeforsociety.org`**. Include line-items for the cloud costs and the managed hub fee.
- **CS&S will send an email to certify that the service has been provided.** The community representative must provide an affirmative response that they are satisfied with that month's service.
- **CS&S will send an invoice**. After they have responded positively, CS&S will send the community an invoice for that month's service.

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
