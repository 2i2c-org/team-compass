(hubspot:index)=

# Customer Relationship Management (CRM)

We use HubSpot as our Source of Truth for tracking Contacts, Organizations, Deals and the relationships that drive each of them through sales. 

:::{note}
We used to use AirTable for this, here's a link to [our old CRM in AirTable](https://airtable.com/appbjBTRIbgRiElkr?). We'll deprecate that in the coming months.
:::

## Current Process

Below are a common list of processes that are frequently done in HubSpot.

1. Creating a new Deal
2. Adding Contracts to Deals
3. Enriching Deals and Contacts
4. Linking HubSpot to Asana (Engagement Management)

To update HubSpot, following the steps below:


### Enriching Deals and Contacts

Currently, we use a mix of _manual_ search and _LLM-supported_ intelligence gathering to gather information about institutions and individuals that we'd like to contact via HubSpot.

For the LLM-supported search, we save the prompts in the Asana Sales Playbook.

### Linking HubSpot to Asana (Engagement Management)

We use Asana for [Engagement Management](engagement.md). This is the project management aspect of coordinating delivery.

Each deal needs to be linked to its related Engagement once it get to Closed-Won.

This is done by creating an Engagement in Asana, and then adding that URL to the
`About this Deal` > `Engagement` field in HubSpot.
