# Process for managing Cloud Costs

## What are Cloud costs overruns?

-   Infrastructure costs that communities incur outside of an active service agreements
-   Costs incurred by 2i2c because invoices cannot (or have not) been sent to communities
-   In general, any cloud costs that 2i2c can’t recoup from a community

# Cloud costs monitoring process

2i2c’s cloud costs monitoring process consists of two phases.

## Phase 1: Monitoring and reducing cost runaways

Preventing cost runaway involves actively responding to **cloud cost alerts** and **escalated community concerns** (from Freshdesk).

### Cloud cost alerts

The P&S team configures public clouds (e.g. AWS, Azure) systems to raise usage alarms at specific thresholds.

When cloud cost alerts are triggered, these are the steps that should taken by the P&S team:

1. When a cloud account is set up, we set a threshold for sending alerts
2. If an account’s forecast (not actual) cost goes above the threshold, an alert email is sent to [support@2i2c.org](mailto:support@2i2c.org)
3. The P&S support triager reviews alert emails
4. Excessive spikes (typically >20%, open to the triager’s judgement) will trigger a formal investigation by a member of the P&S team and where necessary a report is sent to the impacted community
5. In the event of a cost overrun, the Delivery manager will decide if 2i2c will consume the cost and not pass it down to the community
6. DE will communicate to CS&S if a discount should be applied to the communities next invoice

### Escalated community concerns

Community escalated cost concerns should be handled in a similar manner to cloud cost alerts.

1. A message is sent to FreshDesk (by a concerned community)
2. P&S support triagers trigger a discussion within P&S (and BD where necessary)
3. The P&S team will investigate the cost concern and advise the DE team of possible next steps. This should include the following information:
    1. Is this a legitimate cost overrun
    2. Is 2i2c at fault
    3. Does P&S believe that a discount should be issued
4. In the event of a cost overrun, the Delivery manager will decide if 2i2c will consume the cost and not pass it down to the community
5. In the event of a cost overrun, P&S support triagers will communicate costs/discount implications (and root causes) to impacted communities
6. DE will communicate to CS&S if a discount should be applied to the communities next invoice

## Phase 2: Invoicing communities

Reporting and invoicing consist of getting the cloud costs from our different platforms, assessing for anomalies and dispatching adjusted costs for invoicing.

This phase involves the following steps:

1. **Gather costs**: Cloud costs are gathered by the P&S team on a monthly basis.
2. **Review costs**: These costs are communicated to DE for review via the _#billing_ slack channel. DE is responsible for:
    1. Flagging anomalies to P&S
    2. Triggering cost anomaly investigations
    3. Coordinating discounts with CS&S
3. **Dispatch for invoicing**: Cloud costs are sent to CS&S for invoicing. 4. This is done by consolidating the CSV files from P&S to a google cloud sheet 5. P&S is notified on Asana that the cloud costs are ready for invoicing

# Decommissioning hubs

In some extreme cases, 2i2c will have to discontinue services to communities.

The process that governs these decisions is below:

1. The BD team (and representatives from DB and P&S) will review which services agreements have lapsed and are still consuming cloud services in the Biz Dev Sales Sync meeting
2. DE and P&S team members will review Engagements in the P&S Project management meeting, identifying hubs that are candidates for decommission based
    1. They will then notify the BD team via the Biz Dev Sales sync meeting
3. The BD team is responsible for extending the hub decommissioning date (by 2-week increments) to facilitate renewal conversations in those instances where a service agreement has lapsed.
4. If communities have lapsed (or missing) services agreements for more than 6-weeks and are still receiving cloud services for that period of time, the BDL will make a decision if their cloud services should be terminated.
