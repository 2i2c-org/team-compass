# Key Performance Indicators for BD

2i2c's business plan involves (1) maintain our current customer base, (2) grow overall revenue, and (3) find a repeatable way to acquire new customers. We define three _scalar_ time-series as key performance indicators (KPIs) using systems that also provide insight into business performance over time. 

```{list-table} Key Performance Indicators
:header-rows: 1
:widths: 20 25 40 15
:name: kpi-table

* - Metric
  - Definition
  - Description
  - Target
* - (6-Month Backward) **Retention KPI**
  - $ Renewal_6 = 1 - Churn_6 $
  - $Churn_6$ is the ratio of customers who discontinue their membership or have stopped paying over the previous six months. $Renewal_6$ is the ratio of customers retained over the previous six months.
  - `>0.8`
* - (6-Month Forward) **Revenue KPI**
  - $FMRR_6 = SUM(FMRR([\mbox{Now}, \mbox{Now} + \mbox{6 months}]))$
  - Expected total revenue over the next 6 months. It is a _leading revenue indicator_ based on assumptions about conversion rates.
  - TBD
* - **Customer Acquisition KPI**
  - $LQR = \frac{\#[\mbox{Qualified Leads}]}{\#[\mbox{Leads}]}$
  - Ratio of qualified leads to leads generated from an experiment or campaign. This indicator will be used to compare different approaches we try to acquire customers.
  - 0.15
```

The following sections describe these KPIs in more detail, provide the rationale for why they are important to 2i2c, and contextualize their role in 2i2c's sales system.

## Overview of Revenue KPIs

**What** will we measure and forecast? We will measure revenue from current contracts and forecast expected revenue from opportunities in our sales pipeline.

**Why is revenue an important indicator for 2i2c and the BD team?** Revenue is vitally important for 2i2c's sustainability. Revenue is an indicator of the BD team's performance.

**Will what we measure address the imporant answers to "why" we want to track revenue?** Yes. We will build tools that convert information about opportunities captured with our CRM. These tools will spread out the total revenue value of each opportunity across the months in the opportunity's interval of service. The likelihood that an opportunity will convert into actual revenue will be defined based on its stage in the sales pipeline. KPIs can be generated from these tools to track expected total revenue as an indicator of business performance. The tools are designed to provide insights for sustainability planning and steering the BD team. 

:::{note} **Forecast Monthly Recurring Revenue (FMRR)** formula
The **Forecast Monthly Recurring Revenue (FMRR)** is defined by the formula

$$
FMRR = CMRR + \rho ({\mbox{Renewal-}}MRR) + \eta ({\mbox{New-}}MRR)
$$

- FMRR presents the sales pipeline value in expected revenue spread out across all the months of 2i2c's past and future. 
- FMRR can be localized in time by restricting attention to months between a start and end date and aggregating all the contributions into a single number. For example, the expected total revenue over the next six months

  $$
  FMRR_6 = SUM(FMRR([\mbox{Now}, \mbox{Now} + \mbox{6 months}])).
  $$
:::

The ingredients in the FMRR formula are defined and explained below. 

### Contracted Monthly Recurring Revenue (CMRR)

Opportunities that convert to `Closed-Won` stage are associated with an executed agreement. The agreement includes **contracted revenue**, a **service interval** `[start-date, end-date]`, and a **revenue collection schedule** for membership fees, usage fees and cloud costs recovery. Member fees are collected at the start of the service interval. Monthly usage fees are collected during the service interval. Cloud costs are recovered after each month of service. For example, an Advanced Tier sale yields a $15,000 membership fee shortly after the agreement is signed, usage fees collected monthly based on a count of monthly active users (MAU), and recovery of cloud costs. 

MAU counts are not known in advanced but can be estimated using data collected when the opportunity was qualified. The `Total Value` of the opportunity is the membership fee plus the estimated total of usage fees during the service interval. 2i2c will track Contracted Monthly Recurring Revenue (**CMRR**) by amortizing the `Total Value` evenly across all months in the service interval and accumulating these amounts across all executed agreements into buckets for each month. CMRR spreads contracted revenue across time. The different ways that contracted revenue arrive may affect 2i2c's cash flow. 

CMRR is mostly a _lagging indicator_ of lead generation and sales cycle efficiency. CMRR is logged late in the sales pipeline when the opportunity converts to `Closed-Won` stage and is "baked into the future". The contribution to CMRR from any given opportunity is zero for all months to the future of that opportunity's service interval. CMRR has a future revenue cliff. 


### Forecast Monthly Recurring Revenue (FMRR)

The first and most immediate step in 2i2c's [business development plan](https://hackmd.io/jH8BWPccRe-OYhpjeVrguA?view) is to **maintain our current base of customers**. While mostly a lagging indicator, CMRR foreshadows **renewal revenue** that is not "baked into the future" but instead requires 2i2c to "take actions to manifest a desired outcome". 2i2c needs to implement a _team-wide strategy to ensure current agreements renew with a high renewal conversion rate_ (>80%). The **renewal conversion rate is a team-wide KPI**.    

Opportunities flow through [stages in the sales pipeline](https://hackmd.io/S6d1JGTvSVei-pPMY-vN7Q) to `Closed-Won`.

A Prospect associated with a previous engagement will be classifed as a _Renewal Prospect_. Prospects without a previous engagement will be classified as a _New Prospect_. 

```{mermaid}
flowchart LR
A[Lead] --> |Qualify| B[Renewal Prospect]
B -->|...| E[Closed-Won]
B --> F[Closed-Lost]
A --> |Qualify| C[New Prospect]
C -->|...| E[Closed-Won]
C --> F
```

**Figure 1: Leads propagate through the sales pipeline toward `Closed-Won` or `Closed-Lost` stage. This diagram concentrates attention on the transition from `Prospect` to the final stage. Other stages of the sales pipeline are supressed under the `...` prior to arrival at `Closed-Won` or `Closed-Lost`.**


A Prospect is a qualified opportunity tracked in our CRM with data (`Total-Value`, `[Target-Start-Date, Target-End-Date]`) that can be amortized into MRR contributions across the target service interval. A Renewal Prospect is expected convert to `closed-won` with high **renewal prospect conversion rate** $\rho$ (>0.8) and an estimated contribution to future MRR of $\rho$ MRR for each of the months in the target service interval. A New Prospect is expected to convert to `closed-won` with a lower **new prospect conversion rate** $\eta$ (~0.3) with forecast contribution to future MRR of $\eta$ MRR is each of the months in the target service interval. 

> These conversion rates are guesses as of 2025-03-25 and need to be measured. See below.

**What** the BD team needs?
+ An "opportunities table" for collecting data on opportunities as they are qualified and move through the stages of the sales pipeline.
+ An "amortization logic" that associates an array of `[Months X MRR]`  for Months in an opportunity's service interval `[Start-Date, End-Date]` with the MRR contribution determined by `Total-Value` divided by the number of Months in the service interval. 
+ The FMRR object, an array of `[Months X MRR]` collected from all opportunities with metadata (opportunity's stage, conversion rates,...).
    + The ability to localize the FMRR object in various ways (e.g. next six months).
    + The ability to roll-up the FMRR object in various says (e.g. total expected revenue in FMRR over next six months).
    + The ability to visualize FMRR in various ways to support decision-making.

## Overview of Pipeline Conversion and Velocity KPIs

**What** will we measure? We will use data gathered in our CRM to measure the rates of conversion of opportunties as they evolve through the stages in the sales pipeline. We will measure the time that opportunities spend in each stage of the sales pipeline, a measure of sales velocity.  

**Why** are conversion rates and sales velocity important indicators for the BD team? Our plan to grow 2i2c's business involves maintaining our current customers and adding new customers. Maintaining our customer base involves carefully tracking renewals and taking actions to avoid losing any customers. We will run marketing experiments or campaigns to generate leads. The effectiveness of these campaigns as strategies to acquire new customers is measured with conversion rates. We measure sales velocity so that we can take actions to decrease the time between first contact and first revenue. 

The Renewal Prospect Conversion rate $\rho$ and the New Prospect Conversion Rate $\eta$ quantify how likely a given prospect will convert to `Closed-Won` and contribute revenue. The actual sales pipeline is more fine-grained as shown in [this more exploded view](https://hackmd.io/S6d1JGTvSVei-pPMY-vN7Q). Each prospect's journey through the ensuing stages toward `Closed-Won` or landing in `Closed-Lost`. These journeys are packed with information that 2i2c should use for learning about our business operation. Pipeline Conversion is a way to systematically collect the information as opportunities move through the sales pipeline to support decision-making. For example, [Sankey diagrams](https://hackmd.io/_uploads/HJ15Tfkaye.png) -- visualizations of the flow and conversion rates between each stage -- provide insights into actions 2i2c can take to improve our business.





**What** is Pipeline Velocity and **why** is it an important indicator for the BD team? Pipeline Velocity is a way to systematically collect the information on the time an opportunity spends in each stage of the sales pipeline. 2i2c and our BD team need this information to identify and remove inefficiencies in the sales pipeline. [GANTT-style diagrams](https://hackmd.io/_uploads/H1rARGJaye.png) provide visualizations of opportunities evolving through stages across time. [Bottleneck Summaries](https://hackmd.io/_uploads/BymIWQyakl.png) aggregate across all opportunities into a visualization that shows average time spent in each stage. 

### Example: Lead Generation Experiments

2i2c will run experiments (e.g. market 2i2c by participating in a conference, Facebook ad campaign, transactional email blasts) to generate leads. 2i2c will use Pipeline Conversion and Pipeline Velocity to **measure the business outcomes of lead generation experiments**. 2i2c might spend \$5,000 and 6 employee-days to participate in an RSE event to generate a cohort `RSE25Leads` of opportunties. 2i2c might spend \$750 on a Facebook ad campaign targeting "Vice Provosts Teaching and Learning" to generate another cohort `FBProvosts25Leads` of opportunities. By tracking the business outcomes of lead generation experiments, 2i2c can use the scientific method to find a robust way to acquire customers at scale. 

### Example: Improving Renewal Prospect Conversion Rate based on engagement

Current customers who are paying and experiencing value are 2i2c's source of most probably future revenue. The first thrust of 2i2c's business development plan is to **maintain our base of current customers**. Churn events -- engagements that fail to renew -- are signals of warning to the entire 2i2c team. 

P&S is developing a time-series "engagement metric" based on hub usage data over time. The "engagement metric" is expected to serve as a proxy for _value delivered_ to a hub user community over time. 

2i2c may learn that engagements with low "engagement metric" are more likely to not renew. 2i2c can then plan interventions to help communities with low "engagement metric" to create improved conditions for renewal.

**What** the BD team needs?

+ An "event log" or a "sales stage transitions table" that systematically records actions taken to change data in our CRM. This log should record the transition from one stage type to another stage type, when that change of stage type was recorded, and which user implemented that change. 
+ Various methods for converting the "event log" data and localizations of the event log into conversion rates between stages. 
+ Various methods for converting the "event log" data or localizations of the event log into "time spent" or velocity information. 
+ Various visualizations like Sankey diagrams and GANTT-style charts.  