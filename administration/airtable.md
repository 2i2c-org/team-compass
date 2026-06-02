(accounts:airtable)=
# AirTable accounts

```{admonition} Mostly deprecated
:class: warning
The only thing we actively use AirTable for is tracking team [salaries and contracts](#airtable:salaries).
Most other historical content in AirTable is no longer maintained.
```

This page covers our AirTable account, how to access it, and what we use it for.

## Read-only access to the AirTable

[Here's a link to our primary AirTable workspace](https://airtable.com/invite/l?inviteId=inv3bBae7WUqQsehA&inviteToken=7689178d3e79af8956d1f5cd958d9d8e63160e86b70c74d2d8bb2502ce665e00&utm_medium=email&utm_source=product_team&utm_content=transactional-alerts).

This is a read-only link, valid for any `@2i2c.org` address.
If you need edit permissions, use the [shared AirTable account](airtable:shared).

(airtable:shared)=
## Edit access to the AirTable

We have a single account on the "Pro" plan of AirTable.
It is the only account with edit permissions.

To access this account, use our [shared passwords account](account:bitwarden) for credentials.

(airtable:salaries)=
## Salaries base

We use a single AirTable base to track team salaries and internal contracts.

[Open the Salaries base](https://airtable.com/appHxyAV6MR1g8e2w/tblhjCAPx1Fb1A0FE/viwAbKQOByVR92C09?blocks=hide).

The base has three linked tables:

People
: Everyone who currently or has historically worked at 2i2c.

Roles / Titles
: Roles and levels at 2i2c with a start/end date and salary, capturing how roles evolve over time.

Contracts
: Internal team contracts that link a person to a role and represent an active contract.

For our salary policy, bands, and benchmarking process, see [](../people/compensation.md).

### How to update roles and contracts

Every year, we update our roles to reflect cost of living (COLA) adjustments and changes to descriptions.
Follow these steps:

- For each role and for each contract that will continue:
- Duplicate it
- Update the Start / End date (usually July 1st -> June 30th of the next year)
- Update the salary / description if necessary
- Link the old item to the new item via the "Renewed by" field in the old item.

## AirTable structure overview

The rest of this page describes an overview of AirTable's structure in general.

## Bases

A base is the highest unit of organization in AirTable.
They are generally categorized by a broad topic that might have a number of related datasets inside.

Each base has three types of elements in it: **data**, **automations**, and **interfaces**.
Each is described below.

### Data

Contain tabular datasets that make up the content in a base.
These are kind of like **databases**, in the sense that they have typed columns, and each row represents a single "record" within that table.

A base usually has **many tables of data**, and these can then be interlinked with one another.

For example, we have [our Contracts table](https://airtable.com/appbjBTRIbgRiElkr/tbliwB70vYg3hlkb1/viwOWxGxMBVmJFwiC) as well as [our Invoices table](https://airtable.com/appbjBTRIbgRiElkr/tblkmferOITqS2vH8/viwNA9Z2UhSchcuvA) in the same base.
This lets us link records in `Invoices` with those in `Contracts` based on a unique ID in each.

#### Views

Views are ways to filter, group, and subset your data for visualizing purposes.
They do not change the underlying dataset, they merely provide a way to look at it a different way.
For example, our [Invoices table](https://airtable.com/appbjBTRIbgRiElkr/tblkmferOITqS2vH8) has two views:

- [**Incoming**](https://airtable.com/appbjBTRIbgRiElkr/tblkmferOITqS2vH8/viwfuamzW4kbaQSSJ) to only show invoices that are for revenue.
- [**Outgoing**](https://airtable.com/appbjBTRIbgRiElkr/tblkmferOITqS2vH8/viwNA9Z2UhSchcuvA) to only show invoices that are for costs.

#### URL structure

The URL structure of data generally looks like this:

```
https://airtable.com/< BASE ID >/< TABLE ID >/< VIEW ID >
```

### Automations

Allow us to perform certain actions on a schedule or repeated after a certain condition.

For example, we have [a Link Invoices automation](https://airtable.com/appbjBTRIbgRiElkr/wflPVmcmuMb38DYIW/wtr3oTLWhTJoVns8d) that automatically links new records of Invoices with their respective Contract every hour.

### Interfaces

Are dashboards that provide quick and visual summaries of the tables in a base.
For example, we have a Monthly Invoices dashboard that summarizes major financial invoicing and contracts activity each month.

### Example screenshot

Below you can see an example of the **Accounting base**, with the three major sections for **Data**, **Automations**, and **Interfaces** at the top.

Below these, you see **multiple tables** corresponding to different kinds of data (Contracts and Invoices, for example).

For the active table, we can see **multiple views** of that table to the left, corresponding to different subsets of data.

![Major sections of AirTable](../images/airtable-major-sections.png)
