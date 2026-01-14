(communicate-changes:index)=

# Communicating Changes

We're working to be more proactive in planning and communicating infrastructure changes that don't directly impact communities, in addition to sharing new features. This process focuses on changes that match the following description:

> We (2i2c) believe these should have no real user facing changes, but we want you to know this is happening. If you perceive any changes at this date, please let us know and we will respond to it promptly.

This means explicit new feature deployments, working with specific communities, etc are out of scope for this process at this stage.

## When this process applies

Here is an explicit list of the types of changes that will be communicated out through this channel:

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
   3. Changing from Auth0` to CILogon for authenticating by default.
   4. Switching the base instance type from one node type to another.

## Responsibility

Where a communicable change takes place, the engineering manager and the tech leads have the following responsibilities:

1. To ensure that all parties involved in executing or shaping the work are _explicitly_ aware of the need to give notice.
1. To confirm that the notice has been given before the change can be considered "implemented".

It is the responsibility of the person making this change to write the message and ensure it is sent out. This may change in the future as we add more things to the list above.

## How to send this out?

Writing, and sending these messages out should take less than 15 minutes. We do **not** want this to be community specific, but be sent out to _all_ communities. Note that you must be logged in as a FreshDesk admin to complete this process.

### Create a CSV

To create an email to communities via Freshdesk, we need a list of emails, companies (organizations) and names in a .csv file to import into FreshDesk.

- For authorized technical contacts, export a list from FreshDesk, making sure Authorized Technical Contact is checked. FreshDesk has further instructions to [export contacts from FreshDesk](https://support.freshdesk.com/support/solutions/articles/196491-importing-and-exporting-customer-data)
- Then open the resulting file as a spreadsheet and filter on Authorized Technical Contact = TRUE.
- Save that filtered file as a CSV.

### Create an email using our template

We use FreshDesk's [Proactive Outreach](https://support.freshdesk.com/support/solutions/articles/239926-proactive-support-email-outreach) feature to send email alerts for changes.

- Open [Proactive Outreach](https://2i2c.freshdesk.com/a/admin/proactive-support).
- Upload the CSV you created above. This make take a few minutes.
- When prompted to compose an email, start by adding a canned response, and choose Technical Announcement.
- Replace PROMPTs in the Technical Announcement template with text matching the specific change.
- Hit Send.
