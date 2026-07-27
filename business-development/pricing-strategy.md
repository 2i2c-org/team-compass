(product:pricing-strategy)=
# Pricing strategy

This page describes our pricing rationale and numbers.
Our service offering is described in [](#mission:service-model).

**Last Updated:** `2026-06-26`
## Guiding principles

Our prices should:

- Sustain and grow 2i2c's services and allow it to thrive as an organization.
- Support the extra cost associated with open source contributions.
- Reflect the full cost of open source support, not just code.
- Be competitive with other "Data Science environment as a service" offerings (see below for how we consider ourselves relative to similar offerings).
- Be sustainable for the communities we serve, with mechanisms to accommodate institutions with fewer resources.
- Be predictable and bounded. Usage is real cash out the door for us, so our model is a fixed, capped membership base plus bounded usage, cloud, and opt-in add-ons. We avoid usage-blind flat pricing, which doesn't scale as a community grows.


## Pricing structure

### Membership

Membership covers all four [areas of our work](#mission:service-model). Each tier is a fixed annual fee, capped at the listed amount, and is the member's entire required commitment.

- **General Membership** is $15,000 per year.
- **Premier Membership** is $50,000 per year. It includes more service hours and strategic collaboration than General.

A member with no hub pays the tier base fee only, with no [usage](#pricing:usage-costs) or [cloud](#pricing:cloud) costs.

Members who want more can fund a [directed engagement](#directed-engagements) on top of either tier.

See [2i2c's service offering](https://sales.2i2c.org/service-description) for current figures, included service hours, and add-on pricing.


(pricing:cloud)=
### Pass-through cloud costs

If we pay cloud bills on behalf of communities, we pass [cloud infrastructure costs](xref:docs#costs:cloud) directly to the communities we serve, without taking any percentage markup.
We do this for two reasons:

1. We run infrastructure _on behalf of each community_, as if a member of that community were running it themselves.
2. Adding a percentage markup on cloud costs may create perverse incentives for us to avoid optimizing down a community's cloud costs.

(pricing:usage-costs)=
### Usage costs

2i2c charges a monthly usage fees based on Monthly Active Users (MAU) as follows:

+ First 10 MAU $10.00 / month
+ 11-100 MAU $5.00 / month
+ 101-1000 MAU $2.50 / month
+ 1001-10000 MAU $1.25 / month
+ 10001+ MAU $0 / month

For example, 280 active users in a month costs `$1,000` since `$10x10 + $5x90 + $2.50x180 = $1,000`.

Because the rate drops to $0 above 10,000 MAU, this fee is bounded.
A single community's usage fee tops out at about `$14,050` per month (`$10x10 + $5x90 + $2.50x900 + $1.25x9000`) and never grows beyond that, no matter how large the community becomes.

(directed-engagements)=
## Directed engagements

Beyond membership, a member can fund a [directed engagement](#mission:service-model), such as a co-funded [project](https://2i2c.org/roadmap/about/) that follows our roadmap (consistent with the [Right to Replicate](https://2i2c.org/right-to-replicate/) and [Commitment to Open Technology](https://2i2c.org/open-technology/)).

A member raises a need, we scope it together into a rough size and set of deliverables, and we quote from our rate.

(pricing:rate)=
### How we set our rate

We publish a blended rate of about **$250/hour**. Here's where it comes from.

We pay team members for a full ~2,000-hour year, but assume only about 900 of those hours are directly billed to projects.
The rest goes to open source stewardship, maintenance, and running 2i2c.
Membership helps fund that stewardship, but not all of it.
We use directed engagements and our hourly rate to make up the difference.

```{list-table}
:header-rows: 1

* - Layer
  - Running rate
* - A fully-burdened engineer (~$180k/year, salary plus ~20% benefits and payroll taxes) over ~900 hours we bill directly to funded projects.
  - ~$200
* - Plus our fiscal sponsor's fee (~15%), paid on everything we bill.
  - ~$230
* - Plus a margin for 2i2c's operations and financial resilience (~9%).
  - ~$250
```

This % of "billable hours" is lower than most consultancies, but it reflects the fact that we spend a significant amount of additional time providing leadership, maintenance, and support for the open source communities that our members depend on.
We review these figures annually and adjust with our costs.

**Federal and other rate-constrained funders.**
For some funders (e.g., US federal government), we must directly bill all work that is relevant, rather than putting it behind an indirect.
Where possible, we scope this work as a funded workstream with its own deliverables, rather than an indirect cost buried in the rate.
When that is not possible, we may quote a lower rate and accept that we under-recover the open source work.
