# Contracts, grants, and invoices

A **contract** defines our formal relationship with any external organizations or people.
We use **invoices** to exchange funds (incoming and outgoing) that are related to contracts.
This section describes where you can find information about our active and past contracts and invoices.

## Grant folders

We use [the 2i2c Team Drive -> `Finances and Accounting -> Grants` folder](https://drive.google.com/drive/folders/1VvER_SxLDKjDYwfXYyEbPX9GN7YlsNpT?usp=sharing) to keep track of any materials related to a grant we are applying for or have received.  We use that same folder to track all of our preparations and materials for grants that we are applying for.

- The [**Active and In Progress**](https://drive.google.com/drive/folders/1Mgio3WQfpXkuuy_i--ioY_9XHIff4cQe?usp=share_link) folder contains any grant that we've received, or that are in the middle of applying for.
- The [**Rejected and Not Submitted**](https://drive.google.com/drive/folders/1BqCYoOvDrkv_f5eYbbrkP_3sHv2M6i7b?usp=share_link) folder contains any grant that we applied for and did not get, or that we started but did not finish.
- The [**Completed**](https://drive.google.com/drive/folders/1BALUGZh2x_LsQuBSMXAfxeryeP9bMleD?usp=share_link) folder contains any grant that we received and have now completed such that no action is needed.

(contracts:active)=
## Active contracts

{term}`CS&S` tracks all of our contracts in an [AirTable](accounts:airtable).
We synchronize this AirTable to our own in the link below, and generate [dashboards to summarize important data](contracts:dashboards).

This table includes both **service contracts** and **grants**.
Each row in this table is a single contract.
Each column is a piece of metadata about that contract.
There may be multiple contracts (rows) for a single community, representing different periods of time that a contract was active.

```{button-link} https://airtable.com/appbjBTRIbgRiElkr/tbliwB70vYg3hlkb1/viwWPJhcFbXUJZUO6
:color: primary

Contracts AirTable
```

### Linked `Invoices` column

Each contract has a list of the invoices that have been billed against it in the **`Invoices`** column.
This list of invoices is in the `Invoices` column.
See below for more context on how we use this.

### `Service Type` column

We have one custom column that we add to the CS&S data, to represent the _type of service attached to a contract_.
For example, whether a contract is for a _research hub_ or an _educational hub_.
The specific categories are still in flux but the goal is to help us break down where our revenue is coming from in [our invoices dashboards](contracts:dashboards).

(contracts:invoices)=
## Invoices

{term}`CS&S` tracks all of our invoices in an AirTable.
We synchronize this AirTable to our own in the link below, and generate [dashboards to summarize important data](contracts:dashboards).

Each row represents a single invoice.
Each column represents metadata about that invoice (for example, the `Type` column encodes whether it is an incoming (`ACCREC`) or outgoing (`ACCPAY`) invoice.

```{button-link} https://airtable.com/appbjBTRIbgRiElkr/tblkmferOITqS2vH8/viwfuamzW4kbaQSSJ
:color: primary

Invoices AirTable
```

### The `Zero ID` column

Each invoice has **a unique identifier in the `Xero ID` column**.
We use [the `Link Invoices` AirTable automation](https://airtable.com/appbjBTRIbgRiElkr/wflPVmcmuMb38DYIW/wtr3oTLWhTJoVns8d) to link each Invoice record to its corresponding Contract using this ID.

### Linked `Contracts` column

Each `Invoice` record is linked to its corresponding `Contract` record via the **`Contracts`** linked field.

(contracts:dashboards)=
## Dashboards

We use an **AirTable Interface** to summarize important information about our contracts and invoices.
It should be relatively self-explanatory, with section headers describing the primary question each group of graphs is meant to answer.
Each graph should also have a title and subtitle describing its meaning.

```{button-link} https://airtable.com/appbjBTRIbgRiElkr/pagDRzpzpmKVNncH7
:color: primary

Invoicing and contracts dashboard
```
