# Accounting data

Accounting data describes the money that we **know** we have spent or that we **highly expect** to receive.

## Accounting transactions airtable

{term}`CS&S` provides us a monthly dataset of the last 6 months of all of all our accounting transactions.
This is [in a Google Sheet that is automatically updated each day][gsheet].
It includes the last 6 months of any transaction 2i2c has made (if we need more than 6 months of history, ask `fsp@2i2c.org` for a custom data dump).

We have a copy of this sheet in an [**Accounting Transactions AirTable**][accounting-table][^airtable].
Any columns that are synchronized with CS&S have a little lightning bolt (⚡) next to them.
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

See [](accounting-statement-overview.md) for more information about these sheets.

```{toctree}
:hidden:
accounting-statement-overview.md
```

(accounting:dashboard)=
## Summary dashboards

We have an [AirTable interface dashboard][airtable-dashboard] that displays several useful summaries and visualizations of our accounting data[^airtable].

We also have a [page in our KPIs website](https://2i2c.org/kpis/finances/#accounting-tables) that provides public summaries of this information for transparency to external stakeholders.

[airtable-dashboard]: https://airtable.com/appbjBTRIbgRiElkr/pagbwk3T7S14rJ3tb

