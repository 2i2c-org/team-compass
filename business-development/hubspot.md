(hubspot:index)=

# HubSpot Usage (2026)

## Overview

We use HubSpot as our Single Source of Truth for tracking Deals and related sales motions (e.g. Renewals, prospects, general sales inquiries, etc.).
In late 2025, we decided to migrate away from Airtable to HubSpot. We've kept historical data in Airtable and will be deleting the data in mid-2026.

## Current Process

Below are a common list of processes that are frequently done in HubSpot.

1. Creating a new Deal
2. Adding Contracts to Deals
3. Enriching Deals and Contacts
4. Linking HubSpot to Asana (Engagement Management)

### Creating a new Deal

To learn how to create a new deal, refer to the official HubSpot [Create deals](https://knowledge.hubspot.com/records/create-deals) documentation.

#### Naming Convention

We have adopted the following naming convention for deals: **"[YY] [Company Name]"** (e.g. "26 Mars University")

:::{note}
We chose this approach because it aligns with how CS&S names their contracts in Sage.
:::

#### Data Hygene

Ensure that all the deals have the following fields populated when created:

- **Company** - The company the deal is associated to
- **Line Items** - The Line Items related to the expected deal-type (e.g. General Membership vs Premeir, etc)
- **Deal Value** - This should be automatically populated once the Line Items are populated.

### Adding Contracts to Deals

For deals that are at or past Proposal stage, ensure that there is a link in HubSpot that points to the Shared Google Drive that contains the contract documentation.

This allows us to easily find what agreements were make to successful deliver the contract once the P&S team begins working on delivery.

To update HubSpot, following the steps below:

- **Find the agreement folder**: Navigate to `2i2c <> CS&S Shared` > `Outbound Agreements` folder and find the specific folder that containers the contract documentation for the deal. This is a folder that is owned by CS&S. You'll need to request access from the CS&S Finance team.
- **Find the deal**: Navigate to HubSpot and find the related deal.
- **Link the documents to deal**: Copy that Google Drive URL to the `About this Deal` > `Contract/Statement of Work` HubSpot field.

### Enriching Deals and Contacts

Currently, we use a mix of _manual_ search and _LLM-supported_ intelligence gathering to gather information about institutions and individuals that we'd like to contact via HubSpot.

For the LLM-supported search, we save the prompts in the Asana Sales Playbook.

### Linking HubSpot to Asana (Engagement Management)

We use Asana for [Engagement Management](engagement.md). This is the project management aspect of coordinating delivery.

Each deal needs to be linked to its related Engagement once it get to Closed-Won.

This is done by creating an Engagement in Asana, and then adding that URL to the
`About this Deal` > `Engagement` field in HubSpot.
