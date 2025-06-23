# Accounting data

Accounting data describes the money that we **know** we have spent or that we **highly expect** to receive.

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


## Accounting transactions airtable

:::{admonition} This is not reliable
This is not currently reliable, and we should update this section once it is.
:::

{term}`CS&S` provides us a monthly dataset of the last 6 months of all of all our accounting transactions.
This is [in a Google Sheet that is automatically updated each day][gsheet].
It includes the last 6 months of any transaction 2i2c has made (if we need more than 6 months of history, ask `fsp@2i2c.org` for a custom data dump).

We have a copy of this sheet in an [**Accounting Transactions AirTable**][accounting-table][^airtable].
We use this to create [our accounting dashboard](accounting:dashboard).

[^airtable]: See [](../administration/airtable.md) for how to access AirTable.

[gsheet]: https://docs.google.com/spreadsheets/d/1qH5IK18z79X8cEwlwDwnlArTiYnbRVIPGqdOUdrsF0c/edit?usp=sharing

[accounting-table]: https://airtable.com/appbjBTRIbgRiElkr/tblDKGQFU0iEIa5Qb/viwAdsIgMwbqKDdZ0

### Update our accounting data airtable

We have a semi-automated process to update the data in our accounting table.
Here are the steps to follow:

% TODO: We should automate this with a CRON job, make.com/zapier integration, etc.
%   ref: https://github.com/2i2c-org/team-compass/issues/703
1. **Confirm that [the Google Sheet][gsheet] has been updated** by checking the `Automatic Operations Events Log` tab.
2. **Delete all of the records** in the [accounting table][accounting-table].
3. **Import the google sheets data**. Go to `Accounting Transactions` -> `Import Data` -> `Google Sheets` -> `Google sheets account`.
   - Here's an image of the menu you want:

     ![image](https://user-images.githubusercontent.com/1839645/230121196-0d398812-ba22-4cea-a42f-e3ad644a3e19.png)
   - You'll see a list of Google Sheets in our account. Import the one titled `2i2c FYE23 Account Transactions - Auto Generated`.
   - Check the `Skip first row` option during the import, so that we don't import the section title names.

This should automatically import the data into the proper columns, you don't need to do anything else.

When this action happens, an [AirTable automation will run](https://airtable.com/appbjBTRIbgRiElkr/wflVJQz277S6lF0E3/wtrHzwIWJLGTnJl0m) and attempt to link each new record with a corresponding **Contract**, using the `Xero ID` field.
If a contract with the record's `Xero ID` is found, then a linked record will be created in the `Contracts` column.

Here's a brief video describing the above process.

```{video} https://drive.google.com/file/d/1eLHQ15sHF4ihCpEIAypjYUeof9q3CYYQ/view?usp=sharing
```

(accounting:statements)=
## Monthly reports

CS&S generates monthly reports for our current financial situation.
You can find them in [our financial reports folder](https://drive.google.com/drive/folders/1vM_QX1J8GW5z8W5WemxhhVjcCS2kEovN?usp=sharing).

When these monthly reports come in, it triggers [the monthly budget projection process](monthly-process.md).

Below are some Frequently Asked Questions along with a more detailed description of these reports.

### How much Net Income does 2i2c have?

`Net Income` is a combination of the following things:

- Our Cash on Hand.
- Income for which CS&S has `Authorized` an invoice.
- Costs for which CS&S has received an invoice but not yet paid.

To find this number, follow these steps:

- Open [](accounting:income-statement).
- Scroll to the bottom of **the `FSP: 2i2c` column**.
- Use the number in the **`Net Income`** row.

```{admonition} This will be at least one month out of date
:class: warning
CS&S prepares our monthly reports using last-month's data.
This means that the definition of `Net Income` is true as of the end of the window used in that report.
This is usually about a month in the past.
See [](contracts:amount-remaining) for how to correct for this gap.
```

### Detailed monthly reports description

See [](accounting-statement-overview.md) for more information about these sheets.

```{toctree}
:hidden:
accounting-statement-overview.md
```

## CS&S accounting contact

Code for Science and Society has an accounting team that puts together our monthly reports, helps us define annual budgets, and can provide us guidance on accounting questions.
We also have a dedicated **project accountant** named **Josmil Reyes** that focuses his time on 2i2c.
If you have any questions for CS&S regarding accounting, send an e-mail to `fsp@codeforsociety.org` and it will be routed to Josmil.

(accounting:dashboard)=
## Summary dashboards

We have an [AirTable interface dashboard][airtable-dashboard] that displays several useful summaries and visualizations of our accounting data[^airtable].
You can gain access to it with [this invitation link](https://airtable.com/invite/l?inviteId=invF192DfoKa5xqqY&inviteToken=ef8865617dd3b6ebbb01b753fa2de0d231f1a7f526b6fe07d3cf88c12a418f5f&utm_medium=email&utm_source=product_team&utm_content=transactional-alerts).

We also have a [page in our KPIs website](https://2i2c.org/kpis/finances/#accounting-tables) that provides public summaries of this information for transparency to external stakeholders.

[airtable-dashboard]: https://airtable.com/appbjBTRIbgRiElkr/pagbwk3T7S14rJ3tb

