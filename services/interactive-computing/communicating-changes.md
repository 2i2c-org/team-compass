(communicate-changes:index)=

# Communicating Changes to all communities

This page describes how to communicate changes to community infrastructure as part of ongoing operations.

## How to send an e-mail to all community representatives

We send these e-mails through HubSpot, which is configured to send from our `@2i2c.org` domain.
See [](#hubspot:email) for the general process of e-mailing groups of contacts.

Send to our **active community representatives**, which is the combination of these two segments[^note]:

- [Community representatives for Active Communities](https://app-na2.hubspot.com/contacts/242496330/objectLists/54/filters)
- [Technical contacts for Active Communities](https://app-na2.hubspot.com/contacts/242496330/objectLists/56/filters)

See [](#hubspot:email) for instructions on sending an e-mail to segments.

Replies to these e-mails are tracked in FreshDesk, so check there periodically for any responses.

[^note]: This may change if we track active communities at the _deal_ level, but as of May 6 2026 this is how we define active communities.

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

