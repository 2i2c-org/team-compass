# Accounting data

Accounting data describes the money that we **know** we have spent or that we **highly expect** to receive.
Our accounting actuals come from **SAGE Intacct**, managed by our CS&S project accountant.

```{button-link} https://docs.google.com/document/d/1iG2USbvccMGeobKpH52j37LZpmeNASKedJrb0mX8R8Y/edit?tab=t.3bpwr6d9dkbg
:color: primary

Accounting infrastructure guide (SAGE Intacct)
```

For visualizations of this data, see our [finance dashboards](#finance:dashboards).

(accounting:statements)=
## Monthly reports and accounting actuals

Each month, CS&S closes the books and updates our [budget projections](accounting:projections) with the latest actuals.
See [the monthly process](monthly-process.md) for how this works.

## Our custom accounting GL codes

We have a few custom GL Codes for use within the CS&S accounting system.
These help us categorize transactions more effectively. Here is a summary:

```{list-table}
:header-rows: 1
- - Code
  - Description
- - 4220 Revenues: Services
  - A parent category for this collection of services, we need this as a parent category for CS&S's system.
- - 4221 Revenues: Services: Membership fees
  - For recurring membership fees. This is the recurring part of our 3-tier menu.
- - 4222 Revenues: Services: Cloud cost recovery
  - For pass-through cloud costs. For when we pay for infrastructure on behalf of communities and then pass the costs to them.
- - 4223 Revenues: Services: Usage fees
  - Calculated each month based on a community's usage. Currently defined by Monthly Active Users.
- - 4224 Revenues: Services: Service fees
  - Fees for services not included in recurring membership fees. Basically, anything that isn't cloud costs, usage, or recurring monthly membership fees.
- - 7060 Program Expenses: Cloud Costs
  - A parent category for cloud costs.
- - 7061 Program Expenses: Cloud Costs: Recoverable
  - Cloud costs that we aim to recover from communities. Our goal is to make this equal `$0` after subtracting recovered costs from `4222: Revenues: Services: Cloud cost recovery`.
- - 7062 Program Expenses: Cloud Costs: Nonrecoverable
  - Cloud costs for running our own infrastructure. We do not recover any of these costs.
```

## CS&S accounting contact

Code for Science and Society has an accounting team that manages our books in SAGE Intacct, helps us define annual budgets, and can provide us guidance on accounting questions.
We also have a dedicated **project accountant** named **Josmil Reyes** that focuses his time on 2i2c.
If you have any questions for CS&S regarding accounting, send an e-mail to `fsp@codeforsociety.org` and it will be routed to Josmil.

## Programmatic access to Sage data

(sage:snapshots)=
### Daily snapshots in `2i2c-org/data-private`

We maintain a daily snapshot of our accounting actuals (GL transactions and related data) exported from Sage Intacct in the [`2i2c-org/data-private`][data-private-sage] repository.
See [](#sources:data-repos) for an overview of our data repositories, or the [Sage dataset README][data-private-sage] for what's in the export, how it's refreshed, and how to download it from another repo.

### Direct access to the Sage Intacct API

The data above should be all that you need, but if you need to access the Sage API directly, here's a brief explanation.

We use the [XML Gateway API](https://developer.intacct.com/api/) (not the newer REST API).
See those docs for instructions.

You need both a **Sender** and a **User** credential to access the API.
Credentials are in our [team Bitwarden](#account:bitwarden) under the entry **`Sage Intacct API Admin`**.

The values you'll need are:

- `SENDER_ID`
- `SENDER_PASSWORD`
- `USER_ID`
- `USER_PASSWORD`
- `COMPANY_ID`

[data-private-sage]: https://github.com/2i2c-org/data-private/blob/main/scripts/sage/README.md
