# Guide to the 2i2c CRM in HubSpot

This is our team documentation about how we’ve structured HubSpot to be our CRM, and the processes we have for using it. It’s in-flux, so expect the content to change and please suggest edits and make comments.

# How do I?

## Get high-level context for a deal?

Scroll through the “notes” and find one that gives you context about it.

## Choose the name for a deal?

Use a naming convention like `[YY] [Company Name]` where YY is the year the deal will close (e.g. "26 Mars University"). This matches how CS&S Sage contracts are named.

## Find the work plan and progress for a deal?

See the attached Asana project link.

## Find the deliverables we’ve committed to on a deal?

See the attached line items.

## Create a GitHub Sales Issue to a HubSpot Deal?

1. Create the deal in HubSpot.
2. Copy the deal URL.
3. Create an issue in GitHub and select Type “`Sales issue`”.
4. Into the “`HubSpot Link`” field, paste the Deal URL you just copied this will trigger an automation to poplulate the GitHub description.

![alt_text](images/image1.png "image_tooltip")

5. Wait a bit. The GitHub issue URL will automatically propagate to the “sales issue” link in HubSpot via [this Sales Sync Workflow](https://github.com/2i2c-org/data-sync/actions/workflows/sync-sales.yml).
6. Some properties in HubSpot will propagate into GitHub (e.g. Issue title, and several fields that will be added to the issue body).
7. To add your _own_ content to the issue body, put them outside of the HTML comments designating the part of the issue body that this sync overwrites.

## Where are the original contracts for a deal?

From our compass:

- **Find the agreement folder**: Navigate to `2i2c <> CS&S Shared` > `Outbound Agreements` folder and find the specific folder that containers the contract documentation for the deal. This is a folder that is owned by CS&S. You'll need to request access from the CS&S Finance team.
- **Find the deal**: Navigate to HubSpot and find the related deal.
- **Link the documents to deal**: Copy that Google Drive URL to the `About this Deal` > `Contract/Statement of Work` HubSpot field.

## Where

# Reference

These provide reference information for the overall structure of our CRM. They’re intentionally short and to-the-point.

## Entities

Entities are organizations or individuals that we interact with. They are the relationships that _lead to Deals_. Entities are _linked to Deals_.

### Contacts

Individual people. Are attached to organizations (see entities below).

#### Strategic contacts

People that are strategically important to 2i2c. Usually funders, leaders of major customers, etc. We give these people extra attention and strategic-level information.

See the [contacts segments list](https://app-na2.hubspot.com/contacts/242496330/objectLists/views/all?count=25) for various lists of strategic contacts.

This is still in-flux, so it’s OK to edit or change the rules of those lists.

### Companies

#### Funders

We treat funders as a special-case of “Company” in HubSpot. They are distinguished They have their own pipeline, described below. In brief: we move Funders through their “company” pipeline to track _developing the relationship_. When a concrete opportunity for funding has arisen, we create a _Deal_ for it, link it to the company, and track the deal in its own pipeline.

:::{table} Example of funders
:label: tbl:areas-html

<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td><code>NSF</code>
   </td>
   <td>The big organization. This is more like a placeholder for rollups across all NSF related substructure. Enrichment at this level will become a monolith
   </td>
  </tr>
  <tr>
   <td><code>NSF-Program</code>
   </td>
   <td>This is the right level for enrichment. The program level issues CfPs. Enrichment here involves an identification of the mission at the program level, an identification of the program officers.
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>
:::

HubSpot does not allow using a website URL like [https://www.nsf.gov/cise/oac](https://www.nsf.gov/cise/oac) when defining a company. The stuff after the top level domain is stripped. I am using a workaround. Enter a fake url [oac.nsf.gov](oac.nsf.gov) to create the Program level entity “under” the NSF parent.

Deal Cards in the Project Pipeline include some cases where 2i2c is the Prime awardee and other cases where 2i2c is a subawardee and still others where 2i2c is a subawardee of a subawardee of a Prime. Assigning a binary toggle between Prime and Sub might be safe to try.

### Communities

#### Consortia

A sub-type of communities.

### Pipelines for entities

Pipelines for entities are about developing our relationship with them and getting them closer to work with us, fund us, etc.

#### Consortia pipeline

We treat consortia as a special-case of “Community” in HubSpot. They have their own pipeline, described below.

:::{table} Stages in the Consortia pipeline
:label: tbl:areas-html

<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td><code>Sensing</code>
   </td>
   <td>Before the narrative is set (initiatives. LOD-{0,1,..}. 2i2c chooses this work stream)
   </td>
  </tr>
  <tr>
   <td><code>Convening</code>
   </td>
   <td>[narrative, consortia formed]
   </td>
  </tr>
  <tr>
   <td><code>Fundraising</code>
   </td>
   <td>[consortia formed, asks for funding]
   </td>
  </tr>
  <tr>
   <td><code>Proposing</code>
   </td>
   <td>[proposal, closed-won] (or closed-lost)
   </td>
  </tr>
  <tr>
   <td><code>Delivering</code>
   </td>
   <td>[closed-won, closed-won-complete]
   </td>
  </tr>
  <tr>
   <td><code>Closed-Won</code>
   </td>
   <td>Agreement is binding
   </td>
  </tr>
  <tr>
   <td><code>Closed-Lost</code>
   </td>
   <td>This outcome requires post-hoc information gathering.
   </td>
  </tr>
</table>
:::

#### Funder pipeline

TODO: This will eventually change to its own HubSpot object

-

## Deals

### 2i2c Artifacts for Deals

While a deal is being negotiated, documents will need to be created and shared with team members and externals stakeholders. These documents should be stored in the `2i2c Team Drive > Business Development > [Proposals](https://drive.google.com/drive/folders/1kJREO_4QtwcLGsXegVPhjpH8MueBFG_G)` using the same naming convention from above (`[YY] [Company Name]`).

Specifically we want:

1. In business-development Proposals, there is one top-level folder for every type of entity we have in HubSpot (Companies, Communities, Deals)
2. Each optionally has a folder that represents the documents for that entity.
3. Each folder MUST have the same name as the HubSpot entity it corresponds to.
4. Each folder MUST be linked form the HubSpot entity it corresponds to (and this is the source of truth for linkage)

### Views / filters

- **[Missing key data](https://app-na2.hubspot.com/contacts/242496330/objects/0-3/views/350494808/list?noprefetch=) **- Active deals that we must add information to. Here are the criteria we use:
  - A deal marked `Closed - Won` and _not _`Engagement status: Complete`
  - That is missing a `Required` field in the relevant table below.
- The others should be self-explanatory

### Pipelines for deals

::: {warning}
**This applies to all membership pipelines!**
Before moving a Deal to `Contract-Admin` or `Closed-Won` the following conditions must be met:

1. When we create an Asana engagement (see [Engagement Management](/services/delivery/engagement-management.md)), we must link it to hubspot before considering the deal closed-won
2. We must create a "delivery brief" for the engagement that has all the information needed to understand the core objectives of that engagement
3. We must ensure the tasks and sections of the engagement reflect the major milestones and actions in the delivery brief.
4. We must ensure the fields in Asana link back to the correct hubspot record.

:::

#### New Membership Sales

New Membership Sales move through stages involving “sales motions” that have essentially zero overlap with operations until `Closed-Won` stage. After that, onboarding and other delivery steps kick in.

:::{table} New Membership pipeline
:label: tbl:areas-html

<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>% success</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td><code>Enrichment</code>
   </td>
   <td>0
   </td>
   <td>2i2c identifies, researches, and enriches the lead.
   </td>
  </tr>
  <tr>
   <td><code>Outreach</code>
   </td>
   <td>10
   </td>
   <td>2i2c has contacted the lead.
   </td>
  </tr>
  <tr>
   <td><code>Discovery</code>
   </td>
   <td>40
   </td>
   <td>The lead is engaged in learning more about 2i2c.
   </td>
  </tr>
  <tr>
   <td><code>Proposal</code>
   </td>
   <td>60
   </td>
   <td>2i2c has sent a quote. Other stages here include sending the service agreement, answering questions. This stage may need further refinement. I am tempted to add Committing after Proposal
   </td>
  </tr>
  <tr>
   <td><code>Contracting</code>
   </td>
   <td><code>90</code>
   </td>
   <td>Verbal yes, but we have not finished the contracting and engagement setup process. In some limited cases, P&S delivery starts here.
   </td>
  </tr>
  <tr>
   <td><code>Closed-Won</code>
   </td>
   <td><code>100</code>
   </td>
   <td>Agreement is binding
   </td>
  </tr>
  <tr>
   <td><code>Closed-Lost</code>
   </td>
   <td><code>0</code>
   </td>
   <td>This outcome requires post-hoc information gathering.
   </td>
  </tr>
</table>
:::

#### Renewal Membership Sales

Renewal Membership Sales move through stages of “sales motion” that overlap with operations (check-ins, monthly invoicing, support). This pipeline’s stages describe the key milestones in the renewal sales process. Links to operations and information flows between operations and sales need to be developed.

Set T = expected close date.

:::{table} Renewal Membership pipeline
:label: tbl:areas-html

<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>% success</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td><code>Watching</code>
   </td>
   <td>60
   </td>
   <td> [T-365, T-180] Waiting for a future sales milestone, usually because the renewal is a long ways in the future
   </td>
  </tr>
  <tr>
   <td><code>Preparing</code>
   </td>
   <td>60
   </td>
   <td> [T-180, T-90] Renewal is coming up, begin preparing engagement materials for them.
   </td>
  </tr>
  <tr>
   <td><code>Engaging</code>
   </td>
   <td>80
   </td>
   <td>[T-90, T-30] Actively discussing renewal and any adjustments to make, including possible expansions of service
   </td>
  </tr>
  <tr>
   <td><code>Contracting</code>
   </td>
   <td>100
   </td>
   <td>[T-30, T-0] Verbal-yes that they’ll renew. Renewal paperwork shared and processed toward execution.
   </td>
  </tr>
  <tr>
   <td><code>Closed-Won</code>
   </td>
   <td><code>100</code>
   </td>
   <td>Contract signed, Asana link created, Sage ID linked.
   </td>
  </tr>
  <tr>
   <td><code>Closed-Lost</code>
   </td>
   <td><code>0</code>
   </td>
   <td>No contract renewal.
   </td>
  </tr>
</table>
:::

#### Projects Pipeline

This covers any _Deal_ that is not a standard membership or a membership renewal. Ie, any deal that requires a non-trivial amount of coordination and bespoke work for that deal.

:::{table} Projects pipeline
:label: tbl:areas-html

<table>
<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>% success</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td><code>Exploring</code>
   </td>
   <td>0
   </td>
   <td>Exploring whether this is in-scope for a proposal from us.
   </td>
  </tr>
  <tr>
   <td><code>Waiting - New Sale</code>
   </td>
   <td>10
   </td>
   <td>Project equivalent of a “renewal” that we’re waiting to kick-off until we get closer to the previous close.
   </td>
  </tr>
  <tr>
   <td><code>Waiting - Funding Committed</code>
   </td>
   <td>80
   </td>
   <td>For multi-step grants where we need to apply for and receive funds at each step.
   </td>
  </tr>
  <tr>
   <td><code>Qualified</code>
   </td>
   <td>5
   </td>
   <td>For grants we intend to apply for, but are not currently driving proposal writing (e.g. for capacity reasons.
   </td>
  </tr>
  <tr>
   <td><code>Proposal</code>
   </td>
   <td>10
   </td>
   <td>We are actively writing a proposal for this opportunity.
   </td>
  </tr>
  <tr>
   <td><code>Awaiting Decision</code>
   </td>
   <td>15
   </td>
   <td>We’ve submitted our proposal and are waiting on a response.
   </td>
  </tr>
  <tr>
   <td><code>Contracting</code>
   </td>
   <td>90
   </td>
   <td>Verbal yes, but we have not finished the contracting and engagement setup process.
   </td>
  </tr>
  <tr>
   <td><code>Closed-Won</code>
   </td>
   <td>100
   </td>
   <td>Contract signed, Asana link created, Sage ID linked.
   </td>
  </tr>
  <tr>
   <td><code>Closed-Lost</code>
   </td>
   <td>0
   </td>
   <td>No contract renewal.
   </td>
  </tr>
</table>
:::

#### Hand-off between BD and P&S

Once a deal moves to `Contract-Admin`, BD should:

1. Create a related issue on the [BD requests to P&S](https://github.com/orgs/2i2c-org/projects/60) board if there is delivery work that is needed from the P&S team. These issues should be created using the `BD requests to P&S` github issue template.
2. Ensure that a related issue has been created in the Asana [Enagements](https://app.asana.com/0/portfolio/1211914502801258/1211914511709245) board.
3. Meet with P&S to agree when [community on-boarding](/services/interactive-computing/onboard.md) needs to be conducted.

### Fields / properties

:::{table} HubSpot Deal properties
:label: tbl:areas-html

<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>Options</strong>
   </td>
   <td><strong>Required?</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>Close date
   </td>
   <td>[date]
   </td>
   <td>Yes
   </td>
   <td>Is the expected closed date, then updated to the actual close date when Closed-Won
   </td>
  </tr>
  <tr>
   <td>Sage Grant
   </td>
   <td>String
   </td>
   <td>Yes (for closed-won)
   </td>
   <td>The grant name used in Sage. Has the form:
<p>
02NNN: Longer name
   </td>
  </tr>
  <tr>
   <td>Engagement
   </td>
   <td>URL
   </td>
   <td>Yes (for closed-won)
   </td>
   <td>URL to the Asana project for this engagement.
   </td>
  </tr>
  <tr>
   <td>Contract Start / End Date
   </td>
   <td>[dates]
   </td>
   <td>
   </td>
   <td>Is the <strong>expected start/end date</strong>, then <strong>updated to actuals when a contract is signed </strong>in Sage.
   </td>
  </tr>
  <tr>
   <td>Amount
   </td>
   <td>Currency
   </td>
   <td>Yes
   </td>
   <td>The total amount of the contract.
   </td>
  </tr>
  <tr>
   <td>Indirect rate
   </td>
   <td>Percent
   </td>
   <td>No
   </td>
   <td>The indirect rate that CS&S will take on this. If empty, defaults to 15%. Note: CS&S takes 20% on any award attached to federal funding.
   </td>
  </tr>
  <tr>
   <td>Prepaid cloud costs
   </td>
   <td>Currency
   </td>
   <td>No
   </td>
   <td>The part of <code>Amount</code> that is earmarked for cloud costs (ie, that we won’t pass-through because they’ve already paid in regular invoicing).
   </td>
  </tr>
  <tr>
   <td>Prepaid user fees
   </td>
   <td>Currency
   </td>
   <td>No
   </td>
   <td>The part of <code>Amount</code> that is earmarked for active user fees (ie, that we won’t charge because they’ve already paid in regular invoicing).
   </td>
  </tr>
  <tr>
   <td>Amount collected before Sage
   </td>
   <td>Currency
   </td>
   <td>
   </td>
   <td>If this deal started before CSS moved to Sage (~April 2025), this is the amount we know has been invoiced before that happened. We add this to the invoices we find in Sage when calculating how much remains.
   </td>
  </tr>
  <tr>
   <td>Next due date
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>This is to track deadlines like RFP dates.
   </td>
  </tr>
  <tr>
   <td>Engagement status
   </td>
   <td>Not yet started
<p>
In progress
<p>
Complete
   </td>
   <td>
   </td>
   <td>The status of a deal. <code>In progress</code> when a contract begins. <code>Complete</code> when the period of performance is over and we’ve met deliverables.
   </td>
  </tr>
  <tr>
   <td>Renewal status
   </td>
   <td>Will renew
<p>
Renewed
<p>
Did not renew
   </td>
   <td>Yes
   </td>
   <td>Whether we intend to renew this deal. If “Will renew”, this deal <strong>must </strong>be linked to a deal in our renewals pipeline.
   </td>
  </tr>
  <tr>
   <td>Issue - Sales
   </td>
   <td>[link to a github issue]
   </td>
   <td>
   </td>
   <td>For sales that require coordination on github (e.g. grants) this is the link
   </td>
  </tr>
  <tr>
   <td>Proposal materials
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>A URL to a location where proposal materials exist (e.g. a google drive folder)
   </td>
  </tr>
  <tr>
   <td>Added: Days until close. (autocalculated)
   </td>
   <td>(auto-calculated)
   </td>
   <td>
   </td>
   <td>Number of days until the Close date
   </td>
  </tr>
</table>
:::

Deals properties

    Added: Added association labels: `Is funded by`, and `Funds`, for relationships w/ Funders

Company properties

- Added association labels: `Is member of` / `Has members at` for relationships w/ Communities
- Added `Domain / Field` to track more science-aware domains of communities (e.g. geoscience, education)

### Association links

- Link to **deal: Renewal**

### Quotes

- Membership Deals should have associated line items selected from 2i2c’s standard product library as specified in HubSpot
- Quotes can be generated for each deal with text inserted from the line items
- Quotes become web pages with a unique URL that can be shared as links in email messages sent for new or renewal membership sales
- Tracked in the right sidebar of Deals

### Line items

Track units of value / price attached to each deal.

## Contacts

### Association links

- Link to deal: **Buyer**
- Link to **community**: **Community Representative**
- Link to **community**: **Technical Contact**

### Segments

- **[Community Key Contacts Folder](https://app-na2.hubspot.com/contacts/242496330/objectLists/folders?folderId=813455073) **has several key community segments - see the titles for reference.

## Communities

### Properties

- **Number of active deals / contracts: **The number of deals with **Enagagement status: In Progress** linked to this community. Used to get lists of contacts for active communities.

### Association link

- Link to **deal**

## Workflows

**HubSpot Workflows**: These allow us to automate actions in HubSpot. See the [Workflows Page](https://app-na2.hubspot.com/workflows/242496330/view/default) for a list.

**GitHub Workflows: **the [2i2c-org/data-sync](https://github.com/2i2c-org/data-sync) repository syncs HubSpot deal data to “Sales Issues” in GitHub. See [How to create Sales issues](#bookmark=id.kpu3yimlioxu).
