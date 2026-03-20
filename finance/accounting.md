# Accounting data

Accounting data describes the money that we **know** we have spent or that we **highly expect** to receive.
Our accounting actuals come from **SAGE Intacct**, managed by our CS&S project accountant.

```{button-link} https://docs.google.com/document/d/1iG2USbvccMGeobKpH52j37LZpmeNASKedJrb0mX8R8Y/edit?tab=t.3bpwr6d9dkbg
:color: primary

Accounting infrastructure guide (SAGE Intacct)
```

See [](accounting-statement-overview.md) for additional context on our SAGE Intacct reports.

(accounting:statements)=
## Monthly reports and accounting actuals

Each month, CS&S closes the books and updates our [budget projections](accounting:projections) with the latest actuals.
See [the monthly process](monthly-process.md) for how this works.

```{toctree}
:hidden:
accounting-statement-overview.md
```

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
