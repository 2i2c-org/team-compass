
# Things to know before an incident

(incidents:what)=
## What is an incident

An incident is an unplanned interruption to the hub service, or reduction in the quality of it. It is an external representation of an outage.
The definition of an outage and the outage categories are tracked in more detail in the [Outages documentation](https://2i2c-pilot-documentation--272.org.readthedocs.build/admin/topics/outages/#outages).

```{important}
An incident, as defined in this document, is distinct from a "PagerDuty Incident"! The later is is a construct in PagerDuty that can represent alerts of any severity and priority. A PagerDuty Incident may or may not correspond to an actual incident as defined here.

**Only P1 incidents in PagerDuty correspond to outages and trigger the incident response process as defined here.**
```

```{note}
Here is a list of [Important Pagerduty pages to know about](https://infrastructure.2i2c.org/topic/monitoring-alerting/alerting/#important-pagerduty-pages-to-know-about).
```

## When is the incident response process triggered

Whenever an outage has been identified, the incident response process should be triggered by the person who identified the outage.
If they are part of the Infrastructure Engineering team, they become the {term}`Incident Responder`, otherwise they should notify the Infrastructure Engineering team via the `#pagerduty-notifications` Slack channel or the `#product-and-services-team` channel.

## The incident team
A team is formed when the incident response process is triggered. The goal of the team is to collectively and quickly resolve the incident.

The team is **currently formed organically** with the the available members of the Infrastructure Engineering team, and may include other members of the 2i2c team as-needed. A rough way to approximate this team is _"the people that have communicated in internal and external channels to resolve an incident."_

This team needs to fulfill three roles, which ideally are filled by different people, but can be same person.

- An {term}`Incident Responder`
- The {term}`Communication Liaison`
- One or more {term}`Subject Matter Experts`

### Roles and responsibilities

```{glossary}
Incident Responder
  The Incident Responder has the authority to plan and delegate action to others on the team. 
  Their **responsibility** is to:
    - solve or temporally mitigate the incident, either themselves or with the help of the available team members
    - be the {term}`Source of Truth` about the current state and action plan surrounding the incident
    - review the {term}`Incident Report` after the incident is resolved

Communication Liaison
  The person that communicates with external stakeholders about an Incident. This is typically the {term}`Support Triager`
  Their **responsibility** is to:
    - communicate the status of the incident
    - send updates about our current thinking and what we have tried, and any expected changes coming
    - write the {term}`Incident Report` after the incident is resolved

Subject Matter Expert
Subject Matter Experts
  A team member with expertise in an area of relevance to an Incident. They should be pulled in to the Response Team as-needed by the {term}`Incident Responder`. 
  Their **responsibility** is to:
    - help resolve the incident by providing expertise and taking actions
    - inform the {term}`Incident Responder` about their plan/actions/motivations either during or after the incident so they  can  actions as-directed by the {term}- - the Tech Lead must always be included as a Subject Matter Expert, as they have unique expertise in solving certain problems and are ultimately accountable for successful incident resolution.
```

### Accountability

Each of the roles is accountable for their responsibilities, and the {role}`Technology Lead` and the {role}`Engineering Manager` are ultimately accountable for the success of the incident response and how well the process has been followed.
