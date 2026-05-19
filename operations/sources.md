# Where to look for information

There are several major sources of information within 2i2c:

## Documentation

The most stable form of information in 2i2c is documentation that our teams maintain.
This is where most information about 2i2c exists.

See [](./documentation.md) for information about documentation at 2i2c.

## Google Drive

We have a Shared Google Drive that contains all of 2i2c's documents that don't fit into GitHub. It is accessible to everybody at 2i2c, using your `@2i2c.org` account.

It is called **`2i2c Team Drive`** and should be accessible on the left under **`Shared Drives`**.

Google Drive doesn't let you link to a Shared Drive directly, so here's a link to the `Engineering` folder in the drive.
Navigate up one folder to find the Share Drive root.

```{button-link} https://drive.google.com/drive/folders/1a2VTtMubHRiY4yg0pP-FPC9C4nYJzbaT?usp=sharing
:color: primary
2i2c Team Drive
```

:::{note}
There are still some files in the old team drive that we have not yet moved over.
These are mostly assets from earlier partnerships that are trickier to move.
See [the old Drive folder](https://drive.google.com/drive/folders/1ABxxSFycGfCzQc9czfwer_dat-GVi4jw?usp=sharing) if you need anything there.
:::

## Public GitHub Issues

Most of our conversations, planning, and work tracking happens in GitHub.
See [](coordination:workflow) for more information.

## Private GitHub Issues

There are a few repositories that we use for tracking private conversations and issues.
This is usually personally sensitive or identifiable information, or information that needs to be private until decisions or deals are finalized.

- [**`2i2c-org/meta`**](https://github.com/2i2c-org/meta): Private team and organizational conversation.

(sources:data-repos)=
## Data repositories

We maintain two repositories that publish snapshots of 2i2c's data on a daily schedule, so that other tools and repos can consume them without hitting upstream APIs.

- [**`2i2c-org/data`**](https://github.com/2i2c-org/data): Public data about 2i2c's infrastructure and services (e.g. cloud usage, MAUs).
  Datasets are published as GitHub Releases and rendered as a browsable [docs site](https://2i2c.org/data/).
- [**`2i2c-org/data-private`**](https://github.com/2i2c-org/data-private): Private financial data (Sage Intacct accounting, HubSpot deals).
  Datasets are published as GitHub Releases and to Google Sheets.

Each repository's README describes the datasets it contains and how to download them from another repo.
