(operations:data-sync)=

# Data sync automations

[`2i2c-org/data-sync`](https://github.com/2i2c-org/data-sync) keeps data in sync from one system to another ("sync A to B").
It runs scheduled GitHub Actions that read from each source and write changes into the destination.

## What runs today

Here are a few examples, see [2i2c-org/data-sync](https://github.com/2i2c-org/data-sync) for the current list.

- **Label a GitHub issue with a sync label**: a task is created in [our Asana activity log](#operations:activity-log) that mirrors fields like `GitHub Hours` (plus title and status) from GitHub -> Asana. The list of sync labels lives in the [data-sync repository](https://github.com/2i2c-org/data-sync).
- **Add an 'Asana Engagement URL' to a HubSpot Deal**: the matching Asana engagement project will now be updated using HubSpot metadata.
- **Add a HubSpot Deal URL to a GitHub `Sales Issue`**: the issue URL will be added to the HubSpot deal, and HubSpot data will now be synced back to the issue body.

See the [Create a GitHub Sales Issue to a HubSpot Deal?](https://docs.google.com/document/d/1T6kl8bOt6S0ltt5ICxlmX-CKSgkrL3e1qmvGYDI1JNM/edit?tab=t.0#bookmark=id.kpu3yimlioxu) section in the [HubSpot and CRM guide](https://docs.google.com/document/d/1T6kl8bOt6S0ltt5ICxlmX-CKSgkrL3e1qmvGYDI1JNM/edit?usp=sharing) document for the workflow details.

## Seeing what changed

Syncs append to a shared [audit-log spreadsheet](https://docs.google.com/spreadsheets/d/1j2_YL0l91Xjuo-F_6xDTnZnRkka2A9irsqK517itXM0/edit) when something is worth flagging (e.g., a skipped record, or over-writing a URL in HubSpot). It's a place to spot problems, not a complete record of everything that synced.

See the [repository documentation](https://github.com/2i2c-org/data-sync) for sync details and how to add a new one.

## When a sync fails

When a scheduled sync fails, a bot posts a message in the `#operations` Slack channel with a link to the failed run.
This covers the syncs in [`2i2c-org/data-sync`](https://github.com/2i2c-org/data-sync) and the daily MAU update in [`2i2c-org/data`](https://github.com/2i2c-org/data).

The bot posts through a Slack webhook, which is a private URL that can send messages to `#operations`.
The URL is stored in the `SLACK_OPERATIONS_WEBHOOK_URL` [organization secret](https://github.com/organizations/2i2c-org/settings/secrets/actions), and only the repositories listed on that secret can use it.

If another job's failures would be useful in `#operations`, add an alert for it:

1. On the secret's settings page, give the job's repository access to the secret.
2. Copy the "Alert Slack on failure" step from one of the [data-sync workflows](https://github.com/2i2c-org/data-sync/tree/main/.github/workflows) to the end of the job.
