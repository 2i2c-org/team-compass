# Accounting information

Accounting information describes the money that we **know** we have spent or that we **highly expect** to receive.
There are a few kinds of accounting data we have access to:

All 2i2c-specific accounting documents should be accessible on our Team Drive to anybody with a `@2i2c.org` address.
We don't control the access conditions for the CS&S documents described below, so if you don't have access to these, ask the {role}`Executive Director`.

We split our financial and accounting data between two places:

- [2i2c Drive Folder with our finance assets](https://drive.google.com/drive/folders/1D5NQKhPDP6zMQ8EdLcMOceTz-ek81nmX?usp=sharing) contains 2i2c-specific budgeting and modeling information. It is available to all team members.

- [CS&S Drive Folder with their finance assets](https://drive.google.com/drive/folders/115EIa6cD4BNGIqOd2i7Rqu3MgsM73lgR?usp=sharing) contains assets that are stewarded by CS&S. It is available to 2i2c'c executive director.

See these subsections below for more information about accounting data.

(accounting:summary-tables)=
## Accounting summary tables

We have a Sphinx page that summarizes important accounting information for us.
It is generated from the [CS&S accounting statements](accounting:statements) that we get monthly.
You can find this website at the following location:

```{button-link} http://2i2c.org/kpis/finances.html#accounting-tables
:color: primary
Accounting tables
```

(accounting:airtable)=
## AirTable data

We have an AirTable Workspace that is synchronized with several relevant data sources in the CS&S Accounting AirTable Workspace.
It includes information about our active contracts and invoices.
Below is a link to the AirTable, see [](../administration/airtable.md) for how to access it.

```{button-link} https://airtable.com/appbjBTRIbgRiElkr
:color: primary

Accounting AirTable Workspace
```

(accounting:statements)=
## Raw accounting statements

We get monthly accounting reports from our fiscal sponsor, {term}`CS&S`.
These are placed in a shared Google Drive that CS&S controls.

For those with access, you can find the accounting statement folder here:

```{button-link} https://drive.google.com/drive/folders/1vM_QX1J8GW5z8W5WemxhhVjcCS2kEovN?usp=share_link
:color: primary

Financial Statements from CS&S
```

This is a quick guide to understanding the CS&S accounting statements as explained by their team.

The accounting statements represent **realized** income and expenses.
This means that they represent things that have actually happened, not things that _might_ happen in the future (even if they are written into a contract).

There are two relevant tabs to the accounting statements:

### Tab: Account Transactions

An append-only list of every transaction that has been linked to 2i2c.
There are a few relevant columns:

Description
: A free-form description of the transaction. Sometimes this contains information about who paid us, or which contract it was linked to. We can use this to infer important metadata about a transaction.

Reference
: A unique reference number for the transaction. It will begin with `INV-` in the case of invoices for services rendered. This can be useful to cross-reference other transactions that might be linked to that invoice (usually, in the `Description` field).

Debit / Credit
: These are **Costs** like salaries and reimbursement, as well as **Revenue** like grant income and service invoices.

Account
: The type of transaction that occurred. This lets us categorize how we are spending and receiving money. E.g., did we pay for consulting services, did we pay for an online service, did we receive money for contracting, etc.

Grants
: All of our income/expenses are tied to a particular grant, which is encoded here. We have a grant option for every active grant (e.g. the Columbia University Pangeo grant).

  There is a special persistent category called `2i2c: General`. This is a general fund where our contract revenue is placed and spent from. It is essentially "disposable income" with no strings attached.

(accounting:income-statement)=
### Tab: Income statement

The income statement is a summary of our financial situation at a moment in time.
It represents **realized funds**, meaning that **future transactions are not represented here**.
This means that some grant columns will have more realized income than is represented here (for example, when we expect another influx of cash on a multi-year grant).

There are three kinds of columns:

Grant columns
: There's one column for each active grant, that describes the current financial situation on that grant.

`2i2c: General`
: There's a column for 2i2c's persistent general fund (`2i2c: General`).

`FSP: 2i2c`
: The final column has the sum totals _across all of the other columns_. It is the highest-level summary of our financial situation that we've got.

## Common questions and how to answer them

Here are some common questions and how to answer them with the information above.

### How much cash on-hand does 2i2c have?

- Look to the bottom-right cell of the [Income Statement](accounting:income-statement).
- This is the `Net Income` across all of 2i2c's history with CS&S. This number is the amount of disposable cash on hand.

### How much remaining funds should we expect in a grant?

- Find the column for that grant in the latest [Income Statement](accounting:income-statement).
- Find the `Gross Profit` row for that grant.
- Compare this with the total budget that we submitted for the grant (including our FSP fee).
- The difference between the two is the amount we expect to receive in the future.

### What is our burn rate?

- Go to [our budget projections sheet](accounting:projections).
- Look at the `Summary` tab.
- This shows our burn rate, along with 9 and 24 month cutoffs.
