# Key Performance Indicators

We use **Key Performance Indicators** to measure and track our progress and impact as an organization.[^1]
These are tracked along with other important metrics in [our KPIs dashboard site](http://2i2c.org/kpis/).
Here are links to the major sections of that site:

````{grid}
```{grid-item-card} Cloud and hub usage ☁️
:link: https://2i2c.org/kpis/cloud

Our currently running infrastructure and active users over time.
```
```{grid-item-card} Accounting analysis 📈
:link: https://2i2c.org/kpis/finances

Our financial activity, including our costs and revenue broken down by category.
```
```{grid-item-card} Upstream support 💗
:link: https://2i2c.org/kpis/upstream

Our contributions and activity in key upstream communities that we depend on and use.
```
````

[^1]: See [the Fast Forward Playbook on Impact Measurement](https://www.ffwd.org/playbook/impact-measurement/) for an overview of frameworks and metrics to assess impact. Our approach is not quite as complex as this one, as we are intentionally starting simple.


## Goals and principles

Our KPIs have the following goals:

- Signal our _impact_ as an organization
- Signal our _efficiency_ as an organization
- Be _measurable_ either quantitatively or qualitatively
- Be useful for _internal stakeholders_ to guide our strategy and actions
- Be useful for _external stakeholders_ to help them assess our success

As a general rule, the strategic objectives that we set should have an explicit influence on our KPIs.

KPIs **do not** have the following goals:

- Assess individual performance

We currently follow these principles in defining our KPIs:

- **Be measurable at our current capacity**. We should not require extra team members or services in order to measure our KPIs.
- **Start with the basics**. We should not get too-complex in our KPIs because we are new to this and still learning how to use them. We should define three or four at most.
- **Should be automatable**. We should be able to automatically generate our KPIs given data we have about our communities. This is because we have limited capacity to measure and track right now.

## How are KPIs used

We use our KPIs in two ways:

- When defining our strategy and objectives, they should be tied to an expected impact on our KPIs.
- In quarterly reports to external stakeholders we should occasionally highlight our KPIs to provide updates about our progress.

## Impact KPIs

The following KPIs are reflections of our **impact** as an organization.
They represent a positive outcome that is aligned with our mission as a result of our actions.

```{list-table}
:header-rows: 1
:widths: 10 30 10

- - Name
  - Definition
  - Source
- - Communities served
  - The number of unique communities served with at least one hub in the last 6 months.
  - [Our cloud KPIs page](https://2i2c.org/kpis/cloud)
- - Monthly Active Users
  - The number of unique users that have used one of our hubs over a 30-day rolling window.
  - [Our cloud KPIs page](https://2i2c.org/kpis/cloud)
- - MAU percentiles
  - The 10th, 50th, and 90th percentiles of MAUs across all hubs.
  - See this issue to track this effort: https://github.com/2i2c-org/infrastructure/issues/1888
```

## Sustainability KPIs

```{list-table}
:header-rows: 1
:widths: 10 30 10

- - Name
  - Definition
  - Source
- - Monthly revenue
  - Monthly revenue, broken down by category (grants, development contracts, cloud service contracts)
  - [Accounting KPIs page](https://2i2c.org/kpis/finances)
- - Monthly operational costs
  - Monthly operational costs, broken down by category (engineering, partnerships and community, executive, fiscal fee, services)
  - [Accounting KPIs page](https://2i2c.org/kpis/finances)
```

## Aspirational KPIs

There are a few ways in which we'd like to expand the use of KPIs as we learn more.
Here is a quick overview for future reference:

### Area-specific KPIs

Our KPIs are currently defined at an organizational level, but most decisions about strategy and policy happen within a functional area (e.g. `partnerships`).
We may wish to define KPIs within functional areas as well in order to make it easier to tie strategy and policy to an impact on a specific KPI.

For example:

**Engineering KPIs**

- Cloud cost per hub user, broken down by hub type (education vs. research): for each hub, `monthly cloud costs / monthly active users`.
- `issues closed - issues opened`.
- Average time to completing an issue once somebody is assigned.
- Average time it takes to deploy a new hub or cluster from scratch.

**Community guidance KPIs**

- FreshDesk Turnaround Time
- Education Communities: `nbgitpuller` clicks per hub

### Qualitative KPIs

Our metrics above are all "automatable" and quantitative due to resource constraints.
However we recognize that much of our impact will be _qualitative_ rather than quantitative.
For example, we might run _satisfaction surveys_ with our communities to see how we are doing and ask where we can improve.
We will need to grow capacity and skills at running surveys or interviews at-scale in order to assess these more qualitative KPIs

### Upstream KPIs

All of our KPIs thus far are focused on the communities we directly serve with cloud infrastructure.
However, a secondary aspect of 2i2c's mission is to support open communities that underlie this infrastructure.
We commit to doing most of our work by performing upstream contributions, and to support upstream projects in non-coding ways as well.
While we do not currently track our upstream contributions, we aspire to track this information automatically as part of our self-assessment.

```{note}
We track some upstream activity in [our upstream KPIs page](https://2i2c.org/kpis/upstream).
```

### Impact-centric KPIs

Our KPIs are currently fairly basic, because they are immediately measurable and quantifiable.
They are largely a reflection of _usage_, though this is not the same thing as _impact_.
Below are some harder-to-measure KPIs that we may consider for future strategic development:

- Publications or presentations that have been generated as a result of use of our hubs
- Communities served that come from organizations or backgrounds that are historically marginalized.
- Cost reduction given to these communities in a way that is still sustainable for 2i2c.