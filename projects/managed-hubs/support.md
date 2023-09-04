(support:guide)=
# Support process

:::{admonition} In Beta!
:class: warning
We are currently working out our support process.
The content on this page might change over time, and we welcome suggested changes and pull requests!
:::

This section contains information that our team uses to triage, communicate, and resolve {term}`Support Requests` that come from communities.

Currently, Engineering has the authority to design the system of roles and processes that defines "support at 2i2c", and to advocate for the resources needed to fill those roles. This will naturally be done in collaboration with others in 2i2c, but Engineering leads the effort and has an outsized role in the decision-making.

(support:process)=
## Overview of the support process

Here's a brief overview of our support process[^github-support-issues]:

[^github-support-issues]: We had a lot of discussion around various support and operations systems to take as inspiration. [This GitHub Issue](https://github.com/2i2c-org/infrastructure/issues/1068) has a lot of useful discussion, including a few write-ups of specific support systems to use as inspiration ([example one](https://github.com/2i2c-org/infrastructure/issues/1068#issuecomment-1063138772) [example two](https://github.com/2i2c-org/infrastructure/issues/1068#issuecomment-1063516429))

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
Support Requests
  Any request that a community sends to us via `support@2i2c.org`.
  Support requests are generally un-planned and happen in response to a community needing assistance with something unexpected.
  There are a few main categories of support that we consider, each is described below.

Incident
Incidents
  An event that significantly degrades the JupyterHub service. Support requests that are related to incidents should be prioritized over all other work items.

  [](incidents:what) defines the kind of incidents we respond to via PagerDuty and consider immediate issues to be resolved.

  We do not have a limit on the support time we provide related to incidents (as opposed to Change and Guidance requests, which have a {term}`Support Budget`).

  :::{seealso}
  See [](incidents.md) for more information.
  :::

Change Request
Change Requests
  A request for a desired change to a hub's infrastructure that is not related to an incident. For example:

  - Changing the user's software environment.
  - Changing the resources available to users.
  - Updating and deploying changes from upstream tools for a community.
  - Making an improvement to open source tools to benefit a community.

  Change Requests are generally non-urgent and should not be associated with significant diminished service. They are often things that communities _could_ carry out themselves with the proper guidance and infrastructure setup. We aim to make our hubs as configurable as possible _by the community_ so that we are not on the critical path for things like environment updates.

Guidance Request
Guidance Requests
  A Support Request that is not tied directly to a change in infrastructure. Sometimes support requests are not tied to a specific change, but a desire to discuss and request guidance. In this case we may set up a meeting to discuss as a group, or have some back-and-forth via support channels.
```

## Roles and team structure

Supporting a 2i2c hub is a collaborative process between 2i2c and the community we serve.

The **Support Team** is one of the main teams in our **Managed JupyterHub Service Team**.

This consists of three main roles: {term}`Support Stewards`, {term}`Community Representatives`, and {term}`Hub Administrators`.

```{glossary}
Support Steward
Support Stewards
  A **two-person team** of {term}`Support Stewards` work together to triage and communicate with all external support requests.
  Tenure on the support team is **for four weeks**.
  Every **two weeks** (generally at the sprint meeting), a Support Steward cycles off the support team, and a new team member joins the team.
  The support team rotates through [the “Open Infrastructure Engineering Team” on this page](https://team-compass.2i2c.org/en/latest/reference/team.html), in alphabetical order.

  The primary responsibilities of the Support Stewards are:

  - Ensure that we meet {ref}`our Support Service Level Objectives <docs:objectives:support>`.
  - Carry out [our support process](support:process).
  - Act as primary points of contact with {term}`Community Representative`s.
  - Trigger an [Incident Response](support:incident-response) if need be.

  Common alternate terms: **Customer Liason**, **External Liason**, or **Customer Support**.

Community Representative
Community Representatives
  See [the service documentation](https://docs.2i2c.org/en/latest/about/service/shared-responsibility.html#std-role-Community-Representative).

Hub Administrator
Hub Administrators
  See [the service documentation](https://docs.2i2c.org/en/latest/about/service/shared-responsibility.html#std-role-Hub-Administrator).
  
```

### Who are our Support Team?

The Support Steward role rotates through the below Support Team members.

```{include} ../../_data/tmp/support-stewards.txt
```

## Communication channels

### External communication

We use these channels for communicating with external stakeholders like Community Representatives:

- **[support@2i2c.org](mailto:support@2i2c.org)** is our point-of-contact for all support-related external communication.
- **[The 2i2c FreshDesk account](support:freshdesk)** is where we track all support requests and communication.
- **{doc}`the "Get Support" page <docs:support>`** provides guidance that communities may follow to get support.

(support:freshdesk)=
#### FreshDesk

We use FreshDesk to manage all of our hub support questions and change requests.
It is at the following URL:

[**`2i2c.freshdesk.com`**](https://2i2c.freshdesk.com/)

Any emails sent to `support@2i2c.org` will be routed to this FreshDesk account, and all team members should have access to it.

[**Canned responses**](https://support.freshdesk.com/en/support/solutions/articles/37577-creating-common-reply-templates-with-canned-responses) allow us to pre-populate common responses for many kinds of support.

```{button-link} https://2i2c.freshdesk.com/a/admin/canned_responses/folders
:color: primary
Our canned responses.
```

### Internal communication

We have a few channels for communicating around support requests:

- Our [FreshDesk account](https://2i2c.freshdesk.com/a/) allows for internal team communication via the {guilabel}`Add Note` button. This can be useful for sharing quick internal updates.
- The [Eng & Prod board that collects support-related issues](https://github.com/orgs/2i2c-org/projects/22/views/47) identified via metadata `type==support`.
- (deprecated) [Issues with the {guilabel}`support` label](https://github.com/2i2c-org/infrastructure/issues?q=is%3Aopen+label%3Asupport+sort%3Aupdated-desc) were where we tracked support requests related to {term}`Change Requests` and {term}`Guidance Requests`.

## Process for support triage and resolution

Here is the process that we follow when triaging and resolving support requests.

### Triage process

The goal of the triage phase is to understand the Support Request, decide if it is related to an incident, and choose the appropriate resolution pathway.

This process is carried out in an ongoing basis by the {term}`Support Stewards`.

1. **Monitor our support channels**. We use FreshDesk for all support requests, and the Support Stewards should regularly keep an eye on this account for new requests.
   When a new support requests comes in, move to the next step.
2. **Read and understand**. Within one working day[^working-day], read the support request and try to understand what action would resolve it.
3. **Decide if there is an incident**. Determine if a request meets {term}`the definition of an incident <Incident>`.
4. **Categorize the Support Ticket** in FreshDesk.
5. **If an Incident**, go to [](support:incident-response).
6. **If not an Incident**, go to [](support:non-incident-response).

[^working-day]: We define a working day as a continuous 24 hour period of time from Monday through Friday. This is because our team and the communities we serve are distributed across many time zones, so there is no single "working day" for everyone.

(support:non-incident-response)=
### Non-incident response process

The goal of the non-incident response process is to bring standardization to our support response. This simple workflow tries to battle the bias towards a reactive response whereas it is also bringing some common patterns so all of our non-incident support responses are cohesive and shared among our support stewards.
The current iteration of the workflow states each step and who should be responsible/accountable for the specific step, plus some other clarifications.

When a new ticket lands in Freshdesk under the support group and it is not an incident, you should follow the following steps:

1. `Who: Support steward`

   **Respond within 24 working hours**. Acknowledge receipt of the support request and let the {term}`Community Representative` know a time-boxed investigation will start soon. Please request any additional information you may need to be able to reproduce the issue in step 2.

2. `Who: Support steward`

   **Spend 30 minutes trying to resolve**. If you believe you can resolve the issue within 30 minutes, try resolving it yourself.
   1. If you resolve the issue, then jump to the "Confirm resolution" step 7.
   2. If you don't believe you can resolve the issue (or you couldn't) in 30 minutes, jump to the next step.

3. `Who: Support Steward`

   **Open an engineering issue**. If this is a {term}`Change Request` or {term}`Guidance Request` and/or you cannot resolve the issue within 30 minutes, then open a support issue for the team to discuss.

   [{bdg-primary}`Open a general issue`](https://github.com/2i2c-org/infrastructure/issues/new?assignees=&labels=&template=01_new-issue.yml) that describes the request and any next steps we should take. It should be automatically added to the **Eng & Prod** board by the existing automation. Add the **type**: `support` and choose an **impact** level in the **Eng & Prod** board metadata (available for the very same issue, no need to visit the board itself!).
   
   If the issue has a `critical` impact (we defer that first evaluation to the support steward), an additional ping to the support Slack channel is needed to boost the signal.
   
   The support steward **should** self-assign the `critical` issue and work on it immediately (this is now outside of the 30-minute timebox described in step 2).
   
   If the support stewards (both of them) do not have the capacity to resolve the `critical` issue (ie. working on another `critical` issue, being out of their working time, etc.), they should ping the **Engineering Manager** (or the delegated person) so they can secure resources to resolve that issue on the fly (see step 7 below).
   
   The support steward **should not** work on issues with impact lower than `critical` (unless they are assigned as part of the "planned" reactive work in the context of a running sprint (see step 6 below).

4. `Who: Partnerships representative and the Engineering Manager (or respective delegates)`

   **Revisit the impact metadata**. Once a week (at minimum) the [support view in the **Eng & Prod** board](https://github.com/orgs/2i2c-org/projects/22/views/47) should be revisited to validate the impact level on support-related issues.
     
5. `Who: Support steward`

   **Add a reference/link to the created engineering issue inside the Freshdesk ticket**. You can use an internal note or make it public when you communicate back to the Community Representative in step 6. Also, move the status of the ticket to the "Pending" state.
   
6. `Who: Support steward`

   **Communicate status**. Once we have an issue created to track the next steps, send a message to the Community Representative letting them know about the situation: after some initial investigation and no immediate fix, a follow-up issue was created that will be assigned in the future accordingly to the current prioritization. Also, let them know what the next steps will be. Here's a template to help guide you:

   ```
   Hello { NAME }, thanks for sending us your request. We've concluded that
   this is not related to an outage or diminished service, so we'll incorporate
   this request into our team's work planning process. We'll send an update
   when we've got a plan for completing this request.
   ```

7. `Who: Engineering Manager (currently assigning reactive work) or someone delegated by the Engineering Manager`

   **Prioritize the request**. Any non-`critical` issue should wait to be included in our sprints (on Wednesdays, every other week) to be worked out as part of the "planned" reactive work. Follow the [how to prioritize Change and Guidance Requests guide](support:prioritize-requests) to decide how we should prioritize this request relative to the other work we need to do. We should be fully transparent about the support queue to our Community Representatives if they ping us for updates.
   
   If there is any `critical` issue, we could assign people on the fly (during the sprint) to resolve them, but we should minimize that behavior (it should be exceptional cases).

8. `Who: Support steward`

   **Resolve the request**. When some engineer is assigned to a support-related GH issue in the context of a sprint, we move ahead with the investigation/resolution for one (1) sprint. If we failed to find a fix during that time, we communicate back that state in the Freshdesk ticket and resolve it.

   Exceptional tickets might need more than one sprint. These tickets need to be explicitly approved as exceptions.

9. `Who: Support steward`

   **Confirm resolution**. Once we have resolved a support request, send a message to the Community Representative to confirm that we believe it is resolved. In FreshDesk, mark the incident as {guilabel}`Resolved`.

10. `Who: Support steward`

    **Close the request**. If the Community Representative confirms that their request has been fulfilled, consider this request closed. In FreshDesk, mark the incident as {guilabel}`Closed`.

(support:prioritize-requests)=
## Prioritizing non-incident support requests

For support requests that are not related to {term}`Incidents`, we have more flexibility in when to do the work.
We cannot sustainably prioritize all support requests over our other work, so here is a rough prioritization order to follow:

1. Requests that come with dedicated funding.
1. Requests that impact many communities.
1. Requests that align with our pre-existing goals.
1. Requests that align with an upstream open source project's goals.
1. Requests from communities that haven't used much {term}`Support Budget`.
1. Requests that have a high-impact on a single community.
1. Our other work items
1. Requests from communities that have no more {term}`Support Budget`.

:::{admonition} Ask the PMs
We have a few roles that are particularly useful for triaging and prioritizing our work items.

- Our {role}`Project Manager` should have visibility over everybody's workload, and helps us prioritize work during sprints.
- Our Product and Community Lead should understand which work items will be most impactful across our communities. (we currently do not have anybody serving in this role, but will soon!)

When deciding how to prioritize a Change Request, ask for guidance from these two team members.

:::

### Support request key terms

The following are other important terms and ideas in the support process.

```{glossary}
Support Budget
  A fixed amount of time that we can spend providing support for each community that we serve. This helps us ensure that we can sustainably serve many communities. Any support request that is **not tied to an {term}`Incident`** will draw from the support budget for that community. If a community requests support beyond their support budget, we may request extra funds to help cover our costs.

  :::{note}
  We currently keep this term intentionally vague, and ask that communities are respectful of our time when making change requests.
  We are investigating the support budget that we should give to each community, and will update here when we have specific numbers in mind.

  Here is a rough idea of the rationale we follow as we identify more specific numbers for support budget:

  - Assume 173 working hours a month per engineer.
  - Assume any given engineer should spend no more than 20% of their time (one day a week) on average dealing with support requests.
  - That amounts to 34 hours a month on support requests.
  - Then choose a support budget for each community based on the number of communities we think one engineer can sustainably serve.
  Tie this number back to our question "how many hubs should be able to sustain a single engineer?".
  That ranges between 20 and 8 (depending on edu/research, and dedicated cluster).

  :::
```

(support:expected-time-off)=
## Expected time off and downtime

There are some cases when we intentionally reduce our operations and support capacity.
See [](time-off:annual-expected) for our broader policies and support commitments during this time.

(support:expected-time-off:policy)=
### Expected time off support policy

Below is our policy for support during expected time off:

- We monitor our support e-mail for major incidents, but do not guarantee a response for non-essential requests or questions.
  % NOTE: In the future we may define a policy for support if a community knows and
  %   tells us they are doing essential work during expected time off.
  %   We can update this policy when we discuss and make a decision on this.
  %
  %   Some conversation in: https://github.com/2i2c-org/meta/issues/435
- We will take steps to minimize harm and avoid catastrophic problems (e.g. incidents that drastically increase costs), but will not perform non-essential actions. We will assume there is _no essential work happening on any of our hubs for all communities_.
- If there is a catastrophic incident, we will take the minimal number of actions to reduce risk and damage to a reasonable level.
- For non-catastrophic incidents and general change requests, we will wait until _after this period_ to resolve them.

### Support process during expected time off

Here are the steps we take to set expectations for our team and for other organizations during expected time off:

- **One month before the start of time off**. Add footer content to our `support@2i2c.org` and `hello@2i2c.org` responses that communicates our intent.
  See [](freshdesk:footer) for instructions on doing this.

  Example text:

  > **Note:** the 2i2c team will have **expected reduced capacity** from `STARTDATE` to `ENDDATE`.
  > During this time, we will provide operational support for significant cloud incidents and outages, but not for non-essential questions or change requests.
  > We will be less responsive than normal, and will return to answer your questions and resolve issues after the time off.
- **During the time off**. Add an auto-responder to our FreshDesk accounts with a message like the following:

  > **Note:** the 2i2c team is operating at an **expected reduced capacity** until `ENDDATE`.
  > We will provide operational support for significant cloud incidents and outages, but not for non-essential questions or change requests.
  > We will be less responsive than normal, and will return to answer your questions and resolve issues after the time off.

% TODO: In the future, we want to add two extra steps:
%
% 1. Send an e-mail to our mailing list for Community Representatives communicating our intent to be on expected reduced capacity.
%    ref: https://github.com/2i2c-org/team-compass/issues/579
%
% 2. Add a banner announcement to each of our community hubs.
%    ref: https://github.com/2i2c-org/infrastructure/issues/1501

### Rotating team members during expected time off

Because team members continue to serve as support stewards during this time, we should take care to avoid the same person serving in this role across multiple periods of expected time off.
