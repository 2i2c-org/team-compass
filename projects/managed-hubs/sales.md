# Leads, sales, and hubs process

2i2c pursues new collaborations and contracts via following-up on leads for those who may be interested in 2i2c services.
This page has information to help guide this process.

:::{admonition} Out of date!
:class: warning
The information on this page is out of date, and will be updated once we complete our onboarding with {term}`CS&S`.
:::

## Location of sales assets and documents

Here are some locations of common documents used in the sales process (other than the repositories described below).

[The Managed Hub Service folder](https://drive.google.com/drive/folders/1QuvUvwFxPAxw-bJ6_zjgwKXPurHC6UfW?usp=sharing)
: Contains all folders and information that cover the Managed Hub Service, including sales and contracting.

[The leads folder](https://drive.google.com/drive/folders/1msuG0xWPbawMwesD8LZxdMClP-GVpgT2?usp=sharing)
: Contains a folder for each lead that 2i2c is currently engaging. This is where we store client-specific information, such as price quotes or contracts that have been sent to them.

[The sales assets folder](https://drive.google.com/drive/folders/1aMZILBmFSTYBSB9EwyV5wRpcuprM06dJ?usp=sharing)
: Contains all templates, email copy, stationery, etc that is useful in 2i2c sales.

## The Leads to Sales workflow

### Overview

We use `Monday.com` to track our leads
: [**This Monday Board**](https://icsi-company.monday.com/boards/1140216585) keeps track of all leads in the sales process. Below is an overview of each step in the process.

Status fields indicate each step of the sales process
: We use Monday **status fields** to indicate where we are in the leads process. For example, a new lead is in the "Send Questionnaire" status of the "Triage Phase". This means that the next action is to send them a questionnaire.

Fill in information following each status column
: As leads progress through the sales process, we need more information from them, eventually leading to a contract. Fill in this information, and once we reach the next "status" column on the board, we have entered a new phase of the process. At the end of a sale (AKA, once an invoice is sent an paid), all columns of the row should be filled.

### Triage stage

The first stage is to understand whether an interested party is in-scope for 2i2c, and a good fit for the Managed Hub Service.

Create a lead
: When others show obvious interest in working with 2i2c, they are now a lead. [**Create a new item in the sales pipeline**](https://icsi-company.monday.com/boards/1140216585) and fill in the relevant information for them (everything up to "triage status").

Send the questionnaire
: To understand whether a lead is a good fit, we've created [a short questionnaire](https://forms.gle/VFzs364iNrJgKnKu9) for them. Send a link to the questionnaire.

Create a Lead Folder for them
: As soon as a lead responds to the questionnaire, create a folder for them [in the leads folder](https://drive.google.com/drive/folders/1msuG0xWPbawMwesD8LZxdMClP-GVpgT2?usp=sharing). Use this to store any lead-specific information, such as price quotes and contracts.

Decide if they are in-scope
: If the lead is in-scope, then set the Triage status column to "In Scope" and move on to the negotiation stage.

### Negotiation stage

The negotiation stage is where we understand a bit more about what the lead needs and whether we'll be able to provide it. For example, do they want something really custom that goes beyond our standard Managed Hub distributions? If so, they might be a "development lead" rather than a "managed service lead".

Create a quote
: Create a lead-specific copy of the [pricing sheet template](https://docs.google.com/spreadsheets/d/10Gxufgmiuhq2Up69a6NdQoRs0xgKOi1Jts66wwiqF50/edit#gid=832336436) as well as the [price quote template](https://docs.google.com/document/d/1wxIKBzx0pYYVHWK6hnyYIvGRWpifU9vSHUI3ExWN8DI/edit?usp=sharing). Using the pricing sheet, and the answers from their questionnaire, create a price quote for them about the service.

Send a quote
: Once you've generated a quote for them, send them the modified Price Quote Template, along with a link to the [Managed Service Plan](https://docs.google.com/document/d/1Ka7tgJe7HR8EmS_MMakrYztgfkJT_iFksPsWHdQBqhM/edit?usp=sharing).


  :::{warning}
  At this point, ICSI should be notified of the lead, because we have sent a specific price quote. This _should_ be automated with Monday.com.
  :::

Negotiate on a price
: We may require a few back-and-forths to clarify the needs of the lead and arrive at a specific number and date for service. Modify the Price Sheet as well as the Price Quote template as-needed throughout these conversations. If a customer agrees to a quote, we then send them a Contract.

Send them a contract
: Once a customer agrees to a price quote, send them a contract. Notify ICSI contracting as well as ICSI finance that we need to send this contract to the customer. They will prepare the contract in DocuSign and send it to them. Once they sign the contract, put a copy in the lead's folder.

  :::{note}
  This process may involve some negotiation between ICSI admin and the lead. Over time, we should detect common changes that clients want, and consider baking them into our contract language.
  :::

Send an invoice and get to work 🚀
: Once a customer has signed the contract, we may begin work on setting up their hub infrastructure, as well as sending them an invoice. ICSI finance will take care of the latter. We should next focus on setting up their hub.

### The Hub Setup stage

The final step of the Leads and Sales process is to set up a managed JupyterHub for the lead (now, the "client"). To do so, follow the process below:

Create an issue for the client
: We use [issues in the `infrastructure/` repository](https://github.com/2i2c-org/infrastructure/issues) with the [{guilabel}`Hub` label](https://github.com/2i2c-org/infrastructure/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3AHub) to track the progress of each hub we are running.

The New Hub generation process
: Follow the [process defined in the `infrastructure` repo](https://infrastructure.2i2c.org) in creating a new hub for a lead. This will then track the operation and maintenance of the hub.

:::{admonition} To Do: Create a Customer Management system
In addition to tracking our sales / leads, we need to track running hubs and active customers in order to quickly understand their status and respond to their needs.
:::

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
