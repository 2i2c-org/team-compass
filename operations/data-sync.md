(operations:data-sync)=
# Data sync automations

[`2i2c-org/data-sync`](https://github.com/2i2c-org/data-sync) keeps data in sync from one system to another ("sync A to B").
It runs scheduled GitHub Actions that read from each source and write changes into the destination.

## What runs today

Here are a few examples, see [2i2c-org/data-sync](https://github.com/2i2c-org/data-sync) for the current list.

- **Label a GitHub issue `CSH` or `asana-sync`**: an Asana task is created that mirrors fields like `GitHub Hours` (plus title and status) from GitHub -> Asana.
- **Add an 'Asana Engagement URL' to a HubSpot Deal****: the matching Asana engagement project will now be updated using HubSpot metadata.
- **Add a HubSpot Deal URL to a GitHub `Sales Issue`**: the issue URL will be added to the HubSpot deal, and HubSpot data will now be synced back to the issue body.

## Seeing what changed

Syncs append to a shared [audit-log spreadsheet](https://docs.google.com/spreadsheets/d/1j2_YL0l91Xjuo-F_6xDTnZnRkka2A9irsqK517itXM0/edit) when something is worth flagging (e.g., a skipped record, or over-writing a URL in HubSpot). It's a place to spot problems, not a complete record of everything that synced.

See the [repository documentation](https://github.com/2i2c-org/data-sync) for sync details and how to add a new one.
