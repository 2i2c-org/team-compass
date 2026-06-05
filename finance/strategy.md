# Financial strategy

Our financial strategy guides how we'll make decisions that impact our finances.
This includes the indicators we watch to stay sustainable and how we'll prioritize different kinds of revenue streams.

## Definitions

Monthly recurring revenue
: Revenue brought in through **recurring** service contracts.
  This is the primary non-confirmed revenue that we _project into the future_ in our financial modeling.

  Our [budget projections model](accounting:projections) uses deal data from [HubSpot](hubspot:index) to project future revenue, which may include grant-funded service contracts alongside regular service contracts.

Cash on hand
: The amount of disposable funds that we have in our CS&S accounts.
  This does not include expected revenue or expenses.
  We calculate this at the end of each month from CS&S's accounting reports.

Monthly burn rate
: `monthly recurring revenue - monthly costs`. This is the amount by which our cash-on-hand changes each month.
  See [our budget projections](accounting:projections) for how we project future revenue using HubSpot deal data.

Runway
: How many months before we run out of funds. We look at this two complementary ways:

  - **Projected runway** [projects current numbers into the future](#accounting:projections) (for both committed and expected revenue) and sees when we hit `$0`. It tells us whether we can afford to grow.
  - **Cash reserve** is the simpler `cash on hand / monthly costs`: how long we'd last _if revenue stopped today_. It tells us how resilient we are to disruption.

  Both are tracked as [financial health indicators](#finance:financial-health-indicators) on our dashboard.

## Cycles of capacity growth

We expect our runway to grow and shrink as we move between cycles of capacity growth and commitment growth.

If our runway is too long, it means we are not investing enough in our operations and under-achieving our impact.
If our runway is too short, it means that we are running the risk that we'll run out of funding.
Here's what these cycles should look like:

1. **Capacity growth**. Invest to grow our capacity to serve, develop, and experiment. This will _shorten our runway_ (by increasing our costs).
2. **Commitment growth**. Invest in growing revenue via contracts and grants at a fixed capacity. This will _lengthen our runway_ (by increasing our revenue).

(finance:financial-health-indicators)=
## Financial health indicators

We track a handful of indicators to judge whether 2i2c is financially healthy and sustainable.
Their live values, target thresholds, and color-coded bands live on the [financial health indicators](https://finance.2i2c.org/projections/) of our [finance dashboard](#finance:dashboards) - this section describes what each one asks and why it matters.

Committed runway
: How many months we can operate before cash runs out, **assuming we fully collect our on-the-books contracts**.
  It tells us whether we can afford to grow or hire with committed revenue.
  We measure it in sales cycles (the time it takes to close new revenue) rather than absolute months, so the target scales with how quickly we can respond.

Estimated runway
: How many months we can operate before cash runs out, **assuming our expected deals land as well**.
  This is a more ambitious version of our "Committed" runway, with more assumptions being made.
  It is our best estimate for what we think will happen, and generally our default definition of "our runway".

Cash reserve
: How many months we could operate **if revenue stopped today**.
  Unlike projected runway it ignores future revenue, so it measures resilience to disruption.
  Nonprofit best practice is to hold 3-6 months of operating costs in reserve[^reserves].

Committed cost coverage
: How much of our team's monthly cost is paid for by **already-signed** work.
  This tells us whether our active contracts are covering our costs (ie, how quickly we're eating into our cash).

Pipeline coverage
: Whether our probability-weighted **pipeline** is large enough to fill the cost gap that signed work doesn't already cover.
  This tells us whether we expect to cover our cost gap with new sales.

Customer concentration
: How much of our revenue depends on our largest few customers.
  High concentration means losing a single relationship could threaten our solvency.

[^reserves]: See [Nonprofit Operating Reserves: An Introduction](https://nonprofitaccountingbasics.org/sites/default/files/03-Nonprofit%20Operating%20Reserves-An%20Introduction_0.pdf) and [Nonprofit Operating Reserve: Policy, Ratios, and IRS Rules](https://legalclarity.org/nonprofit-operating-reserve-policy-ratios-and-irs-rules/) for the rationale and common benchmarks behind operating-reserve targets.

## Cost recovery indicators

Beyond the projections above, we informally track whether we're **collecting money we've already earned or been promised**.
These live on the [recovery indicators](https://finance.2i2c.org/recovery/) page of our dashboard:

Invoice collection
: Are we collecting invoices we've already billed, or are they slipping overdue?

Grant collection pace
: Are we invoicing our active grants on pace with the time elapsed on each contract?

MAU recovery
: Are we billing the monthly-active-user usage fees that our hub usage implies?

Cloud recovery
: Are we billing back the cloud costs we incur on behalf of communities?

## Balance of contract revenue vs. grants

These are goals that we shoot for, and not necessarily reflective of current reality.

**Most of our funding should come from recurring service fees**.
This is the most reliable source of income.
It gives us a low-variance way to bring in funding and an easy way to demonstrate impact.

**The majority of our recurring revenue should not come from grants**.
Recurring revenue should come from a combination of many contracts, not singular large contracts that will drop off all at once.

**Service-focused grants sohuld support under-resourced communities**.
Grants that cover the costs of our hub service is a special case.
We should treat them like service revenue as long as we have a model for how we'll renew grant funds.
They should particularly target communities that couldn't pay on their own.

**Non-service grants should be used to invest in new services or one-off improvements**.
Other grant opportunities should not go towards core operations that we must continue over time.
We should treat them as temporary extra capacity to:

- Make targeted improvements to our tools, processes, etc.
- Prototype a new service or improvement that we wish to generate funds with in the future.
- Provide crucial, temporary support to ourselves or another community.

**Development contracts should be treated like grants**.
If we get a contract to perform some kind of development, we should think of it as a one-off source of funds, not recurring revenue.

## Case study: how to decide whether to hire somebody

As an example of using the above principles in action, here are a few questions we should ask when deciding whether to hire somebody new.

- Do we have excess or insufficient capacity?
  Are we in a cycle where we wish to grow capacity and decrease stress on the team?
- Is the area of expertise for this role the place where we need the most capacity?
- Will this role grow our capacity in the area of highest need?
- Will this role contribute to bringing in more revenue from 2i2c?[^revenue]
  If so, we may update our budget projections before deciding on the financial impact of the hire.
- Can we afford the role, and does signed work fund it?
  Check the [**projected runway** and **committed cost coverage** indicators](#finance:financial-health-indicators) - we should only hire when both look healthy (the dashboard spells out this "should we hire?" logic).
  Assume it will take about 3 months for a new hire to ramp up and contribute at full capacity.

[^revenue]: For example:

    - They will grow our technical capacity, allowing us to bring on more managed hubs.
    - They will grow our outwards presence, giving us more exposure that leads to more managed hubs.
    - They will participate in grant-writing or sales to convert opportunities into funding.

## References

See [these research notes](https://docs.google.com/document/d/134Sgu6y1H06wc0HYXuRW0syI-uvhtyY-Pei4ErMLuJw/edit?usp=sharing) for where some of these ideas came from.
