(support:guide)=
# Support team guide

:::{admonition} In Beta!
:class: warning
We are currently working out our support process.
The content on this page might change over time, and we welcome suggested changes and pull requests!
:::

This section contains information that our team uses to triage, communicate, and resolve {term}`Support Request`s that come from communities.

(support:process)=
## Support process overview

Here's a brief overview of our support process:

- A {term}`Community Representative` sends a request to `support@2i2c.org`.
- This is triaged by our [Support Stewards](roles:support-steward).
  - They assess whether they can resolve it quickly, and potentially do so.
  - If they cannot resolve it, then we raise this support issue with our engineering team.
- If the issue is an {term}`Incident`
  - We will prioritize resolving it over everything else.
  - We will open a dedicated [Incident issue](support:incident-response) to track its progress.
  - We will provide regular communication to the {term}`Community Representative` as we investigate and work to resolve the issue.
  - We will notify them once the incident is resolved.
- If the issue is a {term}`Change Request` or {term}`Guidance Request`
  - We will incorporate these requests into our work planning pipeline
  - We will [prioritize with our other work](support:prioritize-requests) based on impact, complexity, and whether we have dedicated funding for this work.
  - For these types of support, each community has a {term}`Support Budget` that defines the hours we can sustainably spend on non-incident support requests.
- When any support issue is resolved, we will communicate with the {term}`Community Representative` to confirm with them.

## Support terms

### Types of support requests

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

Change Request
  A Support Request for a desired change to a hub's infrastructure, that is not related to an incident. For example:
  
  - Changing the user's software environment.
  - Changing the resources available to users.
  - Updating and deploying changes from upstream tools for a community.
  - Making an improvement to open source tools to benefit a community.
  
  Change Requests are generally non-urgent and should not be associated with significant diminished service. They are often things that communities _could_ carry out themselves with the proper guidance and infrastructure setup. We aim to make our hubs as configurable as possible _by the community_ so that we are not on the critical path for things like environment updates.

Guidance Request
  A Support Request that is not tied directly to a change in infrastructure. Sometimes support requests are not tied to a specific change, but a desire to discuss and request guidance. In this case we may set up a meeting to discuss as a group, or have some back-and-forth via support channels.
```

### Other support request terms

The following are other important terms and ideas in the support process.

```{glossary}
Support Budget
  A fixed amount of time that we can spend providing support for each community that we serve. This helps us ensure that we can sustainably serve many communities. Any support request that is **not tied to an {term}`Incident`** will draw from the support budget for that community. If a community requests support beyond their support budget, we may request extra funds to help cover our costs.

  :::{note}
  We currently keep this term intentionally vague, and ask that communities are respectful of our time when making change requests.
  We are investigating the support budget that we should give to each community, and will update here when we have specific numbers in mind. 
  :::

Community Representative
  A person that has the authority to speak on behalf of the communities we work with, and is a point-of-contact for support.
  Communities may have multiple community representatives, provided they all have the authority to make decisions on behalf of the community.
  See [](roles:community-representative) for more information.

Incident Report
  A document that describes what went wrong during an incident and what we'll do to avoid it in the future. When we have an {term}`Incident`, we create an Incident Report issue.
  This helps us explain what went wrong, and directs actions to avoid the incident in the future. Its goal is to identify improvements to process, technology, and team dynamics that can avoid incidents like this in the future. It is **not** meant to point fingers at anybody and care should be taken to avoid making it seem like any one person is at fault[^post-mortems].
```

[^post-mortems]: See the [Google SRE post-mortem culture](https://sre.google/sre-book/postmortem-culture/) and the [Blameless guide to post-mortems](https://www.blameless.com/sre/what-are-blameless-postmortems-do-they-work-how) for some guidelines.

## Support team structure

The Support Team is a **two-person team** of Support Stewards that work together.
Tenure on the support team is **for four weeks**.
Every **two weeks** (generally at the sprint meeting), a Support Steward cycles off the support team, and a new team member joins the team.
The support team rotates through [the “Open Infrastructure Engineering Team” on this page](https://team-compass.2i2c.org/en/latest/about/team.html), in alphabetical order.

The primarily goals of the Support Stewards are:

- Ensure that we meet [our Support Service Level Objectives](docs:objectives:support)
- Carry out [our support process](support:process).
- Act as primary points of contact with {term}`Community Representative`s.
- Trigger an [Incident Response](support:incident-response) if need be.


## Communication channels

### External communication

We use these channels for communicating with external stakeholders like Community Representatives:

- **[`support@2i2c.org`](mailto:support@2i2c.org)** is our point-of-contact for all support-related external communication.
- **[The 2i2c FreshDesk account](https://2i2c.freshdesk.com/)** is where we track all support requests and _respond_ to emails sent to `support@2i2c.org`.
- **{doc}`the "Get Support" page <docs:support>`** provides guidance that communities may follow to get support.

### Internal communication

We have a few channels for communicating around support requests:

- Our [FreshDesk account](https://2i2c.freshdesk.com/a/) allows for internal team communication via the {guilabel}`Add Note` button. This can be useful for sharing quick internal updates.
- The Slack channel [{guilabel}`#support-freshdesk`](https://2i2c.slack.com/archives/C028WU9PFBN) contains real-time communication about support issues. Use this to signal-boost support requests related to {term}`Incident`s.
- [Issues with the {guilabel}`support` label](https://github.com/2i2c-org/infrastructure/issues?q=is%3Aopen+label%3Asupport+sort%3Aupdated-desc) are where we track support requests related to {term}`Change Request`s and {term}`Guidance Request`s.
- [Issues with the {guilabel}`incident` label](https://github.com/2i2c-org/infrastructure/issues?q=is%3Aopen+label%3A%22type%3A+Hub+Incident%22+sort%3Aupdated-desc) are where we track progress when [resolving incidents](support:incident-response).

## Support triage and resolution process

Here is the process that we follow when triaging and resolving support requests.

### Triage process

The goal of the triage phase is to understand the Support Request, decide if it is related to an incident, and choose the appropriate resolution pathway.

1. **Read and understand**. Within 8 working hours, read the support request and try to understand what action would resolve it.
2. **Decide if there is an incident**. Determine if a request meets {term}`the definition of an incident <Incident>`.
3. **Categorize the Support Ticket** in FreshDesk.
4. **If an Incident**, go to [](support:incident-response).
5. **If not an Incident**, go to [](support:non-incident-response).

(support:incident-response)=
## Incident response process

Incidents are a special kind of support ticket, because they are related to degraded service that immediately impacts communities.
We prioritize the resolution of incidents above all other kinds of work, and have a special process for tracking conversation and progress with them.

Here is the process that we follow for incidents:

1. **Acknowledge the incident**. Communicate with the Community Representative that there is an incident. Here is a template to get started:
   
   ```
   Hello { NAME }, we have investigated this request and have concluded that
   it is related to an incident that is causing diminished service for your
   community.
   
   We believe that this incident is related to { CONTEXT HERE } and will
   investigate further on next actions. Information about our incident
   response process can be found [in our team support documentation](https://team-compass.2i2c.org/en/latest/projects/managed-hubs/support.html).
 
   We'll prioritize resolving this incident over our other work, and
   will communicate with you throughout our attempts to resolve it.
   We might be in touch with requests for clarifications if needed.
   ```
2. **Open an incident issue**. For each {term}`Incident` we create a dedicated issue to track its progress. [{bdg-primary}`open an incident issue`](https://github.com/2i2c-org/infrastructure/issues/new?assignees=&labels=type%3A+Hub+Incident%2Csupport&template=3_incident-report.md&title=%5BIncident%5D+%7B%7B+TITLE+%7D%7D) and notify our engineering team via Slack.
3. **If you can resolve in 30 minutes**, try doing so.
4. **If you cannot resolve in 30 minutes**, ping our engineering team and our Project Manager in the {guilabel}`#support-freshdesk` channel so that they are aware of the incident.
5. **Investigate and resolve the incident**. Follow the structure of the incident issue you opened in the step above.
6. **Communicate every few hours**. Provide periodic updates to communities as we attempt to resolve the incident. Here is a template to get started:

   ```
   Hello { NAME }, this is a quick update on our progress resolving
   your incident.

   We believe the problem is { XXX } and are investigating { YYY }
   to resolve it. We will keep you updated as we continue to make progress.
   Please let us know if you have had more reports of issues,
   or reports that your issues have gone away.
   ```
7. **Communicate when the incident is resolved**. When we believe the incident is resolved, communicate with the Community Representative that things should be back to normal. Mark the FreshDesk ticket as {guilabel}`Resolved`.
8. **Fill in the {term}`Incident Report`**. Do this in partnership with the team that helped resolve the issue.
9. **Close the incident ticket**. Once we have confirmation from the community (or no response after 48 working hours), and have filled in the incident {term}`Incident Report`, then close the incident by:
   - Closing the incident issue on GitHub
   - Marking the FreshDesk ticket as {guilabel}`Closed`.

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
