# Paying out past Incident Report debt

Each sprint, the Infrastructure Engineering team is scheduled to take the following actions, for **unpublished outages that have happened between September 1st 2025 and February 10th 2026** until we have paid out all debt:

- handle incident reports
- handle action items and incident resolution
- archive outage-related Slack channels

## Process

Every Monday, before a Sprint starts, two issues with the `recurrent` label will be opened in https://github.com/2i2c-org/infrastructure and be added to the `Up Next` column of our P&S sprint board.

### The `"Pay out past incident reporting debt"`

This is the responsability of the Infrastructure Engineers. Each of them must choose at least one activity from the following list and follow the steps there.

#### Handle incident report review
Steps:

1. review at least one of the [`Draft` incidents in PagerDuty](https://2i2c-org.pagerduty.com/postmortems), 
2. edit it and change its status to `Reviewed` when you are done
3. let the owner know in the `#post-outage-actions` Slack channel

#### Handle incident report writing
1. get the list of P1 incidents by sorting [the list of incidents](https://2i2c-org.pagerduty.com/incidents?status=acknowledged%2Ctriggered%2Cresolved) based on priority (start by looking at the past two months)
2. compare this list with the list of Postmortems
3. check which incidents do not have postmortems
4. write up any missing Incident Report and save it as a PD draft postmortem
5. let the team know in the `#post-outage-actions` Slack channel

#### Archive outage-related Slack channels
1. review the list of [PD postmortems that are marked as `Closed`](https://2i2c-org.pagerduty.com/postmortems)
2. if any of these still have Slack channels that have not been archived, archive them now

### The `"Review past outage resolution and actions"`

Each sprint, the Team Lead and the Engineering Manager are scheduled to review the resolution and action items of the outages that have happened **between September 1st 2025 and February 10th 2026** until we have paid out all debt. Each of them must choose at least one activity from the following list and follow the steps there.


#### Handle action items and incident resolution**

1. review the resolution and the action items of a PD postmortem marked as [`Reviewed` in PD postmortems](https://2i2c-org.pagerduty.com/postmortems)
2. review the resolution and the action items of an incident posted in https://github.com/2i2c-org/incident-reports in the specified period
3. let the team know in the `#post-outage-actions` Slack channel and ask any clarifying questions

#### Publish incident reports**
1. open a PR in https://github.com/2i2c-org/incident-reports for all [PD postmortems marked as `Closed`](https://2i2c-org.pagerduty.com/postmortems)
2. let the team know in the `#post-outage-actions` Slack channel and ask any clarifying questions