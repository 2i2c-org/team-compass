
# Things to know before an incident

(incidents:what)=
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

```{important}
Here is a list of [Important Pagerduty pages to know about](https://infrastructure.2i2c.org/topic/monitoring-alerting/alerting/#important-pagerduty-pages-to-know-about).
```