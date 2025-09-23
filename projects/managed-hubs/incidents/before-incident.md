
# Things to know before an incident

## What is an incident

An incident is an unplanned interruption to the hub service, or reduction in the quality of it. It is an external representation of an outage.
The definition of an outage and the outage categories are tracked in more detail in the [Outages documentation](https://2i2c-pilot-documentation--272.org.readthedocs.build/admin/topics/outages/#outages).

```{important}
An incident, as defined in this document, is distinct from a "PagerDuty Incident"! The later is is a construct in PagerDuty that can represent alerts of any severity and priority. A PagerDuty Incident may or may not correspond to an actual incident as defined here.

Only P1 incidents in PagerDuty correspond to outages and trigger the incident response process as defined here.
```

## When is the incident response process triggered

Whenever an outage has been identified, the incident response process should be triggered by the person who identified the outage.
If they are part of the Infrastructure Engineering team, they become the {term}`Incident Responder`, otherwise they should notify the Infrastructure Engineering team via the `#pagerduty-notifications` Slack channel or the `#product-and-services-team` channel.

## Communication channels

### External communication

- The person filling in the {term}`External Liason` role acts as the primary point of communication with external stakeholders like the {term}`Community Representative`s. This is typically the {term}`Support Triager`. But, in their absence, this role becomes the responsibility of the {term}`Incident Responder` 
- The communication happens via Freshdesk

(incidents:communications)=
### Internal communication

- A channel *dedicated* to each incident must be created through pagerduty once an incident has been identified and given a P1 priority. This is where most of the
  discussion about the incident should happen.
- [`2i2c-org.pagerduty.com`](https://2i2c-org.pagerduty.com/) is a dashboard for managing incidents.
  This is the "source of truth" for any active or historical incidents.
- [The `#pagerduty-notifications` Slack channel](https://2i2c.slack.com/archives/C041E05LVHB) is *primarily* used to trigger
  new incidents and control pagerduty in other ways. Discussion of *specific* incidents should not happen here.

