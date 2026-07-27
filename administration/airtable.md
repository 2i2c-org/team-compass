(accounts:airtable)=
# AirTable accounts

```{admonition} Mostly deprecated
:class: warning
The only things we actively use AirTable for are tracking team [salaries and contracts](#airtable:salaries) and [team contact info](#airtable:team-info).
Most other historical content in AirTable is no longer maintained.
```

This page covers our AirTable account, how to access it, and what we use it for.

## Read-only access to the AirTable

[Here's a link to our primary AirTable workspace](https://airtable.com/invite/l?inviteId=inv3bBae7WUqQsehA&inviteToken=7689178d3e79af8956d1f5cd958d9d8e63160e86b70c74d2d8bb2502ce665e00&utm_medium=email&utm_source=product_team&utm_content=transactional-alerts).

This is a read-only link, valid for any `@2i2c.org` address.
If you need edit permissions, use the [shared AirTable account](#airtable:shared).

(airtable:shared)=
## Edit access to the AirTable

We have a single account on the "Pro" plan of AirTable.
It is the only account with edit permissions.

To access this account, use our [shared passwords account](#account:bitwarden) for credentials.

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

(airtable:team-info)=
### Team info table

We track team contact info (GitHub handle, e-mail, etc.) in a table in the same base.

[Open the Team info table](https://airtable.com/appHxyAV6MR1g8e2w/tblP0d3WPPNaov34H/viwQ9qCbadOfdY0Rp?blocks=hide).

It is published nightly to [`2i2c-org/data-private`](https://github.com/2i2c-org/data-private), so automated jobs can look up things like GitHub usernames without querying AirTable directly.

### How to update roles and contracts

Every year, we update our roles to reflect cost of living (COLA) adjustments and changes to descriptions.
Follow these steps:

- For each role and for each contract that will continue:
- Duplicate it
- Update the Start / End date (usually July 1st -> June 30th of the next year)
- Update the salary / description if necessary
- Link the old item to the new item via the "Renewed by" field in the old item.
