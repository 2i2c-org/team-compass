(product:pricing-strategy)=
# Pricing strategy

This page describes the rationale and strategy behind our pricing.

**Last Updated:** `2026-01-22`
## Guiding principles

The following principles guide our decision-making around pricing our services.
We believe that following these principles allows us to deliver the best services for our communities in a way that aligns with our mission and values.
Our prices should:

- Sustain and grow 2i2c's services and allow it to thrive as an organization.
- Support the extra cost associated with open source contributions.
- Reflect a holistic understanding of open source support, not just code.
- Be competitive with other "Data Science environment as a service" offerings (see below for how we consider ourselves relative to similar offerings).
- Be sustainable for the communities we serve, with mechanisms to accommodate institutions with fewer resources.


## Pricing structure

See [2i2c's service offering](https://sales.2i2c.org/service-description) for a public description of the information in this page.

### Membership

2i2c provides two tiers of managed interactive computing platform services: General Member and Premier Member.

- **General Membership** is priced at $15,000 per year.
- **Premier Membership** pricing is customized based on your institution's specific needs and the depth of engagement required.
  - Typical annual investments range from `$50,000` to `$150,000+`, depending on factors such as the number of hubs, level of customization, consulting hours needed, and strategic collaboration scope.


### Pass-through cloud costs

In addition to our monthly hub fees, we pass {external+docs:ref}`cloud infrastructure costs <costs:cloud>` directly to the communities we serve, without taking any percentage markup.
We do this for two reasons:

1. In our eyes, we are running infrastructure _on behalf of each community_, and wish to act as if a member of that community were running the infrastructure themselves. We are simply being compensated for our time and expertise.
2. Adding a percentage markup on cloud costs may create perverse incentives for us to avoid optimizing down a community's cloud costs.

### Usage costs

2i2c charges a monthly usage fees based on Monthly Active Users (MAU) as follows:

+ First 10 MAU $10.00 / month
+ 11-100 MAU $5.00 / month
+ 101-1000 MAU $2.50 / month
+ 1001-10000 MAU $1.25 / month
+ 10001+ MAU $0 / month

For example, 280 active users in a month costs `$1,000` since `$10x10 + $5x90 + $2.50x180 = $1,000`.

## Projects

2i2c provides open source software development to some of our members. We develop software following [our roadmap](https://2i2c.org/roadmap/about/) using a co-funding model and consistent with the [Right to Replicate](https://2i2c.org/right-to-replicate/) and our [Commitment to Open Technology](https://2i2c.org/open-technology/). 

## What we are missing

We know that there are some communities that will not be well-served by the options described above. Our goal during the alpha is to build sustainability in order to meet these communities in the future. If the model described above doesn’t fit your needs well (e.g., wrong kind of service, too expensive, etc) please provide feedback, as this can help us evolve the service over time.

Below are a few things that we know we are missing:

- **Under-resourced communities**. For many communities, $12,000 a year is too much cost to justify. Our mission requires that we serve these communities as well, not just the ones with larger budgets. This proposal is a step towards sustainability, with the goal of developing new models that can serve under-resourced organizations as well. A few ideas to explore are sponsorship models, tiered pricing models that adjust price based on a community’s budget size, and reducing our internal costs (and thus the fees for our services).
- **Lightweight hubs**. For many individuals or communities, these offerings might involve more complexity than what they need. We’d like to offer a much more scalable and lightweight hub service that people could quickly spin up. We hope to prototype and experiment with ideas after the initial roll-out of the alpha service.
- **Communities that need multiple hubs**. For organizations with many sub-communities and complexity, a single hub is likely not enough to meet their needs. These communities may be better-served by their own dedicated federation of hubs, with a different pricing / growth model than the offerings described here. For now we’ll treat these as partnership opportunities, but may wish to standardize this in a service offering in the future.
- **Significant differences in community size**. Our pricing model assumes that most communities have a relatively similar degree of complexity and size between them. However, when communities grow to a certain size (say, two orders of magnitude), it generates additional work in supporting users and hub operations. We hope to better-understand the costs associated with serving these larger communities, and identify ways to recover them via our pricing.
- **Cloud payments as a service**. In some cases we manage the billing infrastructure and payments for communities (as opposed to them paying cloud providers directly). We do not currently charge explicitly for performing this service. In this case we take on extra work and complexity in tracking and paying cloud bills. We should estimate how much work and risk/liability is entailed in this, and work with our fiscal sponsor to understand how to cover these costs.
- **Liability for cloud payments**. For communities where we manage their cloud billing, we hold some liability because we’ll need to pay the cloud provider for their usage before they pay us. We should work with our fiscal sponsor to understand our risk here (for example, what if a community charges $50,000 in cloud costs and then refuses to pay their invoice). We should also explore potential ways to mitigate this risk (for example, pre-billing communities for *estimated* cloud usage to create a buffer, or asking for a deposit.
