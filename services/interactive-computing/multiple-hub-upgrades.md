# Making Changes to Multiple Hubs

As we continue to refine and improve our infrastructure, we encounter situations where we need to modify the infrastructure that impacts multiple hubs and communities.

:::{note}
As **motivation** for this process is used, consider [[Infrastructure Refactor] EKS clusters refactor Q4 2025  ](https://github.com/2i2c-org/infrastructure/issues/6756) as an example.

Other examples:
- Helm chart upgrades (https://github.com/2i2c-org/infrastructure/issues/6692)
- Configuration change involving multiple hubs (https://github.com/2i2c-org/infrastructure/issues/6692)
- Rolling out of a new feature (https://github.com/2i2c-org/infrastructure/issues/5477)

The technical details will be different but the overall structure is repeatable.
:::

## Define the rational and scope of the change

A typical pattern is the an upgrade, new feature, or fix has been completed for one hub and now needs to be rolled to many other hubs and communities.

Create a new `[Platform Initiative]` issue on the [P&S Project Board](https://github.com/orgs/2i2c-org/projects/57/) that uses the following template:

```markdown
We want to <describe the migration>. This will save us future time, make all our infrastructure easier to support, and get us <rationale for completing this migration>.  

This change was previously implemented for <link to the issue where the change was made for one community>

## Changes

- <list of the changes that are expected after the migration is complete>

## Untested

- <list posible areas of concern for thing we do not yet know but need to be aware of>

## Timeline

We want everything migrated by <timeline for the change>.

## Clusters to Migrate

All clusters must be migrated. <Replace with subset based on cloud provider if appropriate>

- [ ] cluster1 <add link to issue once that cluster is migrated>
- [ ] cluster2 <add link to issue once that cluster is migrated>
- [ ] cluster3 <add link to issue once that cluster is migrated>

## Migration procedure

<Document the process anticipated for doing the upgrade or migration. Use sufficient detail so that multiple team members could pick up and assist with the work>

<See https://github.com/2i2c-org/infrastructure/issues/6756 for an example>

## Validation

1. <steps to confirm that the change or migration worked as expected>
2. <checks on any possible side effects that may need to be mitigated>
```

## Schedule the migration

For each cluster (or group of clusters) create a sub-issue to break the migration into iteration long substeps.

Schedule the migration as part P&S iteration planning process.

Once a migration is started, it is recommended that we try and complete the migration relatively quickly (in one to three iterations depending on the complexity).

## Communicate with our communites

These migrations and updates often involve back end infrastruce that may not be visible to the community. Nonetheless, it is important to provide visibility to our Community Representatives and other Technical Contacts that their infrastructure is being changed.

Reasons to communicate:
- Transparency. If we were to encounter an issue or there was degredation of performance, it is better that the Community is aware than being caught by surprise.
- Cooperation. Some communities may have specific dates where the migration is better scheduled or critical times where no migration is possible. By proactively communicating with our communities we are demonstrating we are working with them to improve the interactive computing infrastructure that they depend upon.
- Value. We need to continue demonstrate the value we are providing to our communities. Especially for infrastructure changes that will not be visible to their end users, regular communication with community stakeholders show how and where 2i2c is provide critical value.

See [](communicating-changes) for specific steps.

## Complete the migration

Pull in the sub-issues into P&S interations. Update the main issue as the work is completed cluster-by-cluster. Make any modifications to the technical procedures in the main issue as required.

The main issue is completed when all of its sub-issues are completed.

## Celebrate and share our success

In addition to the [directed communication](communicating-changes) with Community Representatives and Technical Contacts, the conclusion of a multi-hub deployment of a security fix, feature roll out, migration, or improve is a reason to celebrate.

Create a [blog post](blog:index) to share this news with our network.

