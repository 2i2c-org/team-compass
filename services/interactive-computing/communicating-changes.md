(communicate-changes:index)=

# Communicating Changes to all communities

This page describes how to communicate changes to community infrastructure as part of ongoing operations.

## How to send an e-mail to all community representatives

**First, download a CSV of community contacts**

1. In HubSpot, go to the [**Active Communities View**](https://app-na2.hubspot.com/contacts/242496330/objects/0-410/views/350388040/list?noprefetch=). This is a list of communities with an "Active" member status[^note]
2. Click {guilabel}`Export` -> {guilabel}`Export`
3. Go to the [Export Audit page](https://app-na2.hubspot.com/sales-products-settings/242496330/importexport)
4. Click the top-most **Active Communities** link. It will download a CSV of contacts.

[^note]: This may change if we track active communities at the _deal_ level, but as of May 6 2026 this is how we define active communities.

**Next, extract the e-mails with our helper sheet**

1. Go to our [contacts helper google sheet](https://docs.google.com/spreadsheets/d/1XXMcDljWZIg08nHK-QU2ek0kiPnVZXpPJPil9CFl7Jo/edit?gid=641195895#gid=641195895). This is a convenience sheet to extract a unique list of contact e-mails from this export.
2. Follow the instructions on the first tab of that sheet.
3. **Option 1**: Paste the resulting e-mails into your e-mail client of choice and send!
4. **Option 2**: Download the e-mails to a CSV file and follow the FreshDesk steps below.

**Last, send an email using the FreshDesk template**

We use FreshDesk's [Proactive Outreach](https://support.freshdesk.com/support/solutions/articles/239926-proactive-support-email-outreach) feature to send email alerts for changes.

- Open [Proactive Outreach](https://2i2c.freshdesk.com/a/admin/proactive-support).
- Upload the CSV you created above. This may take a few minutes.
- When prompted to compose an email, start by adding a canned response, and choose Technical Announcement.
- Replace PROMPTs in the Technical Announcement template with text matching the specific change.
- Hit Send.

## When this process applies

Here is a list of the types of changes that will be communicated out through this channel:

1. Version upgrades of:
   1. `z2jh`
   2. Kubernetes
   3. `jupyterhub-fancy-profiles`
   4. `jupyterhub-home-nfs`
   5. `dask-gateway`
   6. `binderhub`
   7. [Our home page default implementation](https://github.com/2i2c-org/infrastructure/issues/5399)

2. _Structural_ changes in how we provide our service. Examples of this would be:
   1. Moving from using cloud provider home directories to `jupyterhub-home-nfs`.
   2. Modifying our `profileList` options to match memory requests to guarantees.
   3. Changing from Auth0 to CILogon for authenticating by default.
   4. Switching the base instance type from one node type to another.

## Responsibility

Where a communicable change takes place, the engineering manager and the tech leads have the following responsibilities:

1. To ensure that all parties involved in executing or shaping the work are _explicitly_ aware of the need to give notice.
1. To confirm that the notice has been given before the change can be considered "implemented".

It is the responsibility of the person making this change to write the message and ensure it is sent out.

