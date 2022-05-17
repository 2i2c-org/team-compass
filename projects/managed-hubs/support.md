(support:guide)=
# Support process

:::{admonition} In Beta!
:class: warning
We are currently working out our support process.
The content on this page might change over time, and we welcome suggested changes and pull requests!
:::

This section contains information that our team uses to triage, communicate, and resolve {term}`Support Request`s that come from communities.

(support:process)=
## Overview of the support process

Here's a brief overview of our support process:

- A {term}`Community Representative` sends a request to `support@2i2c.org`.
- This is triaged by our {term}`Support Steward` team.
  - They assess whether they can resolve it quickly, and potentially do so.
  - If they cannot resolve it, then we raise this support issue with our engineering team.
- If the issue is an {term}`Incident`
  - We will designate an {term}`Incident Commander` to orchestrate our efforts around the incident.
  - We will prioritize resolving it over everything else.
  - We will open a dedicated [Incident issue](support:incident-response) to track its progress.
  - We will provide regular communication to the {term}`Community Representative` as we investigate and work to resolve the issue.
  - We will notify them once the incident is resolved.
- If the issue is a {term}`Change Request` or {term}`Guidance Request`
  - We will incorporate these requests into our work planning pipeline
  - We will [prioritize with our other work](support:prioritize-requests) based on impact, complexity, and whether we have dedicated funding for this work.
  - For these types of support, each community has a {term}`Support Budget` that defines the hours we can sustainably spend on non-incident support requests.
- When any support issue is resolved, we will communicate with the {term}`Community Representative` to confirm with them.

(support:types)=
## Types of support requests

Below are a few key terms that describe how we categorize Support Requests.

```{glossary}
Support Request
  Any request that a community sends to us via `support@2i2c.org`.
  Support requests are generally un-planned and happen in response to a community needing assistance with something unexpected.
  There are a few main categories of support that we consider, each is described below.

Incident
  An event that significantly degrades the JupyterHub service. Support requests that are related to incidents should be prioritized over all other work items. Here are a few common examples of incidents:

  1. The hub is inaccessible to a significant number of users.
  2. A significant number of users are unable to start their servers.
  3. A significant number of users cannot create Dask Gateway clusters.

  We do not have a limit on the support time we provide related to incidents (as opposed to Change and Guidance requests, which have a {term}`Support Budget`).

  :::{seealso}
  See [](incidents.md) for more information.
  :::

Change Request
  A request for a desired change to a hub's infrastructure that is not related to an incident. For example:
  
  - Changing the user's software environment.
  - Changing the resources available to users.
  - Updating and deploying changes from upstream tools for a community.
  - Making an improvement to open source tools to benefit a community.
  
  Change Requests are generally non-urgent and should not be associated with significant diminished service. They are often things that communities _could_ carry out themselves with the proper guidance and infrastructure setup. We aim to make our hubs as configurable as possible _by the community_ so that we are not on the critical path for things like environment updates.

Guidance Request
  A Support Request that is not tied directly to a change in infrastructure. Sometimes support requests are not tied to a specific change, but a desire to discuss and request guidance. In this case we may set up a meeting to discuss as a group, or have some back-and-forth via support channels.
```

## Roles and team structure

The Support team is a **two-person team** of {term}`Support Steward`s that work together.
Tenure on the support team is **for four weeks**.
Every **two weeks** (generally at the sprint meeting), a Support Steward cycles off the support team, and a new team member joins the team.
The support team rotates through [the “Open Infrastructure Engineering Team” on this page](https://team-compass.2i2c.org/en/latest/about/team.html), in alphabetical order.

The primarily goals of the Support Stewards are:

- Ensure that we meet [our Support Service Level Objectives](docs:objectives:support)
- Carry out [our support process](support:process).
- Act as primary points of contact with {term}`Community Representative`s.
- Trigger an [Incident Response](support:incident-response) if need be.

```{glossary}
Support Steward
  The main point of contact with external stakeholders like {term}`Community Representative`s. Their goal is to provide regular updates to these stakeholders and coordinate with our Incident Response Team to understand what's going on and what is our action plan.

  Common alternate terms: **Customer Liason**, **External Liason**, or **Customer Support**.

Community Representative
  Has the authority to speak on behalf of the communities we work with, and is a point-of-contact for support. Their goal is to represent the community's perspective and needs in support and during Incidents.
  See [](roles:community-representative) for more information.
```

(roles:external)=
## External roles

We also define a few key external roles as a part of our managed service.
These are roles filled by people who are **not 2i2c staff**.

(roles:community-representative)=
### Community Representative

Acts as the primary point of contact for a community, and ensures that the interests of the {term}`Hub Community` are represented in the infrastructure, and that the hub serves their needs.
There must be **one or two community representatives for a given community**.
This role is usually filled by someone that is a member of the hub's community of practice.

Their main responsibilities include:

- The main point of contact between the hub engineer and the {term}`Hub Community`.
- Collect feedback and questions from users on a hub.
- Surface questions and requests to Hub Engineers via support tickets.
- Oversee the [Hub Administrators](roles:hub-administrator)

(roles:hub-administrator)=
### Hub administrator

Trusted community members that perform common administrative operations on a hub that do not require intervention from a [Hub Engineer](roles:hub-engineer).
[Community Representatives](roles:community-representative) are the first Hub Administrators, and they may add new Hub Administrators via the JupyterHub interface.
They are able to add users, start/stop servers, and generally have more control over operations on the hub.

Their responsibilities include:

- Provide support to users of a hub for common problems that don't require a Hub Engineer to resolve.
- Add new users to a hub, including administrative users.
- Surface major issues or requests to the Community Representative(s).

## Communication channels

### External communication

We use these channels for communicating with external stakeholders like Community Representatives:

- **[support@2i2c.org](mailto:support@2i2c.org)** is our point-of-contact for all support-related external communication.
- **[The 2i2c FreshDesk account](https://2i2c.freshdesk.com/)** is where we track all support requests and _respond_ to emails sent to `support@2i2c.org`.
- **{doc}`the "Get Support" page <docs:support>`** provides guidance that communities may follow to get support.

### Internal communication

We have a few channels for communicating around support requests:

- Our [FreshDesk account](https://2i2c.freshdesk.com/a/) allows for internal team communication via the {guilabel}`Add Note` button. This can be useful for sharing quick internal updates.
- [Issues with the {guilabel}`support` label](https://github.com/2i2c-org/infrastructure/issues?q=is%3Aopen+label%3Asupport+sort%3Aupdated-desc) are where we track support requests related to {term}`Change Request`s and {term}`Guidance Request`s.

## Support triage and resolution process

Here is the process that we follow when triaging and resolving support requests.

### Triage process

The goal of the triage phase is to understand the Support Request, decide if it is related to an incident, and choose the appropriate resolution pathway.

This process is carried out in an ongoing basis by the {term}`Support Steward`s.

1. **Monitor our support channels**. We use FreshDesk for all support requests, and the Support Stewards should regularly keep an eye on this account for new requests.
   When a new support requests comes in, move to the next step.
2. **Read and understand**. Within 8 working hours, read the support request and try to understand what action would resolve it.
3. **Decide if there is an incident**. Determine if a request meets {term}`the definition of an incident <Incident>`.
4. **Categorize the Support Ticket** in FreshDesk.
5. **If an Incident**, go to [](support:incident-response).
6. **If not an Incident**, go to [](support:non-incident-response).

(support:non-incident-response)=
### Non-incident response process

1. **Respond within 24 working hours**. Acknowledge receipt of the support request and let the {term}`Community Representative` know about any investigation we have done thus far. 
2. **Spend 30 minutes trying to resolve**. If you believe you can resolve the issue within 30 minutes, try resolving it yourself.
   1. If you resolve the issue, then jump to the "Communicate resolution" step.
   2. If you don't believe you can resolve the issue in 30 minutes, jump to the next step.
3. **Open an engineering issue**. If this is a {term}`Change Request` or {term}`Guidance Request` and you cannot resolve the issue within 30 minutes, then open a support issue for the team to discuss.
   [{bdg-primary}`Open a general issue`](https://github.com/2i2c-org/infrastructure/issues/new?assignees=&labels=&template=01_new-issue.yml) that describes the request and any next steps we should take. Add the {guilabel}`support` label to it.
4. **Communicate status**. Once we have an issue created to track the next steps, send a message to the Community Representative letting them know about the situation and what the next steps will be. Here's a template to help guide you:

   ```
   Hello { NAME }, thanks for sending us your request. We've concluded that
   this is not related to an outage or diminished service, so we'll incorporate
   this request into our team's work planning process. We'll send an update
   when we've got a plan for completing this request.
   ```
5. **Prioritize the request**. Work with our team to decide how we should prioritize this request relative to the other work we need to do. Follow the [how to prioritize Change and Guidance Requests guide](support:prioritize-requests).
6. **Resolve the request**. Our team should work together to prioritize and resolve this request according to its impact.
7.  **Confirm resolution**. Once we have resolved a support request, send a message to the Community Representative to confirm that we believe it is resolved. In FreshDesk, mark the incident as {guilabel}`Resolved`.
8.  **Close the request**. If the Community Representative confirms that their request has been fulfilled, or if we have not gotten a response after 48 working hours, consider this request closed. In FreshDesk, mark the incident as {guilabel}`Closed`.

(support:prioritize-requests)=
## How to prioritize non-incident support requests

For support requests that are not related to {term}`Incident`s, we have more flexibility in when to do the work.
We cannot sustainably prioritize all support requests over our other work, so here is a rough prioritization order to follow:

1. Requests that come with dedicated funding.
1. Requests that impact many communities.
1. Requests that align with our pre-existing goals.
1. Requests that align with an upstream open source project's goals.
1. Requests from communities that haven't used much {term}`Support Budget`.
1. Requests that have a high-impact on a single community.
1. Our other work items
1. Requests from communities that have no more {term}`Support Budget`.

### Support request key terms

The following are other important terms and ideas in the support process.

```{glossary}
Support Budget
  A fixed amount of time that we can spend providing support for each community that we serve. This helps us ensure that we can sustainably serve many communities. Any support request that is **not tied to an {term}`Incident`** will draw from the support budget for that community. If a community requests support beyond their support budget, we may request extra funds to help cover our costs.

  :::{note}
  We currently keep this term intentionally vague, and ask that communities are respectful of our time when making change requests.
  We are investigating the support budget that we should give to each community, and will update here when we have specific numbers in mind. 
  :::
```
