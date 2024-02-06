
(accounting:statements-summary)=
# Overview of CS&S accounting reports

This section describes how to read

For those with access, you can find the accounting statement folder here:

```{button-link} https://drive.google.com/drive/folders/1vM_QX1J8GW5z8W5WemxhhVjcCS2kEovN?usp=share_link
:color: primary

Financial Statements from CS&S
```

This is a quick guide to understanding the CS&S accounting statements as explained by their team.

The accounting statements represent **realized** income and expenses.
This means that they represent things that have actually happened, not things that _might_ happen in the future (even if they are written into a contract).

There are two relevant tabs to the accounting statements:

(accounting:income-statement)=
## Tab: Inception to Date by Activity

The income statement is a summary of our financial situation at a moment in time.
It represents **realized funds**, meaning that **future transactions are not represented here**.
This means that some grant columns will have more realized income than is represented here (for example, when we expect another influx of cash on a multi-year grant).

There are four kinds of columns, in order of appearance:

`Account`
: Accounting category. This is a way for us to track how much money is coming in/out of a given category.
  We generally care the most about `Net Income` at the bottom.

`FSP: 2i2c`
: The first column has the sum totals _across all of the other columns_. It is the highest-level summary of our financial situation that we've got.

Grant columns
: There's one column for each active grant, that describes the current financial situation on that grant.

`2i2c: General`
: Finally, there's a column for 2i2c's persistent general fund (`2i2c: General`).
  This includes any revenue from our hub service, since it is not tied to a grant.

## Tab: Account Transactions

An append-only list of every transaction that has been linked to 2i2c.

This list is broken into budget categories, and each transaction is listed within the category in chronological order.

There are a few relevant columns:

Source
: Describes the overall kind of transaction that has occurred.
  This is the quickest way to determine if a line item is **revenue** or **cost**.
  **Revenues are called `Receivable Invoice`, and costs are called `Payable Invoice`**.

Description
: A free-form description of the transaction. Sometimes this contains information about who paid us, or which contract it was linked to. We can use this to infer important metadata about a transaction.

Net
: This is the amount of the transaction.
  It is always positive, regardless of whether it represents a Revenue or a Cost.
  It is up to us to categorize the transaction accordingly.
  **If it is negative**, this means that the line item has "reversed" a previously-existing transaction.
  There are two primary cases where this happens:

  - If we need to revoke an invoice to a community.
  - When we charge communities for costs that are "Rebillable to customers".
    These invoices don't get categorized as "income", and instead are all lumped in the same "Rebillable to customers" category.

Account Code
: The type of transaction that occurred. This lets us categorize how we are spending and receiving money. E.g., did we pay for consulting services, did we pay for an online service, did we receive money for contracting, etc.
  The code should always correspond to the group of line items that you're currently looking at.

Grants
: All of our income/expenses are tied to a particular grant, which is encoded here. We have a grant option for every active grant (e.g. the Columbia University Pangeo grant).

  There is a special persistent category called `2i2c: General`. This is a general fund where our contract revenue is placed and spent from. It is essentially "disposable income" with no strings attached.
