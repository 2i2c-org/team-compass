# Grants and projects workflow

Grants and projects are partnerships that are more complex and bespoke than our [hub service contracts](./hub-service.md).
They often require more work to achieve, as well as more work to deliver.

In the remainder of this document we use `Grant` to refer to **both** traditional grant workflows, as well as more complex contracts that are nonetheless service contracts.

## Sources of truth

We split our workflow around a few Sources of Truth:

1. **[Our `Leads/Grants and projects` AirTable](https://airtable.com/appbjBTRIbgRiElkr/tblmRU6U53i8o7z2I/viwQoT7EO2K97mMEu?blocks=hide) captures metadata about each grant**.
   Each entry has a mirrored GitHub issue with an auto-generated table that shares its metadata on GitHub.
2. **[Issues in the `leads/` repository](https://github.com/2i2c-org/leads) capture our conversation around a grant lead**, such as coordinating the actions we must take to complete its application.
3. **Extra GitHub issues capture specific deliverables and tasks**, such as completing a grant application. These should be linked from the mirrored issue described above.
4. **[Our `Active Grants and projects` AirTable](https://airtable.com/appbjBTRIbgRiElkr/tblCUDimpwHgiWbPq/viwzqESsgIqWZoVZf?blocks=hide) tracks grants we've been awarded**.
   This is where we coordinate the actions needed to deliver on the goals of the grant and track its progress.

:::{figure} ./images/grants-airtable.png
Here's an example of the AirTable entry for a grant lead (left) and its corresponding mirrored GitHub issue (right) where we coordinate conversation.
:::

## Workflow around grant and project leads

1. **Add a new entry to [the `Grants and projects` view](https://airtable.com/appbjBTRIbgRiElkr/tblmRU6U53i8o7z2I/viwQoT7EO2K97mMEu?blocks=hide)**. This will automatically create a GitHub issue in [the `leads/` repository](https://github.com/2i2c-org/leads).
2. **Fill in as much metadata as you can**.
   Fill in the fields for each column of the new entry.
   This gives our team the context we need to reason about the opportunity.

   As we fill in this information, it will automatically be mirrored to the GitHub issue for the grant.
3. **Discuss and coordinate in the mirrored GitHub issue**. 
   Use the GitHub issue to have discussion across the team about the status of the grant.
4. **Create new GitHub issues to coordinate work**.
   If we must coordinate a plan around completing a grant, create a new GitHub issue and link it somewhere in the comments from the mirrored issue.
   % TODO: Consider adding a field in our AirTable for a "work issue" if the need arises.
5. **When a grant is awarded, add an entry to [our active `Grants and projects` AirTable](https://airtable.com/appbjBTRIbgRiElkr/tblCUDimpwHgiWbPq/viwzqESsgIqWZoVZf?blocks=hide) and link it to the Lead**.
   We use the [active `Grants and projects` airtable](https://airtable.com/appbjBTRIbgRiElkr/tblCUDimpwHgiWbPq/viwzqESsgIqWZoVZf?blocks=hide) to track grants that we have been awarded.
   Once a grant is awarded, link the Lead to it start tracking our work over there.
   