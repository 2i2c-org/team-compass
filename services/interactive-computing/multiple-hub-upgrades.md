# Making Changes to Multiple Hubs (network-wide updates)

As we continue to maintain, refine and improve our infrastructure, there will be cases when we'll need to make updates that impact multiple hubs and communities. 

:::{note}
Examples:
- Infrastructure refactorings (https://github.com/2i2c-org/infrastructure/issues/6756)
- Recurrent upgrades (https://github.com/2i2c-org/infrastructure/issues/6692)
- Network-wide configuration changes (https://github.com/2i2c-org/infrastructure/issues/6692)
- New feature rollouts (https://github.com/2i2c-org/infrastructure/issues/5477)

The technical details will be different but the overall structure is repeatable.
:::

## Define the rationale, scope and rollout procedure of the change

Create a new issue that uses the `Rollout` template defined in the infrastructure repository and add it to the [P&S Project Board](https://github.com/orgs/2i2c-org/projects/57/) `Refined` or `Up Next` column, depending on its readiness to be worked on.

## Schedule the migration

Unless the change is:
  - a security fix that needs to be rolled out as soon as possible
  - a bugfix
  - something small and straightforward
  - a feature that has been extensively tested in at least one other production hub

1. Break down the list of clusters that need to be updated into batches of clusters, each batch having its own sub-issue. 
1. Schedule the migration as part P&S iteration planning process.

```{tip}
Once a migration is started, it is recommended that we try and complete the migration relatively quickly (in one to three iterations depending on the complexity).
```

### How to choose which cluster should go in what batch
Important guidelines to keep in mind when choosing which cluster should be in which batch:

1. Ideally we would split the list of clusters we want to update into **two to four batches maximum**, depending of the number of the clusters that need to be updated and the complexity of the change.

2. This allows us to deploy the change in a **maximum of two iterations**.

3. Choosing which cluster should be in which batch is a non-trivial task, and it depends on the specific change being made as well as the usage patterns of that cluster. Some general rules:

  - For the first batch **choose clusters that have steady usage patterns, but are not having any major events coming up** (e.g. workshops, events, etc.)
  - Also, try to **choose clusters with a diverse set of configurations**, so that we can test the change in a variety of environments. This way, we can identify any potential issues and address them before they impact a larger number of users. 

4. Use the timezones wisely and deploy the change during a time where the cluster is not being used by a large number of users.

## Complete the migration

1. Pull in the sub-issues into P&S iterations, keeping in mind that ideally they should be completed in a maximum of two iterations.
1. Update the main issue as the work is completed cluster-by-cluster.
1. Make any modifications to the technical procedures in the main issue as required.

```{note}
The main issue is completed when all of its sub-issues are completed.
```

## Communicate with our communities

These migrations and updates often involve back end infrastructure that may not be visible to the community. Nonetheless, it is important to provide visibility to our Community Representatives and other Technical Contacts that their infrastructure is being changed.

Reasons to communicate:

- Transparency. If we were to encounter an issue or there was degradation of performance, it is better that the Community is aware than being caught by surprise.
- Cooperation. Some communities may have specific dates where the migration is better scheduled or critical times where no migration is possible. By proactively communicating with our communities we are demonstrating we are working with them to improve the interactive computing infrastructure that they depend upon.
- Value. We need to continue demonstrate the value we are providing to our communities. Especially for infrastructure changes that will not be visible to their end users, regular communication with community stakeholders show how and where 2i2c is provide critical value.

See [](communicating-changes) for specific steps.

## Celebrate and share our success

In addition to the [directed communication](communicate-changes:index) with Community Representatives and Technical Contacts, the conclusion of a multi-hub deployment of a security fix, feature roll out, migration, or improve, is a reason to celebrate.

Create a [blog post](blog:index) to share this news with our network.
