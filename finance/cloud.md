# Cloud costs

All of our cloud costs are paid via [our Ramp credit card](admin:credit-card) which is attached to cloud billing accounts that are connected to our infrastructure.

These costs are recovered either by our central funds, or via reimbursement requests to our community partners.

Below we describe how we recover these costs for various cloud infrastructure setups.

## General principle

We treat cloud costs differently from other kinds of costs.
They are **not payment for services**, they are **reimbursements for our expenses**.

They have a different line-item and category in our CS&S invoicing statements and this allows us to recover these costs without incurring our Fiscal Sponsorship Fee from CS&S.

We may wish to charge a bit extra for the **staffing** costs of this service, but this is different from the pass-through cloud bill.

## Reimburse cloud costs

See [](reimburse:cloud).

## Dedicated clusters

When a community has a dedicated cluster, it is straightforward to calculate their monthly cloud costs.

In the cloud console, look for their monthly cloud fee, take a screenshot of this page, and notify {role}`CS&S Operations` with the name of the community and the amount to reimburse.

Here's an issue where we are refining this process:

- https://github.com/2i2c-org/team-compass/issues/498

## Shared clusters

:::{admonition} Currently unavailable for new clusters
We are not offering any new shared clusters that are shared by multiple communities. The overhead of managing a shared cluster currently outweighs the administrative overheads. We will revisit this later as we refine our product process.
:::

When usage on a cluster is shared by many communities, we must divide the monthly cloud infrastructure cost between each of these communities.
We divide the cost based on the **usage that each community has incurred**.

We are currently exploring how to quickly define "usage" and will update this once we've resolved the issues below:

- https://github.com/2i2c-org/team-compass/issues/499
- https://github.com/2i2c-org/infrastructure/issues/730

## Grant sub-awards

When we are sub-awardees on a grant (e.g., when somebody is putting 2i2c as a line-item on a grant), we **do not add budget items for our expected cloud costs**.

Instead, we include language in the contract to **reimburse** our cloud costs.
We should include estimates of expected monthly cost, as well as monthly limits we will not exceed without approval.

We should advise collaborators to budget their own expected cloud costs according to [these guidelines](costs:cloud:grants). 

(costs:cloud:grants)=
## Grants we apply for

When we apply for grants, we must add a line item for our expected cloud cost.
This will depend heavily on the nature of the grant and what we commit to.
Here are some guidelines to follow:

- **Use historical data** from similar communities, and multiple by a factor depending on the difference in size and number of communities.
- **Be conservative** and assume that costs will be higher than expected.
- **Add a 2x buffer** in case we go higher than expected. It is much easier to reduce our budget if we under-spend costs than to increase our budget if we over-spend.

## Our own cloud infrastructure

For any cloud infrastructure that is not directly tied to serving another community, we pay for them ourselves out of our central funds.
