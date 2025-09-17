# Terminology

The following are important terms in the support process.

```{glossary}
Support Request
Support Requests
  Any request that a community sends to us via `support@2i2c.org` or the FreshDesk Support widget.
  Support requests are generally un-planned and happen in response to a community needing assistance with something unexpected.
  There are a few main categories of support that we consider, each is described below.

Incident
Incidents
  An event that significantly degrades the JupyterHub service. Support requests that are related to incidents should be prioritized over all other work items.

  [](incidents:what) defines the kind of incidents we respond to via PagerDuty and consider immediate issues to be resolved.

  We do not have a limit on the support time we provide related to incidents (as opposed to Change and Guidance requests, which have a {term}`Support Budget`).

  :::{seealso}
  See [](incidents) for more information.
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
